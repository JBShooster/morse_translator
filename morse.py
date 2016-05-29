def decodeMorse(morseCode):
    morseCode = morseCode.split(" ")
    print morseCode
    results = []
    morseLetters = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        ".----": 1,
        "..---": 2,
        "...--": 3,
        "....-": 4,
        ".....": 5,
        "-....": 6,
        "--...": 7,
        "---..": 8,
        "----.": 9,
        "-----": 0,
        "...---...": "SOS",
        "-.-.--": "!",
        ".-.-.-": "."
    }
    for x in morseCode:
        if len(x) > 0:
            letter = morseLetters[x]
            results.append(letter)
        elif x == "":
            results.append(" ")
    results = "".join(results)
    results = " ".join(results.split())
    return results
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
