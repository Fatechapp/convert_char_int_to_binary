def main():
    main_menu()

def num_to_binary(num):
    return format(num, 'b')

def char_to_binary(char):
    return format(ord(char), '08b')

def main_menu():
    while True:
        print("----- Convert Into Binary -----")
        value = input("Input: ")
        print(convert_to_binary(value))

def convert_to_binary(value):
    # If the input is a digit, convert to int and then to binary
    if value.isdigit():
        return num_to_binary(int(value))
    # If the input is a single character, convert to binary
    elif isinstance(value, str) and len(value) == 1:
        return char_to_binary(value)
    else:
        return "Invalid input"

if __name__ == "__main__":
    main()
