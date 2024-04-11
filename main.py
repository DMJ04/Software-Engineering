# Diego Medina and Austin Derby
def encode(message):
    encoded_message = ""
    for digit in message:  # Creates loop to go through digits in the string
        encoded_digit = str((int(digit) + 3) % 10)  # Adds three to that digit then takes remainder adds encoded_message
        encoded_message += encoded_digit  # Creates the string for all the digits
    return encoded_message


def main():
    while True:  # Starts while loop
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")  # Menu options
        menu_option = input("Please enter an option: ")  # Menu selection
        if menu_option == "1":
            message = input("Please enter your password to encode: ")  # Takes user input for message to be decoded
            encoded_message = encode(message)  # Encodes the message and adds and stores it as encoded_message
            print("Your password has been encoded and stored! ")
        elif menu_option == "2":
            pass
        else:
            break


if __name__ == "__main__":
    main()
