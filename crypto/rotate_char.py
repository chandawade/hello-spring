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

def main():
    print(rotate_character('k', 4))
    print(rotate_character('C', 4))
    
if __name__ == "__main__":
    main()
