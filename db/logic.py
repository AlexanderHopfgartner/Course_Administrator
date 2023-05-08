import json
from course_administrator.couse_administrator import Member


class DB:

    def db_log_on(self):
        with open("db/db.json", "r") as db_json:
            db_read = json.load(db_json)
            [print(member) for member in db_read["ids"]["members"]]
            self.members += [Member(**data) for data in db_read["ids"]["members"]]
        # TODO 3.1 by log to the local db set Member.id = db_read.ids.last_id
        # and update the Member.id = db_read.ids.last_id


    def db_save(self):
        # TODO 3.2 save all members to a json
        pass

    last_id = 0

    def __init__(self):
        self.members: list[Member] = []