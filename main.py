from logic.menu import menu


def main():
    run = True
    while run:
        key = menu()
        if key == "q!":
            run = False


if __name__ == "__main__":
    main()
