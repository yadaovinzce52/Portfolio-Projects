class TextToMorse:
    def __init__(self, message):
        # Dictionary to translate characters to morse code
        self.message = message
        self.translated_text = []
        self.char_morse = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
        }

    # Check if the message contains only alphanumeric characters and spaces
    def is_valid(self):
        return all(char.isalnum() or char.isspace() for char in self.message)

    # Translates text into morse code
    def translate_text(self):
        message = self.message.split()
        for ind, word in enumerate(message):
            for wrd_ind, char in enumerate(word):
                self.translated_text.append(self.char_morse[char])
                if wrd_ind != len(word) - 1:
                    self.translated_text.append(' ')
            if ind != len(message) - 1:
                self.translated_text.append('   ')


    # Displays the translated text in morse code
    def display_morse(self):
        return ''.join(self.translated_text)
