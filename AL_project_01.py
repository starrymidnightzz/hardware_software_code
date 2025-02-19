# <Saving this coding example (perhaps for something in the future?)>
# "So your name is {}".format(name), "and you currently go to {}".format(school)?


def main():
    print("Hello, I would like to get to know a little about you.\n Please answer a few brief questions.")

    print("What's your name?")
    name = input()

    print("What college do you currently attend?")
    college = input()

    print("What high school did you attend?")
    school = input()

    print("It's great to get to know you more! I've learned that your name is {},".format(name.capitalize()), "you attended {}".format(school.capitalize()), "for high school, and you're currently attending {}.".format(college.capitalize()))
    print("It was fun getting to know a little about you.")
    print("Let's do this again!")

    print()
    input("Press enter to close command prompt.")


if __name__ == "__main__":
    main()
