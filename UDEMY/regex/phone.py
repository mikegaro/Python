import re


def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


print(extract_phone("mi numero es 555 100-2772"))
print(extract_phone("mi numero es 432 432897622"))
