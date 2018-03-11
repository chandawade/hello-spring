from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        letter = rotate_character(char, rot)
        encrypted = encrypted + letter

    return encrypted
      
def main():
    text = input("Enter a message")
    rot = int(input("enter a number"))
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()
