from enum import member

from course_administrator.couse_administrator import Member
from course_administrator.member_form import get_role
from consts import INPUT_END, yon
from logic.validator import *


def find_user(db, keyword) -> Member | None:
    edit = ""
    while not edit == "n":
        edit = input(f"Do you want to {keyword} a user? {yon}{INPUT_END}").lower()[0]
        while edit == "y":
            edit_user = []
            [print(member.id, ":\t", member) for member in db.members]
            edit_key = input(f"Please enter the \"ID\".{INPUT_END}")
            if edit_key == "q" or edit_key == "Q":
                break
            try:
                edit_user = [member for member in db.members if member.id == int(edit_key)]
            except ValueError:
                print("Sorry your input is not a Valid \"ID\".")
            if not edit_user:
                print("Sorry no user with this \"ID\".")
            elif len(edit_user) == 1:
                if input(f"Do you want to edit the user: {edit_user}.\n{yon}{INPUT_END}").lower()[0] == "y":
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

        # while edit == "f":
        #     edit_user = []
        #     [print(member.id, ":\t", member) for member in db.members]
        #     edit_key = input(f"Please enter the \"full_name\".{INPUT_END}")
        #     edit_user = [member for member in db.members if member.full_name == edit_key]
        #     if not edit_user:
        #         print("Sorry no user with this \"full_name\".")
        #     elif len(edit_user) == 1:
        #         if input(f"Do you want to edit the user: {edit_user}. yon{INPUT_END}").lower()[0] == "y":
        #             edit = edit_user[0]
        #     else:
        #         [print(f"{edit_user.index(user)}: {user}") for user in edit_user]
        #         user = ""
        #         while not user:
        #             user = input(f"Please enter the correct index of the user{INPUT_END}")
        #             try:
        #                 edit = edit_user[int(user)]
        #             except ValueError:
        #                 print("Sorry invalit input.")
        #                 user = ""
        #             except IndexError:
        #                 print("Sorry index not in range.")
        #                 user = ""

        if type(edit) == Member:
            return edit
        print(f"No user selected to {keyword}")
        return


def edit(member: Member):
    editing = True
    while editing:
        print(member, "Trueee?")
        edit_key = input(f"Please Enter what to change.\n"
                         f"[first_name/name/role/address/telnum/email/url/q]{INPUT_END}").lower()[0]
        if edit_key == "f":
            edit_input = input(f"Change \"{member.first_name}\" to:{INPUT_END}")
            if validate_name(edit_input):
                member.first_name = edit_input
        if edit_key == "n":
            edit_input = input(f"Change \"{member.name}\" to:{INPUT_END}")
            if validate_name(edit_input):
                member.name = edit_input
        if edit_key == "r":
            edit_input = get_role()
            if edit_input:
                member.role = edit_input
        while edit_key == "a":
            edit_key = input(f"{member.display_address()} Please Enter what to change.\n"
                             f"[address_name/street_nummber/postcode/city/q!]{INPUT_END}")
            if edit_key.lower()[0] == "a":
                edit_input = input(f"Change \"{member.address_name}\" to:{INPUT_END}")
                if validate_address_name(edit_input):
                    member.address_name = edit_input
            if edit_key.lower()[0] == "s":
                edit_input = input(f"Change \"{member.street_number}\" to:{INPUT_END}")
                if validate_street_number(edit_input):
                    member.street_number = edit_input
            if edit_key.lower()[0] == "p":
                edit_input = input(f"Change \"{member.postcode}\" to:{INPUT_END}")
                if validate_postcode(edit_input):
                    member.postcode = int(edit_input)
            if edit_key.lower()[0] == "c":
                edit_input = input(f"Change \"{member.city}\" to:{INPUT_END}")
                if validate_city(edit_input):
                    member.city = edit_input
        if edit_key == "t":
            edit_input = input(f"Change \"{member.telnum if member.telnum else 'TelephoneNumber'}\" to:{INPUT_END}")
            if validate_telnum(edit_input):
                member.telnum = edit_input
        if edit_key == "u":
            edit_input = input(f"Change \"{member.url if member.url else 'Url'}\" to{INPUT_END}")
            if validate_url(edit_input):
                member.url = edit_input
        if edit_key == "e":
            edit_input = input(f"Change \"{member.email if member.email else 'Email'}\" to : {INPUT_END}")
            if validate_email(edit_input):
                member.email = edit_input
        member.restructure()
        if edit_key == "q":
            editing = False




