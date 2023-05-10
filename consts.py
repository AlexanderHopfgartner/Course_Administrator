import os
from typing import TypedDict


INPUT_END = "\n>>>"
yon = "[yes/no]"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class AddressForm(TypedDict):
    address_name: str
    number: str
    postcode: int
    city: str


class Form(TypedDict):
    telnum: str
    email: str
    url: str
    f_name: str
    name: str
    role: str
    address: AddressForm


class MemberForm(TypedDict, Form):
    id: int
