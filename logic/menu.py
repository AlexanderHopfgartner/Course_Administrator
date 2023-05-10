from consts import INPUT_END
from db.logic import DB
from course_administrator.couse_administrator import course_administration, Member, clear


def menu():
    db = DB()
    db.db_log_on()
    main_loop = True
    while main_loop:
        user = None
        while type(user) != Member:
            user_name = input(f"Please enter your username ['first_name name']{INPUT_END}")
            for member in db.members:
                if member.full_name == user_name:
                    if input(f"\n{member}\n\nIDNumber is: {member.id}\tare you {member.full_name}? [yes?]{INPUT_END}").lower()[0] == "y":
                        user = member
                        clear()
                        print(f"{member.first_name} is logged on")
                        break
            if type(user) != Member:
                print("User not found!\n\n")

        key = course_administration(db, user)
        if key == "q!":
            return key

