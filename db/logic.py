import json
from course_administrator.couse_administrator import Member


class DB:

    def db_log_on(self):
        with open("db/db.json", "r") as db_json:
            db_read = json.load(db_json)
            self.members += [Member(**data) for data in db_read["ids"]["members"]]
            Member.id = db_read["ids"]["last_id"]

    def db_save(self):
        member_list = []
        for member in self.members:
            member_list.append(member.member_form())
        json_dict = {"ids": {"last_id": Member.id, "members": member_list}}
        with open("db/db.json", 'w') as file_object:  # open the file in write mode
            json.dump(json_dict, file_object)  # json.dump() function to stores data in test.json file

    def __init__(self):
        self.members: list[Member] = []
