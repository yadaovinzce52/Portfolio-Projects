from TextToMorse import TextToMorse
from MorseToText import MorseToText

# Welcome screen
print('\n********** Welcome to the morse code translator. **********\n')

# Loop that will continue until the user enters "quit" which will let the user know that
# the program is ending
while True:

    # Exception handling for invalid input regarding text to morse or morse to text
    try:
        choice = input('Enter "1" if you want to translate from text to morse or "2" if you want to translate from morse to text or "3" to quit the program: ')
        if choice not in ['1', '2', '3']:
            raise Exception('Invalid choice. Please enter "1" for text to morse or "2" for morse to text.')

    # If the user inputs anything other than "1" or "2", an error will be displayed
    except Exception as err:
        print(f'\nError: {err}\n')

    # If no error is raised, the program continues to the translator depending on the user's choice
    else:

        # START text to morse translator
        if choice == '1':
            # Instructions on how the morse code is formatted
            print('\n********** Text to morse translator **********\n')
            print('How to read morse code:')
            print("\n1. The space between letters of the same word is one space.\n2. The space between words is three spaces.\n")

            message = input('Enter your message: ').upper()

            if message == 'QUIT':
                print('Thank you for using this morse code translator. Exiting program.')
                break

            # Exception handling for invalid input regarding the text
            try:
                text_to_morse = TextToMorse(message)
                if not text_to_morse.is_valid():
                    raise Exception('Input can only contain letters, numbers, and spaces.')

            # If the user enters a message that contains invalid characters, an error will be displayed
            except Exception as err:
                print(f'\nError: {err}\n')

            # If no error is raised, the program translates the message and displays the morse code
            else:
                text_to_morse.translate_text()
                print(f'\nTranslated message: {text_to_morse.display_morse()}\n')

        # START morse to text translator
        elif choice == '2':
            # Instructions on how to input morse code for proper translation
            print('\n********** Morse to text translator **********\n')
            print('How to format morse code for proper translation:')
            print('\n1. Place a single space between letters of the same word (e.g ".... .-..").\n'
                  '2. Place a slash between words (e.g ".... .-../.-.. ---").\n3. If the morse code does not associate '
                  'with a letter/number a "~" will be displayed instead.\n')

            message = input('Enter your message: ').upper()

            # Exception handling for invalid morse code input
            try:
                morse_to_text = MorseToText(message)
                if not morse_to_text.is_valid():
                    raise Exception('Input can only contain morse code characters ("." or "-" or "/"')

            # If the user enters an invalid morse code, an error will be displayed
            except Exception as err:
                print(f'\nError: {err}\n')

            # If no error, the program translates the code into text
            else:
                morse_to_text.translate_morse()
                print(f'\nTranslated message: {morse_to_text.display_text()}\n')
        else:
            print('\nThank you for using this morse code translator. Exiting program.')
            break