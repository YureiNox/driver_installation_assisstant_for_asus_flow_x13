import os
import json

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
PURPLE = "\033[35m"
RESET = "\033[0m"

def jsonChecker(key):
    file = "json/main.json"
    
    with open(file, 'r') as f:
        data = json.load(f)
    
    if key in data:
        return data[key]
    else:
        return f"Erreur: La clé '{key}' n'existe pas dans le fichier JSON."

def getAllKeys():
    file = "json/main.json"
    with open(file, 'r') as f:
        data = json.load(f)
        return data
