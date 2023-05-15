from Member import Member
import codecs
import json
from consts import *


class DB:

    def db_log_on(self):
        with codecs.open("db_.json", "r", encoding="utf-8") as db_json:
            db_read = json.load(db_json)
            self.members += [Member(**data) for data in db_read["ids"]["members"]]
            Member.id = db_read["ids"]["last_id"]

    def db_save(self):
        member_list = []
        for member in self.members:
            member_list.append(member.member_form())
        json_dict = {"ids": {"last_id": Member.id, "members": member_list}}
        with codecs.open("db/db.json", 'w', encoding="utf-8") as file_object:  # open the file in write mode
            json.dump(json_dict, file_object,
                      ensure_ascii=False)  # json.dump() function to stores data in test.json file

    def login(self) -> Member:
        while True:
            user_name = input(f"Please Enter your username ['first_name surname']")
            current_users = [member for member in self.members if member.full_name == user_name]
            match len(current_users):
                case 0:
                    print("Sorry no user found.\n")
                    clear()
                case _:
                    for user in current_users:
                        if itis(f"login with:\nUser: {user} found.\nIDNumber is: {user.id}"):
                            return user

    def start(self):
        pass

    def get_user_to(self, keyword) -> Member | None:
        user_get = True
        while user_get:
            if user_get := itis(f"Do you want to {keyword} a user? {YON}{INPUT_END}"):
                user_by_id = []
                [print(member.id, "\t", member) for member in self.members]
                user_id = input(f"Please Enter the \"ID\".{INPUT_END}")
                if not user_id or user_id == "q" or user_id == "Q":
                    return
                users_by_id = [member for member in self.members if member.id == int(user_id)]
                if not users_by_id:
                    print("Sorry no user with this \"ID\".")
                elif len(users_by_id) == 1:
                    if itis(f"Do you want to {keyword} the user: {users_by_id}.\n{YON}{INPUT_END}"):
                        user_get = users_by_id[0]
                else:
                    [print(f"{users_by_id.index(user)}: {user}") for user in users_by_id]
                    user_get = ""
                while not user_get:
                    user_get = input(f"Please enter the correct index of the user {INPUT_END}")
                    try:
                        user_get = users_by_id[int(user_get)]
                    except ValueError:
                        print("Sorry invalit input.")
                        user_get = ""
                    except IndexError:
                        print("Sorry index not in range.")
                        user_get = ""
                if type(user_get) == Member:
                    return user_get

    def __init__(self):
        self.members: list[Member] = []
        self.use: Member = self.login()

    def __str__(self):
        return [member.full_name for member in self.members]

    def __repr__(self):
        return [member.full_name for member in self.members]
