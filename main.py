def get_number() -> int:
    while True:
        number = input("\nEnter a number to check for in the fibonacci series: ")
        if not number.isdigit():
            print("\nPlease enter a valid number.")
        elif not int(number) > 0:
            print("\nPlease enter a number greater than zero.")
        else:
            return int(number)


def find_fibonacci(number: int) -> (bool, int):
    last_number = 0
    current_number = 1
    count = 1
    while True:
        if current_number == number:
            return True, count
        elif current_number > number:
            return False, count
        else:
            new_number = last_number + current_number
            last_number = current_number
            current_number = new_number
            count += 1


def check_again():
    while True:
        response = input("\nWould you like to check again with a different number? (y/n) ")
        if response not in ["y", "n"]:
            print("\nPlease enter a valid response.")
        elif response == "y":
            main()
        elif response == "n":
            exit()


def main():
    number = get_number()
    result = find_fibonacci(number)
    if result[0]:
        print(f"\nThe number {number} is number {result[1]} in the fibonacci series.")
    else:
        print(f"\nThe number {number} is not in the fibonacci series.")

    check_again()


if __name__ == "__main__":
    main()