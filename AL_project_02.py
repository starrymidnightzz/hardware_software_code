def conversation():
    print("Welcome to my conversation program")
    print("I will keep asking questions until you type 'exit'.")

def questions():
    name = input("What is your name?")
    color = input("What's your favorite color, {}?".format(name))
    answer = input("Do you like video games, {}?".format(name))
    show = input("What's your favorite TV show, {}?".format(name))
    sport = input("What's your favorite sport, {}?".format(name))
    food = input("What's your favorite food, {}?".format(name))
    preference = input("Do you prefer coffee or tea, {}?".format(name))

    return input("Type exit to leave program."), name

def main():
    count = 0
    run_loop, name = questions()

    while run_loop != 'exit':
        run_loop, name = questions()

    print("Thanks for chatting with me, {}".format(name))
    print("You answered", str(count), "questions.")
    print()

    input("Press enter to close command prompt.")

if __name__ == "__main__":
    main()
