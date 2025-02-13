def main():
    print("This program adds two numbers.")

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    total = int(num1) + int(num2)

    print("{} + {} = {}".format(num1, num2, total))

    return input("Type 'exit' to leave program.")

def loop():
    run_loop = main()
    while run_loop != 'exit':
        run_loop = main()

if __name__ == "__main__":
    main()
    loop()
