def soundex_code(char):
    char = char.upper()
    code_map = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return code_map.get(char, '0')  # Return '0' for characters not in the map

def filter_code(new_code, last_code):
    return new_code if new_code != '0' and new_code != last_code else ""

def map_characters(name, last_code):
    soundex_result = ""
    for char in name[1:]:
        new_code = soundex_code(char)
        filtered_code = filter_code(new_code, last_code)
        if filtered_code:
            soundex_result += filtered_code
            last_code = filtered_code
    return soundex_result

def compute_soundex(name):
    if not name:
        return ""
    soundex_str = name[0].upper()
    last_code = soundex_code(soundex_str)
    soundex_str += map_characters(name, last_code)
    
    # Trim to 4 characters if longer
    if len(soundex_str) > 4:
        soundex_str = soundex_str[:4]

    # Pad with zeros to ensure length is 4
    soundex_str = soundex_str.ljust(4, '0')

    return soundex_str
