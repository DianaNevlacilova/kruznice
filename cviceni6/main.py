# def analyze_password(password, min_lenght=8, require_digit=True, require_upper=True, require_symbol=False, banned_words=None):
#     if banned_words is None:
#         banned_words = ['heslo', 'password', '1234']
#         missing = []
#         total_rules = 1
#         if len(password) < min_lenght:
#             missing.append("min_lenght")
#         if require_digit:
#             total_rules += 1
#             if not any(char.isdigit() for char in password):
#                 missing.append("digit")
#         if require_upper :
#             total_rules += 1
#             if not any(char.isupper() for char in password):
#                 missing.append("upper")
#         if require_symbol:
#             total_rules += 1
#             symbols = "!@#$%^&*()-_=+[]{};:,.?"
#             if not any(char in symbols for char in password):
#                 missing.append("symbol")
#
#         total_rules += 1
#         if any(word in password.lower() for word in banned_words):
#             missing.append("banned_word")
#
#         is_strong = len(missing) == 0
#         score = int(((total_rules - len(missing)) / total_rules) * 100)
#         return is_strong, score, missing
#
# print(analyze_password("Kyticka789", 8, True, True, False))

# import matplotlib.pyplot as plt
#
# path = 'ekg_signal.txt'
#
# with open(path, "r") as file:
#     lines = file.readlines()
#
# print(lines)
# rows = [float(line.strip()) for line in lines]
# print(rows)

import matplotlib.pyplot as plt


