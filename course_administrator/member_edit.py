from course_administrator.couse_administrator import Member
from consts import INPUT_END


def find_edit_user(db) -> Member | None:
    edit = input(f"Do you want to edit by \"ID\" or \"full_name\".[\"q!\" ot leave]{INPUT_END}").lower()[0]
    while edit == "i":
        edit_user = []
        edit_key = input(f"Please enter the \"ID\".{INPUT_END}")
        try:
            edit_user = [member for member in db.members if member.id == int(edit_key)]
        except ValueError:
            print("Sorry your input is not a Valid \"ID\".")
        if not edit_user:
            print("Sorry no user with this \"ID\".")
        elif len(edit_user) == 1:
            if input(f"Do you want to edit the user: {edit_user}. [yes/no]{INPUT_END}").lower()[0] == "y":
                edit = edit_user[0]
        else:
            [print(f"{edit_user.index(user)}: {user}") for user in edit_user]
            user = ""
            while not user:
                user = input(f"Please enter the correct index of the user{INPUT_END}")
                try:
                    edit = edit_user[int(user)]
                except ValueError:
                    print("Sorry invalit input.")
                    user = ""
                except IndexError:
                    print("Sorry index not in range.")
                    user = ""

    while edit == "f":
        edit_user = []
        edit_key = input(f"Please enter the \"full_name\".{INPUT_END}")
        edit_user = [member for member in db.members if member.full_name == edit_key]
        if not edit_user:
            print("Sorry no user with this \"full_name\".")
        elif len(edit_user) == 1:
            if input(f"Do you want to edit the user: {edit_user}. [yes/no]{INPUT_END}").lower()[0] == "y":
                edit = edit_user[0]
        else:
            [print(f"{edit_user.index(user)}: {user}") for user in edit_user]
            user = ""
            while not user:
                user = input(f"Please enter the correct index of the user{INPUT_END}")
                try:
                    edit = edit_user[int(user)]
                except ValueError:
                    print("Sorry invalit input.")
                    user = ""
                except IndexError:
                    print("Sorry index not in range.")
                    user = ""

    if type(edit) == Member:
        return edit
    if edit == "q!":
        return
    print(f"Sorry invalid input.")


def edit(member: Member):
    pass