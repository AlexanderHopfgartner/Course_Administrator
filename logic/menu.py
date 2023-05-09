from consts import INPUT_END
from db.logic import DB
from course_administrator.couse_administrator import course_administration, Member, clear

"""Module = main menu => sub menus: check Users,
                                    add User, -> validate
                                    edit User,
"""
db = {
    """ids:
        last_id: X
        id: Member for member.id, member in db["ids"][id].items()"""
}


def menu():
    # TODO 3. log db to the local db
    db = DB()
    db.db_log_on()
    main_loop = True
    while main_loop:
        user = None
        while type(user) != Member:
            user_name = input(f"Please enter your username ['first_name name']{INPUT_END}")
            for member in db.members:
                if member.full_name == user_name:
                    if input(f"{member}\nIDNumber is: {member.id}\tis this you? [yes/no]{INPUT_END}").lower()[0] == "y":
                        user = member
                        clear()
                        print(f"{member.first_name} is logged on")
            if type(user) != Member:
                print("User not found!\n\n")

        key = course_administration(db, user)
        if key == "q!":
            return key

