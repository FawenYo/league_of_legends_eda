from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Player:
    data: dict[str, str]
    id: str = field(init=False)
    account_id: Optional[str] = ""
    puuid: Optional[str] = ""
    name: str = field(init=False)
    summoner_level: Optional[int] = 0
    tier: str = field(init=False)
    rank: str = field(init=False)
    league_points: int = field(init=False)
    wins: int = field(init=False)
    losses: int = field(init=False)
    veteran: bool = field(init=False)
    inactive: bool = field(init=False)
    fresh_blood: bool = field(init=False)
    hot_streak: bool = field(init=False)

    def __post_init__(self):
        self.id = self.data["summonerId"]
        self.name = self.data["summonerName"]
        try:
            self.tier = self.data["tier"]
        except:
            self.tier = ""
        self.rank = self.data["rank"]
        self.league_points = self.data["leaguePoints"]
        self.wins = self.data["wins"]
        self.losses = self.data["losses"]
        self.veteran = self.data["veteran"]
        self.inactive = self.data["inactive"]
        self.fresh_blood = self.data["freshBlood"]
        self.hot_streak = self.data["hotStreak"]

@dataclass
class MatchInfo:
    match_id: str
    game_start_time: int
    game_duration: int
    game_end_time: str
    game_version: str
    win_team: str
    #########################
    # Team info - Blue team #
    #########################
    # Bans
    team_blue_ban_1: int
    team_blue_ban_2: int
    team_blue_ban_3: int
    team_blue_ban_4: int
    team_blue_ban_5: int
    # Objectives
    ## Baron
    team_blue_baron_first: bool
    team_blue_baron_kills: int
    ## Champion
    team_blue_champion_first: bool
    team_blue_champion_kills: int
    ## Dragon
    team_blue_dragon_first: bool
    team_blue_dragon_kills: int
    ## Inhibitor
    team_blue_inhibitor_first: bool
    team_blue_inhibitor_kills: int
    ## Rift Herald
    team_blue_rift_herald_first: bool
    team_blue_rift_herald_kills: int
    ## Tower
    team_blue_tower_first: bool
    team_blue_tower_kills: int
    ########################
    # Team info - Red team #
    ########################
    # Bans
    team_red_ban_1: int
    team_red_ban_2: int
    team_red_ban_3: int
    team_red_ban_4: int
    team_red_ban_5: int
    # Objectives
    ## Baron
    team_red_baron_first: bool
    team_red_baron_kills: int
    ## Champion
    team_red_champion_first: bool
    team_red_champion_kills: int
    ## Dragon
    team_red_dragon_first: bool
    team_red_dragon_kills: int
    ## Inhibitor
    team_red_inhibitor_first: bool
    team_red_inhibitor_kills: int
    ## Rift Herald
    team_red_rift_herald_first: bool
    team_red_rift_herald_kills: int
    ## Tower
    team_red_tower_first: bool
    team_red_tower_kills: int
    #############################
    # Champion info - Blue team #
    #############################
    # Top
    ## Champion info
    team_blue_top_champion: str
    team_blue_top_level: int
    team_blue_top_experience: int
    ## Stats
    team_blue_top_kills: int
    team_blue_top_deaths: int
    team_blue_top_assists: int
    team_blue_top_gold: int
    ## Damage
    team_blue_top_damage_building: int
    team_blue_top_damage_objective: int
    team_blue_top_damage_turrents: int
    team_blue_top_phisical_damage: int
    team_blue_top_phisical_damage_to_champion: int
    team_blue_top_total_damage: int
    team_blue_top_total_damage_to_champion: int
    ## Healing
    team_blue_top_damage_self_mitigated: int
    team_blue_top_physical_damage_taken: int
    team_blue_top_total_damage_taken: int
    team_blue_top_total_shielded_on_teammate: int
    team_blue_top_total_heal: int
    team_blue_top_total_heal_on_teammate: int
    ## CC
    team_blue_top_time_ccing_others: int

    ## Kills
    team_blue_top_double_kills: int
    team_blue_top_triple_kills: int
    team_blue_top_quadra_kills: int
    team_blue_top_penta_kills: int