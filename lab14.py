def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1 # determine greatest power
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1 # decrease by 1
    return result # if in 'for' command, returns result as 'None'

def binary():
    num = input ("Enter Binary Number: ")
    binary_num = binary_to_decimal(num)
    print("Binary {} to Decimal: {}". format(num, binary_num))

    return input("Type 'exit' to leave program.")

def main():
    run_loop = binary()
    while run_loop != 'exit':
        run_loop = binary()

if __name__ == "__main__":
    main()
