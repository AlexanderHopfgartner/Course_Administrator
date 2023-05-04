# TODO 3. create all validation checks
def validate_name(name: str) -> tuple[bool, str]:
    """if name
       Return tuple[boolean=True and name=string]

       if name invalid print an error message and

       Return tuple[boolean=False, name=string]
    """
    for name in name.split():
        if name.isalpha():
            print("The name is valid")
            return True, name
    print("The name entered is not correct\nOnly letters and spaces are allowed\n")
    return False, name
def validate_addressname(address_name: str) -> tuple[bool, str]:
    """Return tuple with boolean and error message as a string"""
    if type(address_name) == str:
        return True, "The address name is valid"
    return False, "The address name is not valid\nOnly letters and spaces are allowed"
def validate_streetnumber(street_number: str) -> tuple[bool, str]:
    """Return tuple with boolean and error message as a string"""
    new_list = []
    numbers = street_number.split('/')
    print(numbers[0][0], type(int(numbers[0][0])))
    print(numbers[0][-1], type(int(numbers[0][-1])))

    if type(int(numbers[0][0])) == int and type(int(numbers[0][-1])) == int:

        print("Bin im IF drinnen","")
        #new_list.append(int(num))
        #print(new_list)
        #print("Please enter your streetnumber in this format:\n123-124/12/1")
    print(numbers)

def validate_postcode(postcode: int) -> tuple[bool, int]:
    """Return tuple with boolean and error message as a string"""
    print("not finished")

def validate_city(city: str) -> tuple[bool, str]:
    """Return tuple with boolean and error message as a string"""
    print("not finished")

def validate_TelNr(TelNr: str) -> tuple[bool, str]:
    """Return tuple with boolean and error message as a string"""
    print("not finsihed")

def validate_email(email: str) -> tuple[bool, str]:
    """Return tuple with boolean and error message as a string"""
    print("not finished")

#validate_streetnumber("33-37/12/17")
validate_name("Melcher Christoph")
validate_name("Melche***")
validate_name("Mel1234")

