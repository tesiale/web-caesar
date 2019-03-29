from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    new_text = ""
    for i in range(len(text)):
        new_text = new_text + rotate_character(text[i], rot)
    return new_text

def main():
    user_msg = input("Type a message: ")
    user_rot = input("Rotate by: ")

    print(encrypt(user_msg, int(user_rot)))

if __name__ == "__main__":
    main()