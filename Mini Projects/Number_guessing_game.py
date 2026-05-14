import random

dictionary = {
    "easy": (1, 50, 10),
    "hard": (1, 100, 5)
}

def calculate_score(attempts_used, max_attempts):
    # we have max attempts
    score_negetive_ratio = 100/max_attempts # reduce linearly

    if (attempts_used > max_attempts): return 0
    else: return (100 - (attempts_used) * score_negetive_ratio)
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
    bool = False
    while(bool == False):
        level = input("Enter 'easy' or 'hard' : ").lower().strip()

        if(level == "easy"): 
            bool = True
            return dictionary["easy"]
        
        if(level == "hard"):
            bool = True
            return dictionary["hard"]
        
        else: print("Wrong input, try again:- ")
        # bool remains false;
    pass

def get_guess(attempt, max_attempts, low, high):
    bool = False
    while(bool == False):
        print("Enter your", attempt, "/", max_attempts, "attempt: ")
        num = input()

        if(num.isnumeric()):
            if(int(num) <= high and int(num) >= low):
                bool = True
                return int(num)
            else: 
                print("Number out of bounds")
        else: 
            print("Enter only integer numbers")
            
        attempt += 1
    pass    

def play_round(low, high, max_attempts):
    number = random.randint(low, high)
    # using the random module

    attempt = 0

    bool = False
    while(bool == False and attempt < max_attempts):
        myguess = get_guess(attempt + 1, max_attempts, low, high)
        if(myguess == number):
            print("You won!")
            print("Your score is: ", calculate_score(attempt, max_attempts))
            bool = True
            return calculate_score(attempt, max_attempts)
        else: 
            attempt += 1
            print(get_hint(myguess, number, high))

    if(attempt > max_attempts): 
        print("You Lost! Answer was: ", number)
    pass

def main():
    print("---------- Welcome to the number guessing game ----------")
    high_score = 0 # currunt high score which is zero, we will update it soon

    bool = False
    while(bool == False):
        mode = get_difficulty() # enter the difficulty
        num = play_round(*mode)

        if(num > high_score): high_score = num
        print("high score in this sessions: ", high_score)

        play = input("enter y/n or exit whether you want to play the game again? ").lower().strip();
        if(play == "y"): bool = False
        elif(play == "n"): bool = True
        elif(play == "exit"): bool = True

        else: print("Wrong input, try again:- ")

if __name__ == "__main__":
    main()