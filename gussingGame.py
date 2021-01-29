if __name__ == '__main__':

    secret_word = "sitges"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_fo_guesses = False

    while guess != secret_word:
        guess = input("enter guess: ")

    print(" You win.")
