def check_number(numbers):
    valid_number = ['1','2','3','4','5',
                    '6','7','8','9','0']

    for digit in numbers:
        if digit in valid_number:
            print("{} is a good number".format(numbers))
            return numbers
        else:
            check_number(input("Numbers only, Try again!!! "))

def calculate():
    print("This program adds two numbers.")

    num1 = input("Enter first whole number: ")
    check_number(num1)
    num2 = input("Enter second whole number: ")
    check_number(num2)

    total = int(num1) + int(num2)

    print("Let's do some adding!")
    print("{} + {} = {}".format(num1, num2, total))

    return input("Type 'done' to leave program.")

def main():
    run_loop = calculate()
    while run_loop != 'done':
        run_loop = calculate()

    print("Goodbye!!")
    print("Come back when you have more numbers :]")

if __name__ == "__main__":
    main()

# not bonus anymore: The program can tell if the user has entered an
# Invalid entry and prompts the user. The promt has the user keep trying
# until they enter a valid number.
#
# make bonus mandatory bc it's basically the same code as lab10 :|
