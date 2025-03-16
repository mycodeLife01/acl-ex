from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
from extensions import db
from da import *
import logging

main_bp = Blueprint("main", __name__, url_prefix="/acl/api")


@main_bp.route("/seasons")
def seasons():
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")
    try:
        if start_time and not end_time:
            seasons = get_season_by_startTime(start_time)
        elif end_time and not start_time:
            seasons = get_season_by_endTime(end_time)
        elif not (start_time or end_time):
            seasons = get_season_all()
        else:
            raise Exception("season参数传递有误")

        if seasons is None or seasons == []:
            return jsonify({"code": 501, "message": "查询的数据不存在"})
        else:
            return jsonify({"code": 200, "data": seasons, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


@main_bp.route("/schedules")
def schedules():
    season_id = request.args.get("season_id")
    season_ids = request.get_json().get("season_ids") if request.is_json else None
    try:
        if season_id and not season_ids:
            schedules = get_schedule_by_season(season_id)
        elif season_ids and not season_id:
            schedules = get_schedule_by_seasons(season_ids)
        elif not (season_id or season_ids):
            schedules = get_schedule_all()
        else:
            raise Exception("team参数传递有误")

        if schedules is None or schedules == []:
            return jsonify({"code": 501, "message": "查询的数据不存在"})
        else:
            return jsonify({"code": 200, "data": schedules, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


@main_bp.route("/teams")
def teams():
    season_id = request.args.get("season_id")
    schedule_id = request.args.get("schedule_id")
    season_ids = request.get_json().get("season_ids") if request.is_json else None
    schedule_ids = request.get_json().get("schedule_ids") if request.is_json else None
    try:
        if not (season_id or schedule_id or season_ids or schedule_ids):
            teams = get_team_all()
        elif season_id and not (schedule_id or season_ids or schedule_ids):
            teams = get_team_by_season(season_id)
        elif schedule_id and not (season_id or season_ids or schedule_ids):
            teams = get_team_by_schedule(schedule_id)
        elif season_ids and not (season_id or schedule_id or schedule_ids):
            teams = get_team_by_seasons(season_ids)
        elif schedule_ids and not (season_id or schedule_id or season_ids):
            teams = get_team_by_schedules(schedule_ids)
        else:
            raise Exception("team参数传递有误")
        if teams is None or teams == []:
            return jsonify({"code": 501, "message": "查询的数据不存在"})
        else:
            return jsonify({"code": 200, "data": teams, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


@main_bp.route("/matches")
def matches():
    schedule_id = request.args.get("schedule_id")
    schedule_ids = request.get_json().get("schedule_ids") if request.is_json else None
    try:
        if schedule_id and not schedule_ids:
            matches = get_match_by_schedule(schedule_id)
        elif schedule_ids and not schedule_id:
            matches = get_match_by_schedules(schedule_ids)
        elif not schedule_id and not schedule_ids:
            matches = get_match_all()
        else:
            raise Exception("match参数传递有误")
        if matches is None or matches == []:
            return jsonify({"code": 501, "message": "查询的数据不存在"})
        else:
            return jsonify({"code": 200, "data": matches, "message": "数据获取成功"})
    except Exception as e:
        logging.error(f"发生错误：{e}", exc_info=True)
        return jsonify({"code": 500, "message": "数据获取失败"})


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
    app.run()
