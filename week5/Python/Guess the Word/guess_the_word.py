import random 

ENGLISH_WORDS = [
    "python", "variable", "function", "computer", "network",
    "terminal", "protocol", "database", "interface", "algorithm"
]
try_count = 5
secret_word=[]
status_word = []
used_letters = []
def initialize_game(words):
    """The function initializes the game, selects the word,
       and updates the appropriate variables."""
    global secret_word
    global try_count
    global status_word 
    i_word = random.randint(0,len(words)-1)
    secret_word = words[i_word]
    status_word = ["-"]*len(secret_word)

def status_display():
    global status_word
    global try_count
    global used_letters
    """The function brings you your current game status."""
    print("*"*30)
    print(f"The state of the words you guessed: {"".join(status_word)}")
    print("/"*30)
    print(f"The number of guesses you have left : {try_count}")
    print("/"*30)
    print(f"The letters you used : {used_letters}")
    print("*"*30)


def get_player_guess():
   """The function receives 
   the signal from the user and checks its validity."""
   while True:
       char = input("Enter the letter you think will fit from A to Z.")
       char: str
       if char.isascii() and char.isalpha():
           return char.lower()


def is_guess_correc(char):
    """The function checks if the signal is correct for use."""
    global status_word
    global used_letters
    global secret_word
    global try_count
    
    used_letters.append(char)
    if char in secret_word and char not in status_word:
        return True
    try_count -= 1
    return False

def update_game_state(char):
    """The function receives a valid character 
    and checks where it should be."""
    global secret_word
    global status_word
    new_i = 0
    for i, signal in enumerate(secret_word):
        if signal == char:
            status_word[i] = char 


def display_current_status():
    pass

def is_game_finished():

    """The function checks whether it has reached the end and prints accordingly."""
    global status_word
    global try_count
    global secret_word
    if "".join(status_word) == secret_word:
        "".join(secret_word)
        print("*"*60)
        print(f"Well done, you managed to identify the word:{"".join(secret_word)}")
        print("*"*60)
        return True
    elif try_count == 0 :
        print("*"*60)
        print("The number of attempts has reached 0.")
        print("*"*60)
        return True
    return False

def main(list_words : list):
    initialize_game(list_words)
    print(secret_word)
    while True:
        finish = is_game_finished()
        if finish:
            break
        status_display()
        char = get_player_guess()
        change = is_guess_correc(char)
        if change:
            update_game_state(char)
        continue    


main(ENGLISH_WORDS)