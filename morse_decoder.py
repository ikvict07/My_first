def morse_decoder(code):
    """Буквы разделены одним пробелом, слова - тремя пробелами"""
    MORSE = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
    }
    coded_words = code.split('   ')
    coded_letters = [i.split() for i in coded_words]
    ans= [[] for _ in range(len(coded_words))]
    for n,j in enumerate(coded_letters):
        ans[n] = [MORSE[i] for i in j]
    new_ans = []
    for i in ans:
        new_ans.append(''.join(i))


    return ' '.join(new_ans).capitalize()
