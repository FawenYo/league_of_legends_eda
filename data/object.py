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
    team_blue_largest_critical_strike: int
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
    total_all_jungle_minions_killed: int
    total_allied_jungle_minions_killed: int
    total_enemy_jungle_minions_killed: int
    ## Other
    turret_kills: int
    turret_takedowns: int
    ## CC
    time_ccing_others: int
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
    tema_blue_top: ParticipantInfo
    tema_blue_jungle: ParticipantInfo
    tema_blue_mid: ParticipantInfo
    tema_blue_adc: ParticipantInfo
    tema_blue_support: ParticipantInfo
    ############################
    # Champion info - Red team #
    ############################
    tema_red_top: ParticipantInfo
    tema_red_jungle: ParticipantInfo
    tema_red_mid: ParticipantInfo
    tema_red_adc: ParticipantInfo
    tema_red_support: ParticipantInfo
