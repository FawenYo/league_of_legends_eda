import os
import pickle
import random
from typing import Optional

from dotenv import load_dotenv
from loguru import logger
from riotwatcher import LolWatcher
from tqdm import tqdm

from data.object import MatchInfo, Player


class Game:
    def __init__(self) -> None:
        self.load_env()
        self.player_region = "tw2"
        self.server_region = "sea"
        self.lol_wathers = [
            LolWatcher(os.getenv("RIOT_API_KEY_1")),
            LolWatcher(os.getenv("RIOT_API_KEY_2")),
            LolWatcher(os.getenv("RIOT_API_KEY_3")),
            LolWatcher(os.getenv("RIOT_API_KEY_4")),
            LolWatcher(os.getenv("RIOT_API_KEY_5")),
        ]

    def load_env(self) -> None:
        """Load environment variables"""
        load_dotenv()

    def get_player_details(self, player: Player, tier: str) -> Player:
        """Get player details

        Args:
            player (Player): Player informaton
            tier (str): Player tier

        Returns:
            Player: Player detail information
        """
        lol_watcher = random.choice(self.lol_wathers)
        info = lol_watcher.summoner.by_account(self.player_region, player.account_id)
        if tier:
            player.tier = tier
        player.account_id = info["accountId"]
        player.puuid = info["puuid"]
        player.summoner_level = info["summonerLevel"]
        return player

    def get_match_id(
        self, user_puuid: str, start_time: int, end_time: int, count: int
    ) -> list[str]:
        """Get match id

        Args:
            user_puuid (str): Player puuid
            start_time (int): Start time
            end_time (int): End time
            count (int): Number of matches

        Returns:
            list[str]: List of match id
        """
        lol_watcher = random.choice(self.lol_wathers)
        return lol_watcher.match.matchlist_by_puuid(
            region=self.server_region,
            puuid=user_puuid,
            count=count,
            start_time=start_time,
            end_time=end_time,
        )

    def get_match_info(self, match_id: str) -> dict:
        """Get match info

        Args:
            match_id (str): Match id

        Returns:
            dict: Match info
        """
        lol_watcher = random.choice(self.lol_wathers)
        return lol_watcher.match.by_id(region=self.server_region, match_id=match_id)

    def get_league_entries(
        self, tier: str, division: Optional[str] = ""
    ) -> list[dict[str, str]]:
        """Get league entries

        Args:
            tier (str): Rank tier
            division (Optional[str], optional): Tier division. Defaults to "".

        Returns:
            list[dict[str, str]]: List of players
        """
        # IRON, BRONZE, SILVER, GOLD, PLATINUM, DIAMOND
        if division:
            result = []
            for page_index in range(1, 6):
                lol_watcher = random.choice(self.lol_wathers)
                entries = lol_watcher.league.entries(
                    region=self.player_region,
                    queue="RANKED_SOLO_5x5",
                    tier=tier,
                    division=division,
                    page=page_index,
                )
                result += entries
            return result

        elif tier == "MASTER":
            lol_watcher = random.choice(self.lol_wathers)
            return lol_watcher.league.masters_by_queue(
                region=self.player_region, queue="RANKED_SOLO_5x5"
            )
        elif tier == "GRANDMASTER":
            lol_watcher = random.choice(self.lol_wathers)
            return lol_watcher.league.grandmaster_by_queue(
                region=self.player_region, queue="RANKED_SOLO_5x5"
            )
        elif tier == "CHALLENGER":
            lol_watcher = random.choice(self.lol_wathers)
            return lol_watcher.league.challenger_by_queue(
                region=self.player_region, queue="RANKED_SOLO_5x5"
            )

    def get_all_players(self, new_data: bool = True) -> list[Player]:
        """Get all players

        Args:
            new_data (bool, optional): Get new data or not. Defaults to True.

        Returns:
            list[Player]: List of players
        """
        if new_data:
            # Utils
            def get_data(player: Player, tier: Optional[str] = "") -> Player:
                """Get player data"""
                try:
                    player = Player(data=player)
                    return self.get_player_details(player=player, tier=tier)
                except Exception as e:
                    pass
                    return None

            players: list[Player] = []

            logger.info("Getting players data")
            DIVISIONS = ["IV", "III", "II", "I"]
            ENTRIES_TIERS = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]
            ADVANCED_TIERS = ["MASTER", "GRANDMASTER", "CHALLENGER"]

            for tier in ENTRIES_TIERS:
                for division in DIVISIONS:
                    logger.debug(f"Getting {tier} {division} players")
                    _league_entries = self.get_league_entries(
                        tier=tier, division=division
                    )
                    for player in tqdm(_league_entries):
                        player = get_data(player)
                        if player:
                            players.append(player)

            for tier in ADVANCED_TIERS:
                logger.debug(f"Getting {tier} players")
                _league_entries = self.get_league_entries(tier=tier)["entries"]
                for player in tqdm(_league_entries):
                    player = get_data(player, tier=tier.lower())
                    if player:
                        players.append(player)
            pickle.dump(players, open("players.pkl", "wb"))
            return players
        else:
            return pickle.load(open("players.pkl", "rb"))

    def get_all_match_id(
        self,
        players: list[Player],
        start_time: int,
        end_time: int,
        new_data: bool = True,
    ) -> dict[str, int]:
        """Get all match id

        Args:
            players (list[Player]): List of players
            start_time (int): Start time
            end_time (int): End time
            new_data (bool, optional): Get new data or not. Defaults to True.

        Returns:
            dict[str, int]: List of match id
        """
        if new_data:
            match_id_list = {}
            for player in tqdm(players):
                player_matches = self.get_match_id(
                    user_puuid=player.puuid,
                    start_time=start_time,
                    end_time=end_time,
                    count=20,
                )
                for match in player_matches:
                    if match not in match_id_list:
                        match_id_list[match] = 1
            pickle.dump(match_id_list, open("match_id_list.pkl", "wb"))
            return match_id_list
        else:
            return pickle.load(open("match_id_list.pkl", "rb"))

    def parse_match_info(self, match_info: dict) -> MatchInfo:
        """Parse match info

        Args:
            match_info (dict): Match info

        Returns:
            MatchInfo: Match info
        """
        match_info = MatchInfo(data=match_info)
        return match_info

    def fetch_all(self, start_time: int, end_time: int) -> list[str]:
        """Fetch all data

        Args:
            start_time (int): Start time
            end_time (int): End time

        Returns:
            list[str]: List of match info
        """
        result: list[MatchInfo] = []
        # Get players
        players = self.get_all_players()

        # Get match list
        match_id_list = self.get_all_match_id(
            players=players, start_time=start_time, end_time=end_time
        )
        for match in tqdm(match_id_list.keys()):
            match_info_dict = self.get_match_info(match_id=match)
            match_info = self.parse_match_info(match_info=match_info_dict)
            result.append(match_info)
        return result
