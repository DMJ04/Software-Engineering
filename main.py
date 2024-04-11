# Diego Medina and Austin Derby
def encode(message):
    encoded_message = ""
    for digit in message:  # Creates loop to go through digits in the string
        encoded_digit = str((int(digit) + 3) % 10)  # Adds three to that digit then takes remainder adds encoded_message
        encoded_message += encoded_digit  # Creates the string for all the digits
    return encoded_message

def decoder(new_password):
    password = ""

    for i in range(len(new_password)):
        if "6" <= new_password[i] <= "9":
            if new_password[i] == "6":
                password += "3"

            elif new_password[i] == "7":
                password += "4"

            elif new_password[i] == "8":
                password += "5"

            elif new_password == "9":
                password += "6"

        elif "0" <= new_password[i] <= "6":
            if new_password[i] == "0":
                password += "7"

            elif new_password[i] == "1":
                password += "8"

            elif new_password[i] == "2":
                password += "9"

            elif new_password[i] == "3":
                password += "0"

            elif new_password[i] == "4":
                password += "1"

            elif new_password[i] == "5":
                password += "2"

            elif new_password[i] == "6":
                password += "3"
    return password


def main():
    while True:  # Starts while loop
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")  # Menu options
        menu_option = input("\nPlease enter an option: ")  # Menu selection
        if menu_option == "1":
            message = input("Please enter your password to encode: ")  # Takes user input for message to be decoded
            encoded_message = encode(message)  # Encodes the message and adds and stores it as encoded_message
            print("Your password has been encoded and stored! ")
            print()
        elif menu_option == "2":
            decoded_message = decoder(encoded_message)
            print(f"The encoded password is {encoded_message}, and the original password is {decoded_message}")
            print()

        else:
            break


if __name__ == "__main__":
    main()
