
from .en import greet as en_greet
from .tn import greet as tn_greet

def greet(lang):
    if lang == "en":
       en_greet() 
    elif lang == "tn":
        tn_greet()
    else:
        print("Language not supported")