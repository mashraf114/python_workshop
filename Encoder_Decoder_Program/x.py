alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def caesar(original_text, shift_amount,direction):
    cipher_text = ""
    for letter in original_text:

        if direction == "encode":
            print(direction, "enc")
            shifted_position = alphabet.index(letter) + shift_amount
        else:
            print(direction, "dec")

            shifted_position = alphabet.index(letter) - shift_amount

        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {direction} result: {cipher_text}")

caesar(text, shift,direction)