if __name__ == '__main__':

    secret_word = ["sitges", "play", "fly", "trial"]
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_fo_guesses = False

    while guess not in secret_word and not out_fo_guesses:
        if guess_count < guess_limit:
            guess = input("enter guess: ").lower()
            guess_count += 1

        else:
            out_fo_guesses = True

    if out_fo_guesses:
        print(" you lose out of gusses")
    else:
        print(" You win.")
