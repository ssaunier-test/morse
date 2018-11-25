class Morse:
    ALPHABET = {
        '.-':   'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':  'D',
        '.':    'E',
        '..-.': 'F',
        '--.':  'G',
        '....': 'H',
        '..':   'I',
        '.---': 'J',
        '-.-':  'K',
        '.-..': 'L',
        '--':   'M',
        '-.':   'N',
        '---':  'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.':  'R',
        '...':  'S',
        '-':    'T',
        '..-':  'U',
        '...-': 'V',
        '.--':  'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    def decode(self, input):
        if input == "":
            return ""

        symbols = input.split(" ")
        letters = [ self.ALPHABET[s] for s in symbols ]
        return ''.join(letters)

        # words = input.split(" / ")
        # decoded_words = []
        # for word in words:
        #     symbols = word.split(" ")
        #     letters = [ self.ALPHABET[s] for s in symbols ]
        #     decoded_words.append(''.join(letters))

        # return ' '.join(decoded_words)
