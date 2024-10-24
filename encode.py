#aahan shin

def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10 
        encoded_password += str(new_digit)
    return encoded_password

def decode(encoded_password):
    original_password = ""
    for digit in encoded_password:
        new_digit = (int(digit) - 3) % 10 
        original_password += str(new_digit)
    return original_password

def main():
    encoded_password = ""  
    while True:
        print("\nMenu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():  
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("error")
        
        elif option == "2":
            if encoded_password: 
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("error")
        
        elif option == "3":
            break  

        else:
            print("error")

if __name__ == "__main__":
    main()
