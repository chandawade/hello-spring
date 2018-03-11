def alphabet_position(letter):
    value = ord(letter)
    for i in letter:
        if value >= 65 and value <= 90:
            return value - 65 
        else:
            return value - 97
    return value 

def rotate_character(char, rot):
    if ord(char) >= 65 and ord(char) <= 90:
        return chr(65 + (alphabet_position(char) + rot) % 26)
    elif ord(char) >= 97 and ord(char) <= 122:
        return chr(97 + (alphabet_position(char) + rot) % 26)
    else:
        return char

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
