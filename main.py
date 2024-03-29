from logic.menu import menu
from consts import INPUT_END, YON


def main():
    run = True
    while run:
        key = menu()
        if key == "q!":
            if input(f"Logged out\n\nDo you want to log on again?\t{YON}{INPUT_END}").lower()[0] == "n":
                run = False
    print("Closed")


if __name__ == "__main__":
    main()
