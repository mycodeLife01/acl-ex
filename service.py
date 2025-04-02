from models import (
    Season,
    Schedule,
    Team_Info,
    Match,
    PlayerList,
    RealTimeMatch,
    RealTimePlayer,
    TeamOffline,
    PlayerOffline,
)
from sqlalchemy import and_
import logging


def get_season_all():
    try:
        seasons = [
            {
                "seasonId": season.season_id,
                "seasonName": season.season_name,
                "startTime": season.season_start_time,
                "endTime": season.season_end_time,
            }
            for season in Season.query.all()
        ]
        return seasons
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_season_by_startTime(start_time):
    try:
        result = Season.query.filter(Season.season_start_time == start_time).first()
        season = [
            {
                "seasonId": result.season_id,
                "seasonName": result.season_name,
                "startTime": result.season_start_time,
                "endTime": result.season_end_time,
            }
        ]
        return season
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_season_by_endTime(end_time):
    try:
        result = Season.query.filter(Season.season_end_time == end_time).first()
        season = [
            {
                "seasonId": result.season_id,
                "seasonName": result.season_name,
                "startTime": result.season_start_time,
                "endTime": result.season_end_time,
            }
        ]
        return season
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_season_by_startTime_endTime(start_time, end_time):
    try:
        result = Season.query.filter(
            and_(
                Season.season_start_time == start_time,
                Season.season_end_time == end_time,
            )
        ).first()
        season = [
            {
                "seasonId": result.season_id,
                "seasonName": result.season_name,
                "startTime": result.season_start_time,
                "endTime": result.season_end_time,
            }
        ]
        return season
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_schedule_all():
    try:
        schedules = [
            {
                "scheduleId": schedule.schedule_id,
                "season_id": schedule.season_id,
                "scheduleName": schedule.schedule_name,
                "scheduleStartTime": schedule.schedule_start_time,
                "scheduleStatus": schedule.schedule_status,
                "teamScoreList": [
                    {"teamId": schedule.team_1, "score": schedule.team_1_score},
                    {"teamId": schedule.team_2, "score": schedule.team_2_score},
                ],
                "stageId": schedule.stage_id,
                "stageName": schedule.stage_name,
                "scheduleType": schedule.schedule_type,
            }
            for schedule in Schedule.query.all()
        ]
        season_dict = {}
        for s in schedules:
            season_id = s["season_id"]
            del s["season_id"]
            if season_id not in season_dict:
                season_dict[season_id] = {
                    "seasonId": season_id,
                    "scheduleList": [s],
                }
            else:
                season_dict[season_id]["scheduleList"].append(s)
        return list(season_dict.values())
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_schedule_by_id(id):
    try:
        schedule_result = schedule.query.get(id)
        schedule = {
            "season_id": 0,
            "schedule_list": {
                "schedule_id": schedule_result.schedule_id,
                "season_id": schedule_result.season_id,
                "schedule_name": schedule_result.schedule_name,
                "schedule_start_time": schedule_result.schedule_start_time,
                "schedule_status": schedule_result.schedule_status,
                "team_score_list": [
                    {
                        "team_name": schedule_result.team_1,
                        "score": schedule_result.team_1_score,
                    },
                    {
                        "team_name": schedule_result.team_2,
                        "score": schedule_result.team_2_score,
                    },
                ],
                "stage_id": schedule_result.stage_id,
                "stage_name": schedule_result.stage_name,
            },
        }
        return schedule
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_schedule_by_ids(ids):
    try:
        schedules_result = Schedule.query.filter(Schedule.schedule_id.in_(ids)).all()
        schedules = [
            {
                "schedule_id": schedule.schedule_id,
                "season_id": schedule.season_id,
                "schedule_name": schedule.schedule_name,
                "schedule_start_time": schedule.schedule_start_time,
                "schedule_status": schedule.schedule_status,
                "team_score_list": [
                    {"team_name": schedule.team_1, "score": schedule.team_1_score},
                    {"team_name": schedule.team_2, "score": schedule.team_2_score},
                ],
                "stage_id": schedule.stage_id,
                "stage_name": schedule.stage_name,
            }
            for schedule in schedules_result
        ]
        return schedules
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_schedule_by_season(id):
    try:
        schedules = [
            {
                "seasonId": id,
                "scheduleList": [
                    {
                        "scheduleId": schedule.schedule_id,
                        "seasonId": schedule.season_id,
                        "scheduleName": schedule.schedule_name,
                        "scheduleStartTime": schedule.schedule_start_time,
                        "scheduleStatus": schedule.schedule_status,
                        "teamScoreList": [
                            {
                                "teamId": schedule.team_1,
                                "score": schedule.team_1_score,
                            },
                            {
                                "teamId": schedule.team_2,
                                "score": schedule.team_2_score,
                            },
                        ],
                        "stageId": schedule.stage_id,
                        "stageName": schedule.stage_name,
                        "scheduleType": schedule.schedule_type,
                    }
                    for schedule in Schedule.query.filter(
                        Schedule.season_id == id
                    ).all()
                ],
            }
        ]
        for season in schedules:
            schedules_in_season = season["scheduleList"]
            for schedule in schedules_in_season:
                del schedule["seasonId"]
        return schedules
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_schedule_by_seasons(ids):
    try:
        schedules = [
            {
                "seasonId": id,
                "scheduleList": [
                    {
                        "scheduleId": schedule.schedule_id,
                        "seasonId": schedule.season_id,
                        "scheduleName": schedule.schedule_name,
                        "scheduleStartTime": schedule.schedule_start_time,
                        "scheduleStatus": schedule.schedule_status,
                        "teamScoreList": [
                            {
                                "teamId": schedule.team_1,
                                "score": schedule.team_1_score,
                            },
                            {
                                "teamId": schedule.team_2,
                                "score": schedule.team_2_score,
                            },
                        ],
                        "stageId": schedule.stage_id,
                        "stageName": schedule.stage_name,
                        "scheduleType": schedule.schedule_type,
                    }
                    for schedule in Schedule.query.filter(
                        Schedule.season_id.in_(ids)
                    ).all()
                ],
            }
            for id in ids
        ]
        for season in schedules:
            schedules_in_season = season["scheduleList"]
            for schedule in schedules_in_season:
                del schedule["seasonId"]
        return schedules
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_team_all():
    try:
        teams = [
            {
                "teamId": team.team_id,
                "name": team.team_name,
                "logo": team.team_logo,
            }
            for team in TeamOffline.query.all()
        ]
        return teams
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_team_by_schedule(id):
    try:
        team_set = set()
        for team_1, team_2 in (
            Schedule.query.with_entities(Schedule.team_1, Schedule.team_2)
            .filter(Schedule.schedule_id == id)
            .all()
        ):
            team_set.add(team_1)
            team_set.add(team_2)
        teams = [
            {
                "teamId": t.team_id,
                "name": t.team_name,
                "logo": t.team_logo,
            }
            for t in TeamOffline.query.filter(TeamOffline.team_id.in_(team_set)).all()
        ]
        return teams
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_team_by_schedules(ids):
    try:
        res = []
        for id in ids:
            teams = get_team_by_schedule(id)
            for team in teams:
                team_names = []
                for item in res:
                    if item is not None:
                        team_names.append(item["name"])
                if team["name"] not in team_names:
                    res.append(team)
        return res
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_team_by_season(id):
    try:
        # team_set = set()
        # for team_1, team_2 in (
        #     Schedule.query.with_entities(Schedule.team_1, Schedule.team_2)
        #     .filter(Schedule.season_id == id)
        #     .all()
        # ):
        #     team_set.add(team_1)
        #     team_set.add(team_2)
        # teams = [
        #     {
        #         "teamId": t.team_id,
        #         "name": t.team_name,
        #         "logo": t.team_logo,
        #     }
        #     for t in Team_Info.query.filter(Team_Info.team_name.in_(team_set)).all()
        # ]
        # return teams
        return get_team_all()
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_team_by_seasons(ids):
    try:
        # res = set()
        # for id in ids:
        #     teams = get_team_by_season(id)
        #     res.add(teams)
        # return res
        return get_team_all()
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_match_all():
    try:
        matches = [
            {
                "matchId": match.match_id,
                "scheduleId": match.schedule_id,
                "matchStartTime": match.match_start_time,
                "matchEndTime": match.match_end_time,
                "winner": match.winner,
                "matchOrder": match.match_num,
            }
            for match in Match.query.all()
        ]
        grouped_matches = {}
        for match in matches:
            schedule_id = match["scheduleId"]
            if schedule_id not in grouped_matches:
                grouped_matches[schedule_id] = []  # 初始化一个空列表
            del match["scheduleId"]
            grouped_matches[schedule_id].append(
                match
            )  # 将当前 match 添加到对应的 schedule_id 列表中
        # 整理结果
        res = [
            {"scheduleId": schedule_id, "matchList": grouped_matches[schedule_id]}
            for schedule_id in grouped_matches
        ]
        return res
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_match_by_schedule(id):
    try:
        res = []
        matches = get_match_all()
        for match in matches:
            if match["scheduleId"] == id:
                res.append(match)
        return res
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_match_by_schedules(ids):
    try:
        res = []
        for id in ids:
            matches = get_match_by_schedule(id)
            res.append(matches)
        return res
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_players():
    try:
        res = [
            {"playerName": char_name.split("_")[1], "teamId": team_id, "photo": photo}
            for (char_name, team_id, photo) in PlayerOffline.query.with_entities(
                PlayerOffline.char_name,
                PlayerOffline.team_id,
                PlayerOffline.profile_photo,
            )
            .order_by(PlayerOffline.team_id.asc())
            .all()
        ]
        return res
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_real_time_match():
    try:
        match_id_ongoing = (
            Match.query.with_entities(Match.match_id)
            .filter(Match.match_status == 2)
            .scalar()
        )
        # match_id_end = (
        #     Match.query.with_entities(Match.match_id)
        #     .filter(Match.match_status == 3)
        #     .order_by(Match.match_id.desc())
        #     .limit(1)
        #     .scalar()
        # )
        # q_id = match_id_ongoing if match_id_ongoing else match_id_end
        if match_id_ongoing:
            q_id = match_id_ongoing
        else:
            return None
        real_time_match_info: RealTimeMatch = RealTimeMatch.query.filter(
            RealTimeMatch.match_id == q_id
        ).first()
        player_info: list[RealTimePlayer] = RealTimePlayer.query.filter(
            RealTimePlayer.match_id == q_id
        ).all()
        match_info: Match = Match.query.filter(Match.match_id == q_id).first()
        return {
            "matchId": real_time_match_info.match_id,
            "matchStatus": match_info.match_status,
            "winner_team": match_info.winner,
            "team_1": {
                "teamId": real_time_match_info.team_1,
                "teamName": real_time_match_info.team_1,
                "teamScore": real_time_match_info.team_1_score,
                "playerStats": [
                    {
                        "steamId": p.steam_id,
                        "playerName": p.player_name,
                        "kills": p.kills,
                        "deaths": p.deaths,
                        "assists": p.assists,
                    }
                    for p in player_info
                    if p.team == real_time_match_info.team_1
                ],
            },
            "team_2": {
                "teamId": real_time_match_info.team_2,
                "teamName": real_time_match_info.team_2,
                "teamScore": real_time_match_info.team_2_score,
                "playerStats": [
                    {
                        "steamId": p.steam_id,
                        "playerName": p.player_name,
                        "kills": p.kills,
                        "deaths": p.deaths,
                        "assists": p.assists,
                    }
                    for p in player_info
                    if p.team == real_time_match_info.team_2
                ],
            },
        }

    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None


def get_real_time_player():

    def process_players(players):
        team_player_dict = {}
        for player in players:
            p = dict(player)
            team = p["team"]
            match_id = p["matchId"]
            del p["matchId"]
            if team not in list(team_player_dict.keys()):
                team_player_dict.update(
                    {
                        team: [
                            p,
                        ]
                    }
                )
            else:
                team_player_dict[team].append(player)
        return {"match_id": match_id, "team_player_dict": team_player_dict}

    try:
        match_id = (
            Match.query.with_entities(Match.match_id)
            .filter(Match.match_status == 2)
            .scalar()
        )
        if match_id:
            players = [
                {
                    "matchId": player.match_id,
                    "steamId": player.steam_id,
                    "team": player.team,
                    "playerName": player.player_name,
                    "team": player.team,
                    "kills": player.kills,
                    "deaths": player.deaths,
                    "assists": player.assists,
                }
                for player in RealTimePlayer.query.filter(
                    RealTimePlayer.match_id == match_id
                )
                .order_by(RealTimePlayer.team.asc())
                .all()
            ]
            d = process_players(players)["team_player_dict"]
            res = {"matchStatus": 2, "matchId": match_id}
            team_list = list(d.values())
        else:
            players = [
                {
                    "matchId": player.match_id,
                    "steamId": player.steam_id,
                    "playerName": player.player_name,
                    "team": player.team,
                    "kills": player.kills,
                    "deaths": player.deaths,
                    "assists": player.assists,
                }
                for player in RealTimePlayer.query.order_by(
                    RealTimePlayer.match_id.desc()
                ).limit(10)
            ]
            d = process_players(players)["team_player_dict"]
            match_id = process_players(players)["match_id"]
            team_list = list(d.values())
            res = {"matchStatus": 3, "matchId": match_id}

        if team_list[0][0]["team"] == get_real_time_match()["team_1"]:
            res["team_1"] = team_list[0]
            res["team_2"] = team_list[1]
        else:
            res["team_1"] = team_list[1]
            res["team_2"] = team_list[0]
        return res

    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return None
