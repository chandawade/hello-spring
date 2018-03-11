from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    new_text = ' '
    updated_key =[]
    no_alpha = 0

    for i in key:
        letter = alphabet_position(i)
        updated_key.append(letter)

    for index in range(len(text)):
        if text[index].isalpha():
            x = (index - no_alpha) % len(updated_key)
            new_char = rotate_character(text[index], updated_key[x])
            new_text = new_text + new_char
        else:
            no_alpha = no_alpha + 1
            new_text = new_text + text[index]
    return new_text

def main():
    text = input("Enter your encrypted message")
    key = input("Enter the keyword your encryption will be set to")
    print(encrypt(text,key))

if __name__ == "__main__":
    main()