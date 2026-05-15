import random
import datetime

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
    binary_data = max_range # we are taking as a binary data 

    mid = binary_data // 2 # we are taking the mid of the binary data

    if(guess > max_range):
        return "Out of bounds"

    if (difference) >= 0:
        if(difference <= 5): return "High, but very close"
        if(difference > 5 and difference <= 15): return "High, but little warmer"
        else: return "Too High"
    
    else: 
        if(abs(difference) <= 5): return "Low, but very close"
        if(abs(difference) > 5 and abs(difference) <= 15): return "Low, but little warmer"
        else: return "Too Low, Try " + str(mid) # this takes over the binary search logic 

    # curruntly the binary logic, is only valid for if the diffrence is higher than 15
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
            print(get_hint(myguess, number, high))
        attempt += 1

    if(attempt >= max_attempts): 
        print("You Lost! Answer was: ", number)
    pass

def main():
    print("---------- Welcome to the number guessing game ----------")
    high_score = 0 # currunt high score which is zero, we will update it soon

    bool = False
    top_scores = [] # cretead a list
    count = 1

    while(bool == False):
        mode = get_difficulty() # enter the difficulty
        start = datetime.datetime.now() ## game has started

        num = play_round(*mode)
        end = datetime.datetime.now()

        print("Total time taken to solve the game is: ", end - start)
        # this would print the total time executed

        if(count <= 3):
            top_scores.append(num)
            top_scores.sort(reverse= True) # sort in the descending order
        elif(num > top_scores[2]):
            top_scores.pop() # pops the last which is the lowest score
            top_scores.append(num) # adds it to the last
            top_scores.sort(reverse= True)
        # takes consideration for the highest element - only 3 
        # this takes the first three cases since these all are the high scores

        if(num > high_score): high_score = num    
        # prints the high score
    
        print("high score in this sessions: ", high_score)

        with open("Top Scores.txt", "w") as file:
            file.write("The top scores of the last gameplay:- \n") 
            for score in top_scores:
                file.write(str(score) + "\n")
        # it replaces every writing, so the top scores are getting wriiten

        play = input("enter y/n or exit whether you want to play the game again? ").lower().strip();
        if(play == "y"): bool = False
        elif(play == "n"): bool = True
        elif(play == "exit"): break

        else: print("Wrong input, try again:- ")

if __name__ == "__main__":
    main()