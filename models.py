from extensions import db


class Season(db.Model):
    __tablename__ = 'season'
    season_id = db.Column(db.Integer, primary_key=True)
    season_name = db.Column(db.String(255), nullable=False)
    season_start_time = db.Column(db.Integer, nullable=False)
    season_end_time = db.Column(db.Integer, nullable=False)


class Schedule(db.Model):
    __tablename__ = 'schedule'
    schedule_id = db.Column(db.String(255), primary_key=True)
    season_id = db.Column(db.Integer)
    schedule_name = db.Column(db.String(255), nullable=False)
    schedule_start_time = db.Column(db.Integer, nullable=False)
    schedule_status = db.Column(db.Integer, nullable=False)
    team_1 = db.Column(db.String(255), nullable=False)
    team_2 = db.Column(db.String(255), nullable=False)
    team_1_score = db.Column(db.Integer, nullable=False)
    team_2_score = db.Column(db.Integer, nullable=False)
    stage_id = db.Column(db.Integer, nullable=False)
    stage_name = db.Column(db.String(255), nullable=False)


class Team_Info(db.Model):
    __tablename__ = 'team_info'
    team_id = db.Column(db.String, primary_key=True)
    team_name = db.Column(db.String(255), nullable=False)
    team_logo = db.Column(db.String(255))


class Match(db.Model):
    __tablename__ = 'match'
    match_id = db.Column(db.String(255), primary_key=True)
    schedule_id = db.Column(db.String(255))
    match_start_time = db.Column(db.Integer, nullable=False)
    match_end_time = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.String(255), nullable=False)
    match_num = db.Column(db.Integer, nullable=False)
