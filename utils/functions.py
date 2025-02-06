import json

from utils.flags import get_card_flags_json


def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0


def load_prefixes():
    with open("./json/card_flags.json", "r", encoding="utf-8") as file:
        card_flags = json.load(file)

    prefixes = set()
    for flag in card_flags.values():
        for prefix in flag["prefixos"]:
            prefixes.add(str(prefix))
    return prefixes


def get_card_flag(card_number):
    with open("./json/card_flags.json", "r", encoding="utf-8") as file:
        card_flags = json.load(file)

    card_number = card_number.replace(" ", "")
    if not luhn_check(card_number):
        return False

    prefixes = load_prefixes()
    for i in range(4, 0, -1):
        if card_number[:i] in prefixes:
            for flag, details in card_flags.items():
                if card_number[:i] in map(str, details["prefixos"]):
                    if len(card_number) in details["comprimento"]:
                        return flag
    return -1
    


if __name__ == "__main__":
    get_card_flags_json()
