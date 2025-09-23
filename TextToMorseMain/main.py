from TextToMorse import TextToMorse
from MorseToText import MorseToText

# Welcome screen
print('********** Welcome to the morse code translator. **********')

# Loop that will continue until the user enters "quit" which will let the user know that
# the program is ending
while True:

    # Exception handling for invalid input regarding text to morse or morse to text
    try:
        choice = input('Enter "1" if you want to translate from text to morse or "2" if you want to translate from morse to text: ')
        if choice not in ['1', '2']:
            raise Exception('Invalid choice. Please enter "1" for text to morse or "2" for morse to text.')

    # If the user inputs anything other than "1" or "2", an error will be displayed
    except Exception as err:
        print(f'Error: {err}')

    # If no error is raised, the program continues to the translator depending on the user's choice
    else:
        message = input('Enter your message: ').upper()

        if message == 'QUIT':
            print('Thank you for using this morse code translator. Exiting program.')
            break
        else:

            # START text to morse translator
            if choice == '1':
                # Instructions on how the morse code is formatted
                print('********** Text to morse translator **********')
                print('How to read morse code:')
                print("""
                    1. The space between letters of the same word is one space.
                    2. The space between words is three spaces.
                    """)

                # Exception handling for invalid input regarding the text
                try:
                    text_to_morse = TextToMorse(message)
                    if not text_to_morse.is_valid(message):
                        raise Exception('Input can only contain letters, numbers, and spaces.')

                # If the user enters a message that contains invalid characters, an error will be displayed
                except Exception as err:
                    print(f'Error: {err}')

                # If no error is raised, the program translates the message and displays the morse code
                else:
                    message_split = message.split()
                    text_to_morse.translate_text(message_split)
                    print(f'Translated message: {text_to_morse.display_morse()}')

            # START morse to text translator
            else:
                # Instructions on how to input morse code for proper translation
                print('********** Morse to text translator **********')
                print('How to format morse code for proper translation:')
                print("""
                    1. Place a single space between letters of the same word (e.g ".... .-..").
                    2. Place a slash between words (e.g ".... .-../.-.. ---").
                    """)
                try:
                    morse_to_text = MorseToText()
                    if not morse_to_text.is_valid(message):
                        raise Exception('Input can only contain morse code characters ("." or "-".')
