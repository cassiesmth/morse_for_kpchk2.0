def encode_morse_en(morse_code):
    morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',   
        'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3':'...--',
        '4': '....-', '5': '.....', '6':'-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--',
        '?': '..--..', '/': '-..-.', ':': '---...', ';': '-.-.-.',
        '+': '.-.-.', '-': '-....-'}
    words = morse_code.lower()
    words = words.strip().split(' ')
    encoded_words = []
    try:
        for word in words:
            letters = list(word)
            encoded_letters = [morze.get(i, '') for i in letters]
            encoded_words.append(' '.join(encoded_letters))
        return '   '.join(encoded_words)
    except Exception:
        return "you okay bro?"


def decode_morse_en(morse_code):
    morze = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd',
        '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
        '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
        '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
        '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6',
        '--...': '7', '---..': '8', '----.': '9',
        '-----': '0', '.-.-.-': '.', '--..--': ',',
        '..--..': '?', '-..-.': '/', '---...': ':',
        '-.-.-.': ';', '.-.-.': '+', '-....-': '-'}

    words = morse_code.strip().split('   ')
    decoded_words = []
    try:
        for word in words:
            letters = word.split()
            decoded_letters = [morze.get(i, '') for i in letters]
            decoded_words.append(''.join(decoded_letters))
        return ' '.join(decoded_words)
    except Exception:
        return "you okay bro?"


def encode_morse_rus(morse_code):
    morze = {'а': '.-',    'б': '-...',  'в': '.--',   'г': '--.',
             'д': '-..',   'е': '.',     'ж': '...-',  'з': '--..',
             'и': '..',    'й': '.---',  'к': '-.-',   'л': '.-..',
             'м': '--',    'н': '-.',    'о': '---',   'п': '.--.',
             'р': '.-.',   'с': '...',   'т': '-',     'у': '..-',
             'ф': '..-.',  'х': '....',  'ц': '-.-.',  'ч': '---.',
             'ш': '----',  'щ': '--.-',  'ъ': '--.--', 'ы': '-.--',
             'ь': '-..-',  'э': '..-..', 'ю': '..--',  'я': '.-.-',
             '1': '.----', '2': '..---', '3':'...--',
             '4': '....-', '5': '.....', '6':'-....', '7': '--...', '8': '---..',
             '9': '----.', '0': '-----', '.': '......', ',': '.-.-.-', ';': '-.-.-.',
             ':':'---...', '?': '..--..', '!': '--..--', '-': '-....-'}
    words = morse_code.lower()
    words = words.strip().split(' ')
    encoded_words = []
    try:
        for word in words:
            letters = list(word)
            encoded_letters = [morze.get(i, '') for i in letters]
            encoded_words.append(' '.join(encoded_letters))
        return '   '.join(encoded_words)
    except Exception:
        return "все норм?"


def decode_morse_rus(morse_code):
    morze = morse_reverse = {'.-': 'а', '-...': 'б', '.--': 'в', '--.': 'г',
                             '-..': 'д', '.': 'е', '...-': 'ж', '--..': 'з',
                             '..': 'и', '.---': 'й', '-.-': 'к', '.-..': 'л',
                             '--': 'м', '-.': 'н', '---': 'о', '.--.': 'п',
                             '.-.': 'р', '...': 'с', '-': 'т', '..-': 'у',
                             '..-.': 'ф', '....': 'х', '-.-.': 'ц', '---.': 'ч',
                             '----': 'ш', '--.-': 'щ', '--.--': 'ъ', '-.--': 'ы',
                             '-..-': 'ь', '..-..': 'э', '..--': 'ю', '.-.-': 'я',
                             '.----': '1', '..---': '2', '...--': '3',
                             '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
                             '----.': '9', '-----': '0', '......': '.', '.-.-.-': ',', '-.-.-.': ';',
                             '---...': ':', '..--..': '?', '--..--': '!', '-....-': '-'}

    words = morse_code.strip().split('   ')
    decoded_words = []
    try:
        for word in words:
            letters = word.split()
            decoded_letters = [morze.get(i, '') for i in letters]
            decoded_words.append(''.join(decoded_letters))
        return ' '.join(decoded_words)
    except Exception:
        return "все норм?"
