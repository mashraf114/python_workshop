alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text,shift_amount):
    encoded_letter = ""
    for letter in original_text:
        if alphabet.index(letter) + shift_amount >= 25:
            new_position= (alphabet.index(letter)-25) + shift_amount
            encoded_letter += alphabet[new_position]

        else:
            new_position= (alphabet.index(letter)+shift_amount)
            encoded_letter += alphabet[new_position]
    print(encoded_letter)

encrypt(text,shift)

