from TextToMorse import TextToMorse
from MorseToText import MorseToText

print('********** Welcome to the morse code translator. **********')
print('How to read morse code:')
print("""
    1. The space between letters of the same word is one space.
    2. The space between words is three spaces.
    """)

while True:
    try:
        choice = input('Enter "1" if you want to translate from text to morse or "2" if you want to translate from morse to text: ')
        if choice not in ['1', '2']:
            raise Exception('Invalid choice. Please enter "1" for text to morse or "2" for morse to text.')

    except Exception as err:
        print(f'Error: {err}')

    else:
        message = input('Enter your message: ').upper()

        if message == 'QUIT':
            print('Thank you for using this morse code translator. Exiting program.')
            break
        else:
            if choice == '1':
                try:
                    text_to_morse = TextToMorse(message)
                    if not text_to_morse.is_valid(message):
                        raise Exception('Input can only contain letters, numbers, and spaces.')
                except Exception as err:
                    print(f'Error: {err}')
                else:
                    message_split = message.split()
                    text_to_morse.translate_text(message_split)
                    print(f'Translated message: {text_to_morse.display_morse()}')

            else:
                morse_to_text = MorseToText()
                if not morse_to_text.is_valid(message):
                    raise Exception('Input can only contain morse code characters ("." or "-".')
