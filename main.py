Morse2 = {
    'A': '⚫ ⬛⬛⬛', 'B': '⬛⬛⬛ ⚫ ⚫ ⚫', 'C': '⬛⬛⬛ ⚫ ⬛⬛⬛ ⚫', 'D': '⬛⬛⬛ ⚫ ⚫', 'E': '⚫', 'F': '⚫ ⚫ ⬛⬛⬛ ⚫',
    'G': '⬛⬛⬛ ⬛⬛⬛ ⚫', 'H': '⚫ ⚫ ⚫ ⚫', 'I': '⚫ ⚫', 'J': '⚫ ⬛⬛⬛ ⬛⬛⬛ ⬛⬛⬛', 'K': '⬛⬛⬛ ⚫ ⬛⬛⬛', 'L': '⚫ ⬛⬛⬛ ⚫ ⚫',
    'M': '⬛⬛⬛ ⬛⬛⬛', 'N': '⬛⬛⬛ ⚫', 'O': '⬛⬛⬛ ⬛⬛⬛ ⬛⬛⬛', 'P': '⚫ ⬛⬛⬛ ⬛⬛⬛ ⚫', 'Q': '⬛⬛⬛ ⬛⬛⬛ ⚫ ⬛⬛⬛',
    'R': '⚫ ⬛⬛⬛ ⚫', 'S': '⚫ ⚫ ⚫', 'T': '⬛⬛⬛', 'U': '⚫ ⚫ ⬛⬛⬛', 'V': '⚫ ⚫ ⚫ ⬛⬛⬛', 'W': '⚫ ⬛⬛⬛ ⬛⬛⬛',
    'X': '⬛⬛⬛ ⚫ ⚫ ⬛⬛⬛', 'Y': '⬛⬛⬛ ⚫ ⬛⬛⬛ ⬛⬛⬛', 'Z': '⬛⬛⬛ ⬛⬛⬛ ⚫ ⚫', ' ': '/'
}

Morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}


def translator(d, msg):
    output = ""
    if d.lower() == 'encode':
        for m in msg:
            output += Morse[m]
            output += " "
        print("Note : '/' separates one word from another !")
        print(output)
    elif d.lower() == 'decode':
        msg = msg.split('  ')
        # print(msg)
        msg2 = []
        for i in range(len(msg)):
            msg2.append(msg[i].split(' '))
        # print(msg2)
        for m in msg2:
            for n in m:
                for key, value in Morse.items():
                    if value == n:
                        output += key
            output += ' '
        print(output)
    else:
        print("Invalid direction")


to_repeat = True

while to_repeat:
    direction = input("Enter what to perform? Type 'encode' for encoding or 'decode' for decoding.")
    plain_text = input("--------------------------------------------------------------------------\n"
                       "Enter text(only alphabets and numbers allowed) or \nMorse code(Use double blank spaces to "
                       "separate different words) to convert vice versa: \n").upper()
    translator(direction, plain_text)
    do_again = input("--------------------------------------------------------------------------"
                     "\nDo you want to perform again? Type 'Y' for Yes or 'N' for No: ")
    if do_again.upper() == 'N':
        to_repeat = False
