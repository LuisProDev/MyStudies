def end_game():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 45:
        shift = shift % 26

    def caesar(text, shift):
        cipher_direction = direction
        end_text = ''
        if direction == 'decode':
            shift *= -1
        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                new_position = index + shift
                end_text += alphabet[new_position]
            else:
                end_text += char    
        print(f"The {cipher_direction}d text is {end_text}")

    caesar(text, shift)

    choice = input("Do you want to play again? Y/N: ").lower()
    if choice == 'y':
        end_game()
    else:
        exit()
        
end_game()