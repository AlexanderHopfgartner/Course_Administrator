import json
from course_administrator.couse_administrator import Member

class DB:

    last_id = 0

    def __init__(self):
        self.members: list[Member] = []

    def db_log_on(self):
        with open("db/db.json", "r") as db_json:
            db_read = json.load(db_json)
            [print(member) for member in db_read["ids"]["members"]]
            self.members += [Member(**data) for data in db_read["ids"]["members"]]
        # TODO 3.1 by log to the local db set Member.id = last id
        # TODO 3.1.1 return db read IF db
        pass


    def db_log_out(self):
        # TODO 3.2 save all members to a json
        pass

    def db_add(self):
        # TODO 3.3 add Member to members
        pass
