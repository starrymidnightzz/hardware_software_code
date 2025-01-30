def main():
    print("Welcome to my conversation program")
    print("I will keep asking questions until you type 'exit'.")

    print("What is your name?")
    name = input()

    print("What's your favorite color, {}?".format(name))
    color = input()

    print("Do you like video games, {}?".format(name))
    answer = input()

    if input() != 'exit':
        print("Thanks for chatting with me, {}".format(name))
        print("You answered questions.")

if __name__ == "__main__":
    main()
 
