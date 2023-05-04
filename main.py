from couse_administrator import course_administrator


def main():
    run = True
    while run:
        key = course_administrator()
        if key == "q!":
            run = False


if __name__ == "__main__":
    main()