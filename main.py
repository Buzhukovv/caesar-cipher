import alphabet
def caesar(double_alpha, original, enc_or_dec):
    final_ans = ''
    for letter in original:
        if letter in double_alpha:
            if enc_or_dec == 'encode':
                index = double_alpha.index(letter) + shift
            elif enc_or_dec == 'decode':
                index = double_alpha.index(letter) - shift
            final_ans = final_ans + double_alpha[index]
        else:
            final_ans = final_ans + letter
    return final_ans

from art import logo
print(logo)
doubled = alphabet.alphabet * 2

working_game = True

while working_game == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    output = caesar(doubled, text, direction)
    print( f"The encoded text is {output}")
    work_or_not = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if work_or_not == 'yes':
        working_game = True
    elif work_or_not == 'no':
        working_game = False

