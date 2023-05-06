from consts import INPUT_END
from db.logic import DB
from course_administrator.couse_administrator import course_administration

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
        course_administration(db)

