# main.py

## REQUIREMENT: install cryptography.fernet

import json
with open("Data/EncryptedGroupHints Spring 2025.json", "r") as file:
    encrypted = json.load(file)

with open("Data/TeamsAndEncryptedMessagesForDistribution.json", "r") as f:
    teams = json.load(f)

encrypted_keys = list(encrypted.keys())
# print(encrypted_keys)
teams_keys = list(teams.keys())

# print(encrypted[encrypted_keys[0]])
print(encrypted_keys)
print(list(teams.keys()))
print(f'\n{teams_keys[0]}')
print(teams[teams_keys[0]])
print(len(encrypted_keys))