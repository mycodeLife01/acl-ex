from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
from extensions import db
from service import *
import logging
import json

main_bp = Blueprint("main", __name__, url_prefix="/acl/api")


@main_bp.route("/")
def root():
    return jsonify({"status": "operational"})


@main_bp.route("/seasons")
def seasons():
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")
    try:
        if start_time and not end_time:
            seasons = get_season_by_startTime(start_time)
        elif end_time and not start_time:
            seasons = get_season_by_endTime(end_time)
        elif start_time and end_time:
            seasons = get_season_by_startTime_endTime(start_time, end_time)
        elif not (request.args or request.is_json):
            seasons = get_season_all()
        else:
            return jsonify({"code": 400, "message": "查询参数错误"})

        if not season_checked(seasons):
            return jsonify({"code": 404, "message": "查询的数据不存在"})
        return jsonify({"code": 200, "data": seasons, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


@main_bp.route("/schedules")
def schedules():
    season_id = request.args.get("season_id")
    # season_ids = request.get_json().get("season_ids") if request.is_json else None
    season_ids_param = request.args.get("season_ids")

    season_ids = json.loads(season_ids_param) if season_ids_param else None

    try:
        if season_id and not season_ids:
            schedules = get_schedule_by_season(season_id)
        elif season_ids and not season_id:
            schedules = get_schedule_by_seasons(season_ids)
        elif not (request.args or season_ids):
            schedules = get_schedule_all()
        else:
            return jsonify({"code": 400, "message": "查询参数错误"})
        if not schedule_checked(schedules):
            return jsonify({"code": 404, "message": "查询的数据不存在"})
        return jsonify({"code": 200, "data": schedules, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


@main_bp.route("/teams")
def teams():
    season_id = request.args.get("season_id")
    schedule_id = request.args.get("schedule_id")
    # season_ids = request.get_json().get("season_ids") if request.is_json else None
    # schedule_ids = request.get_json().get("schedule_ids") if request.is_json else None

    season_ids_param = request.args.get("season_ids")
    schedule_ids_param = request.args.get("schedule_ids")

    season_ids = json.loads(season_ids_param) if season_ids_param else None
    schedule_ids = json.loads(schedule_ids_param) if schedule_ids_param else None

    try:
        if not (request.args or season_ids or schedule_ids):
            teams = get_team_all()
        elif season_id and not (schedule_id or season_ids or schedule_ids):
            if season_id != "1":
                return jsonify({"code": 404, "message": "查询的数据不存在"})
            teams = get_team_by_season(season_id)
        elif schedule_id and not (season_id or season_ids or schedule_ids):
            teams = get_team_by_schedule(schedule_id)
        elif season_ids and not (season_id or schedule_id or schedule_ids):
            if int(1) not in season_ids:
                return jsonify({"code": 404, "message": "查询的数据不存在"})
            teams = get_team_by_seasons(season_ids)
        elif schedule_ids and not (season_id or schedule_id or season_ids):
            teams = get_team_by_schedules(schedule_ids)
        else:
            return jsonify({"code": 400, "message": "查询参数错误"})

        if teams is None or teams == []:
            return jsonify({"code": 404, "message": "查询的数据不存在"})
        else:
            return jsonify({"code": 200, "data": teams, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


@main_bp.route("/matches")
def matches():
    schedule_id = request.args.get("schedule_id")
    # schedule_ids = request.get_json().get("schedule_ids") if request.is_json else None
    try:
        schedule_ids_param = request.args.get("schedule_ids")
        schedule_ids = json.loads(schedule_ids_param) if schedule_ids_param else None
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 400, "message": "参数错误"})
    try:
        if schedule_id and not schedule_ids:
            matches = get_match_by_schedule(schedule_id)
        elif schedule_ids and not schedule_id:
            matches = get_match_by_schedules(schedule_ids)
        elif not (request.args or schedule_ids):
            matches = get_match_all()
        else:
            return jsonify({"code": 400, "message": "查询参数错误"})
        if matches is None or matches == []:
            return jsonify({"code": 404, "message": "查询的数据不存在"})
        else:
            return jsonify({"code": 200, "data": matches, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


@main_bp.route("/players")
def players():
    try:
        if request.args or request.is_json:
            return jsonify({"code": 400, "message": "查询参数错误"})
        players = get_players()
        for p in players:
            p.update(
                {
                    "photo": "https://global.bussiness.vspo.cn/acl_2025/player_photo/test.jpg"
                }
            )
        return jsonify({"code": 200, "data": players, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


@main_bp.route("/real_time_match")
def real_time_match():
    try:
        real_time_match = get_real_time_match()
        if real_time_match:
            return jsonify(
                {"code": 200, "data": real_time_match, "message": "数据获取成功"}
            )
        return jsonify({"code": 404, "message": "暂无正在进行中的比赛"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


# @main_bp.route("/real_time_players")
# def real_time_players():
#     try:
#         real_time_players = get_real_time_player()
#         if real_time_players:
#             return jsonify(
#                 {"code": 200, "data": real_time_players, "message": "数据获取成功"}
#             )
#         return jsonify({"code": 404, "message": "暂无正在进行中的比赛"})
#     except Exception as e:
#         logging.error(f"发生错误：{e}", exc_info=True)
#         return jsonify({"code": 500, "message": "数据获取失败"})


# 返回校验
def schedule_checked(schedules):
    if schedules and len(schedules) == 1:
        if schedules[0]["scheduleList"] == []:
            return False
        return True
    elif schedules and len(schedules) > 1:
        schedule_list = []
        for s in schedules:
            schedule_list.extend(s["scheduleList"])
        if schedule_list == []:
            return False
        return True
    else:
        return False


def season_checked(seasons):
    if seasons and len(seasons) == 1:
        if seasons[0] == []:
            return False
        return True
    elif seasons and len(seasons) > 1:
        if seasons == []:
            return False
        return True
    else:
        return False


def create_app():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://vspnjovi:Pubgm2021@rm-uf6f326265lft8bwrdo.mysql.rds.aliyuncs.com:3306/acl_cs_2025"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    CORS(app)
    app.register_blueprint(main_bp)
    return app


app = create_app()

if __name__ == "__main__":
    # 这是一行注释
    app.run(host="0.0.0.0", port=5555)
