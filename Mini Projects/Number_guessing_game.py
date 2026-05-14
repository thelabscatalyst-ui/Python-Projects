import random

dictionary = {
    "easy": (1, 50, 10),
    "hard": (1, 100, 5)
}

def calculate_score(attempts_used, max_attempts):
    # we have max attempts
    score_negetive_ratio = 100/max_attempts # reduce linearly

    if (attempts_used > max_attempts): return 0
    else: return (100 - (attempts_used - 1) * score_negetive_ratio)
    pass

def get_hint(guess, secret, max_range):
    #secret is the number that we are guessing
    difference = guess - secret

    if(guess > max_range):
        return "Out of bounds"

    if (difference) >= 0:
        if(difference <= 5): return "High, but very close"
        if(difference > 5 and difference <= 15): return "High, but little warmer"
        else: return "Too High"
    
    else: 
        if(abs(difference) <= 5): return "Low, but very close"
        if(abs(difference) > 5 and abs(difference) <= 15): return "Low, but little warmer"
        else: return "Too Low"
    pass

def get_difficulty():
    level = input("Enter 'easy' or 'hard' according to what level do you want to play:- ")
    
    if(input == "easy"): return dictionary.fromkeys(easy)
    
    pass



