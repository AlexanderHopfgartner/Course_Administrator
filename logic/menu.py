from consts import INPUT_END
from db.logic import *

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
    db = db_log_on()
    main_loop = True
    while main_loop:
        print("hello")
        print(dir())
