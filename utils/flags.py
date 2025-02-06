import json
from db.database import fetch_card_flags_from_db

def parse_prefixes(prefixes):
    parsed_prefixes = []
    for prefix in prefixes:
        if '-' in prefix:
            start, end = map(int, prefix.split('-'))
            parsed_prefixes.extend(range(start, end + 1))
        else:
            parsed_prefixes.append(int(prefix))
    return parsed_prefixes

def parse_lengths(lengths):
    parsed_lengths = []
    for length in lengths:
        if '-' in length:
            start, end = map(int, length.split('-'))
            parsed_lengths.extend(range(start, end + 1))
        elif ',' in length:
            parsed_lengths.extend(map(int, length.split(',')))
        else:
            parsed_lengths.append(int(length))
    return parsed_lengths

def get_card_flags_json():
    card_flags = fetch_card_flags_from_db()
    card_flags_dict = {}

    for bandeira, details in card_flags.items():
        prefixos = details["prefixes"].split(", ")
        comprimentos = details["lengths"].split(", ")
        card_flags_dict[bandeira] = {
            "prefixos": parse_prefixes(prefixos),
            "comprimento": parse_lengths(comprimentos)
        }
    
    # transforme o dicionário em um json
    # sobreescriva o arquivo card_flags.json a cada chamada da função
    with open("./json/card_flags.json", "w+", encoding="utf-8") as file:
        json.dump(card_flags_dict, file, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    get_card_flags_json()