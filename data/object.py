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
class ParticipantInfo:
    ## Champion info
    champion: str
    level: int
    experience: int
    ## K/D/A
    kills: int
    deaths: int
    assists: int
    ## Damage
    total_damage_to_champion: int
    phisical_damage_to_champion: int
    magic_damage_to_champion: int
    true_damage_to_champion: int
    total_damage_dealt: int
    phisical_damage_dealt: int
    magic_damage_dealt: int
    true_damage_dealt: int
    largest_critical_strike: int
    largest_killing_spree: int
    largest_multi_kill: int
    damage_building: int
    damage_objective: int
    ## Damage taken and healed
    total_heal: int
    total_damage_taken: int
    physical_damage_taken: int
    magic_damage_taken: int
    true_damage_taken: int
    damage_self_mitigated: int
    total_shielded_on_teammate: int
    total_heal_on_teammate: int
    ## Vision
    vision_score: int
    wards_placed: int
    wards_killed: int
    vision_wards_bought_in_game: int
    ## Earned gold
    gold: int
    total_minions_killed: int
    neutral_minions_killed: int
    total_allied_jungle_minions_killed: int
    total_enemy_jungle_minions_killed: int
    ## Other
    turret_kills: int
    turret_takedowns: int
    turrent_lost: int
    ## CC
    time_ccing_others: int
    total_time_cc_dealt: int
    ## Kills
    double_kills: int
    triple_kills: int
    quadra_kills: int
    penta_kills: int
    ## Ping
    all_in_pings: int
    bait_pings: int
    command_pings: int
    danger_pings: int
    enemy_missing_pings: int
    enemy_vision_pings: int
    getback_pings: int
    hold_pings: int
    onmyway_pings: int
    push_pings: int
    ## Items
    item_0: int
    item_1: int
    item_2: int
    item_3: int
    item_4: int
    item_5: int
    item_6: int


@dataclass
class MatchInfo:
    data: dict[str, str | int | bool | dict[str, str]]
    match_id: str = field(init=False)
    game_start_time: int = field(init=False)
    game_duration: int = field(init=False)
    game_end_time: str = field(init=False)
    game_version: str = field(init=False)
    win_team: str = field(init=False)
    #########################
    # Team info - Blue team #
    #########################
    # Bans
    team_blue_ban_1: int = field(init=False)
    team_blue_ban_2: int = field(init=False)
    team_blue_ban_3: int = field(init=False)
    team_blue_ban_4: int = field(init=False)
    team_blue_ban_5: int = field(init=False)
    # Objectives
    ## Baron
    team_blue_baron_first: bool = field(init=False)
    team_blue_baron_kills: int = field(init=False)
    ## Champion
    team_blue_champion_first: bool = field(init=False)
    team_blue_champion_kills: int = field(init=False)
    ## Dragon
    team_blue_dragon_first: bool = field(init=False)
    team_blue_dragon_kills: int = field(init=False)
    ## Inhibitor
    team_blue_inhibitor_first: bool = field(init=False)
    team_blue_inhibitor_kills: int = field(init=False)
    ## Rift Herald
    team_blue_rift_herald_first: bool = field(init=False)
    team_blue_rift_herald_kills: int = field(init=False)
    ## Tower
    team_blue_tower_first: bool = field(init=False)
    team_blue_tower_kills: int = field(init=False)
    ########################
    # Team info - Red team #
    ########################
    # Bans
    team_red_ban_1: int = field(init=False)
    team_red_ban_2: int = field(init=False)
    team_red_ban_3: int = field(init=False)
    team_red_ban_4: int = field(init=False)
    team_red_ban_5: int = field(init=False)
    # Objectives
    ## Baron
    team_red_baron_first: bool = field(init=False)
    team_red_baron_kills: int = field(init=False)
    ## Champion
    team_red_champion_first: bool = field(init=False)
    team_red_champion_kills: int = field(init=False)
    ## Dragon
    team_red_dragon_first: bool = field(init=False)
    team_red_dragon_kills: int = field(init=False)
    ## Inhibitor
    team_red_inhibitor_first: bool = field(init=False)
    team_red_inhibitor_kills: int = field(init=False)
    ## Rift Herald
    team_red_rift_herald_first: bool = field(init=False)
    team_red_rift_herald_kills: int = field(init=False)
    ## Tower
    team_red_tower_first: bool = field(init=False)
    team_red_tower_kills: int = field(init=False)
    #############################
    # Champion info - Blue team #
    #############################
    tema_blue_top: ParticipantInfo = field(init=False)
    tema_blue_jungle: ParticipantInfo = field(init=False)
    tema_blue_mid: ParticipantInfo = field(init=False)
    tema_blue_adc: ParticipantInfo = field(init=False)
    tema_blue_support: ParticipantInfo = field(init=False)
    ############################
    # Champion info - Red team #
    ############################
    tema_red_top: ParticipantInfo = field(init=False)
    tema_red_jungle: ParticipantInfo = field(init=False)
    tema_red_mid: ParticipantInfo = field(init=False)
    tema_red_adc: ParticipantInfo = field(init=False)
    tema_red_support: ParticipantInfo = field(init=False)

    def __post_init__(self):
        self.match_id = self.data["metadata"]["matchId"]
        self.game_start_time = self.data["info"]["gameStartTimestamp"]
        self.game_duration = self.data["info"]["gameDuration"]
        self.game_end_time = self.data["info"]["gameEndTimestamp"]
        self.game_version = self.data["info"]["gameVersion"]
        #############
        # Team info #
        #############
        for team in self.data["info"]["teams"]:
            # Blue team
            if team["teamId"] == 100:
                # Bans
                self.team_blue_ban_1 = team["bans"][0]["championId"]
                self.team_blue_ban_2 = team["bans"][1]["championId"]
                self.team_blue_ban_3 = team["bans"][2]["championId"]
                self.team_blue_ban_4 = team["bans"][3]["championId"]
                self.team_blue_ban_5 = team["bans"][4]["championId"]
                # Baron
                self.team_blue_baron_first = team["objectives"]["baron"]["first"]
                self.team_blue_baron_kills = team["objectives"]["baron"]["kills"]
                # Champion
                self.team_blue_champion_first = team["objectives"]["champion"]["first"]
                self.team_blue_champion_kills = team["objectives"]["champion"]["kills"]
                # Dragon
                self.team_blue_dragon_first = team["objectives"]["dragon"]["first"]
                self.team_blue_dragon_kills = team["objectives"]["dragon"]["kills"]
                # Inhibitor
                self.team_blue_inhibitor_first = team["objectives"]["inhibitor"][
                    "first"
                ]
                self.team_blue_inhibitor_kills = team["objectives"]["inhibitor"][
                    "kills"
                ]
                # Rift Herald
                self.team_blue_rift_herald_first = team["objectives"]["riftHerald"][
                    "first"
                ]
                self.team_blue_rift_herald_kills = team["objectives"]["riftHerald"][
                    "kills"
                ]
                # Tower
                self.team_blue_tower_first = team["objectives"]["tower"]["first"]
                self.team_blue_tower_kills = team["objectives"]["tower"]["kills"]
                # Win
                if team["objectives"]["win"]:
                    self.win_team = "Blue"
            # Red team
            else:
                # Bans
                self.team_red_ban_1 = team["bans"][0]["championId"]
                self.team_red_ban_2 = team["bans"][1]["championId"]
                self.team_red_ban_3 = team["bans"][2]["championId"]
                self.team_red_ban_4 = team["bans"][3]["championId"]
                self.team_red_ban_5 = team["bans"][4]["championId"]
                # Baron
                self.team_red_baron_first = team["objectives"]["baron"]["first"]
                self.team_red_baron_kills = team["objectives"]["baron"]["kills"]
                # Champion
                self.team_red_champion_first = team["objectives"]["champion"]["first"]
                self.team_red_champion_kills = team["objectives"]["champion"]["kills"]
                # Dragon
                self.team_red_dragon_first = team["objectives"]["dragon"]["first"]
                self.team_red_dragon_kills = team["objectives"]["dragon"]["kills"]
                # Inhibitor
                self.team_red_inhibitor_first = team["objectives"]["inhibitor"]["first"]
                self.team_red_inhibitor_kills = team["objectives"]["inhibitor"]["kills"]
                # Rift Herald
                self.team_red_rift_herald_first = team["objectives"]["riftHerald"][
                    "first"
                ]
                self.team_red_rift_herald_kills = team["objectives"]["riftHerald"][
                    "kills"
                ]
                # Tower
                self.team_red_tower_first = team["objectives"]["tower"]["first"]
                self.team_red_tower_kills = team["objectives"]["tower"]["kills"]
                # Win
                if team["objectives"]["win"]:
                    self.win_team = "Red"

        ################
        # Participants #
        ################
        for participant in self.data["info"]["participants"]:
            # Blue team
            if participant["teamId"] == 100:
                # Top
                if participant["teamPosition"] == "TOP":
                    self.tema_blue_top = self.create_participants(participant)
                # Jungle
                elif participant["teamPosition"] == "JUNGLE":
                    self.tema_blue_jungle = self.create_participants(participant)
                # Mid
                elif participant["teamPosition"] == "MIDDLE":
                    self.tema_blue_mid = self.create_participants(participant)
                # ADC
                elif (
                    participant["teamPosition"] == "BOTTOM"
                    and participant["role"] == "SOLO"
                ):
                    self.tema_blue_adc = self.create_participants(participant)
                # Support
                elif (
                    participant["teamPosition"] == "BOTTOM"
                    and participant["role"] == "UTILITY"
                ):
                    self.tema_blue_support = self.create_participants(participant)
            # Red team
            else:
                # Top
                if participant["teamPosition"] == "TOP":
                    self.tema_red_top = self.create_participants(participant)
                # Jungle
                elif participant["teamPosition"] == "JUNGLE":
                    self.tema_red_jungle = self.create_participants(participant)
                # Mid
                elif participant["teamPosition"] == "MIDDLE":
                    self.tema_red_mid = self.create_participants(participant)
                # ADC
                elif (
                    participant["teamPosition"] == "BOTTOM"
                    and participant["role"] == "SOLO"
                ):
                    self.tema_red_adc = self.create_participants(participant)
                # Support
                elif (
                    participant["teamPosition"] == "BOTTOM"
                    and participant["role"] == "UTILITY"
                ):
                    self.tema_red_support = self.create_participants(participant)

    def create_participants(self, participant):
        return ParticipantInfo(
            champion=participant["championName"],
            level=participant["champLevel"],
            experience=participant["champExperience"],
            kills=participant["kills"],
            deaths=participant["deaths"],
            assists=participant["assists"],
            total_damage_to_champion=participant["totalDamageDealtToChampions"],
            phisical_damage_to_champion=participant["physicalDamageDealtToChampions"],
            magic_damage_to_champion=participant["magicDamageDealtToChampions"],
            true_damage_to_champion=participant["trueDamageDealtToChampions"],
            total_damage_dealt=participant["totalDamageDealt"],
            phisical_damage_dealt=participant["physicalDamageDealt"],
            magic_damage_dealt=participant["magicDamageDealt"],
            true_damage_dealt=participant["trueDamageDealt"],
            largest_critical_strike=participant["largestCriticalStrike"],
            largest_killing_spree=participant["largestKillingSpree"],
            largest_multi_kill=participant["largestMultiKill"],
            damage_building=participant["damageDealtToBuildings"],
            damage_objective=participant["damageDealtToObjectives"],
            total_heal=participant["totalHeal"],
            total_damage_taken=participant["totalDamageTaken"],
            physical_damage_taken=participant["physicalDamageTaken"],
            magic_damage_taken=participant["magicDamageTaken"],
            true_damage_taken=participant["trueDamageTaken"],
            damage_self_mitigated=participant["damageSelfMitigated"],
            total_shielded_on_teammate=participant["totalDamageShieldedOnTeammates"],
            total_heal_on_teammate=participant["totalHealOnTeammates"],
            vision_score=participant["visionScore"],
            wards_placed=participant["wardsPlaced"],
            wards_killed=participant["wardsKilled"],
            vision_wards_bought_in_game=participant["visionWardsBoughtInGame"],
            gold=participant["goldEarned"],
            total_minions_killed=participant["totalMinionsKilled"],
            neutral_minions_killed=participant["neutralMinionsKilled"],
            total_allied_jungle_minions_killed=participant[
                "totalAllyJungleMinionsKilled"
            ],
            total_enemy_jungle_minions_killed=participant[
                "totalEnemyJungleMinionsKilled"
            ],
            turret_kills=participant["turretKills"],
            turret_takedowns=participant["turretTakedowns"],
            turrent_lost=participant["turretsLost"],
            time_ccing_others=participant["timeCCingOthers"],
            total_time_cc_dealt=participant["totalTimeCCDealt"],
            double_kills=participant["doubleKills"],
            triple_kills=participant["tripleKills"],
            quadra_kills=participant["quadraKills"],
            penta_kills=participant["pentaKills"],
            all_in_pings=participant["allInPings"],
            bait_pings=participant["baitPings"],
            command_pings=participant["commandPings"],
            danger_pings=participant["dangerPings"],
            enemy_missing_pings=participant["enemyMissingPings"],
            enemy_vision_pings=participant["enemyVisionPings"],
            getback_pings=participant["getBackPings"],
            hold_pings=participant["holdPings"],
            onmyway_pings=participant["onMyWayPings"],
            push_pings=participant["pushPings"],
            item_0=participant["item0"],
            item_1=participant["item1"],
            item_2=participant["item2"],
            item_3=participant["item3"],
            item_4=participant["item4"],
            item_5=participant["item5"],
            item_6=participant["item6"],
        )
