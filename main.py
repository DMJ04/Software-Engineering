def encode(message):
    encoded_message = ""
    for digit in message:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_message += encoded_digit
    return encoded_message


def main():
    while True:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")
        menu_option = input("Please enter an option: ")
        if menu_option == "1":
            message = input("Please enter your password to encode: ")
            encoded_message = encode(message)
            print("Your password has been encoded and stored! ")
        elif menu_option == "2":
            pass
        else:
            break


if __name__ == "__main__":
    main()
