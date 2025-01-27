# <Saving this coding example (perhaps for something in the future?)>
# "So your name is {}".format(name), "and you currently go to {}".format(school)?


def main():
    print("Hello and welcome! Python is a computer programming language that lets you work swiftly and integrate systems more efficiently.")
    print("We want to know if you like programming!")
    print("Do you like programming?")
    answer = input()

    print()
    print("Great! You said {}?".format(answer))
    print("Let’s start learning some Python today. But before that, I would like for you to answer a few questions first.")

    print()
    print("What's your name?")
    name = input()

    print()
    print("What high school did you attend?")
    school = input()

    print()
    print("What college do you currently attend?")
    college = input()

    print()
    print("It's great to get to know you more! I've learned that your name is {},".format(name.capitalize()), "you attended {}".format(school.capitalize()), "for high school, and you're currently attending {}.".format(college.capitalize()))
    print("It was fun getting to know you.")
    print("Now let's get started!")


if __name__ == "__main__":
    main()
