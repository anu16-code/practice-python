life = 6
secret_word = list("Mountain")
display = "________"
guess = input("guess a letter:").lower()
if guess in secret_word:
    display = display[:secret_word.index(guess)] + guess + display[secret_word.index(guess) + 1:]
else:
    life = life - 1
while life > 0:
    print(display)
    if display == "".join(secret_word):
        print("you win!")
        break
    guess = input("guess a letter:").lower()
    if guess in secret_word:
        display = display[:secret_word.index(guess)] + guess + display[secret_word.index(guess) + 1:]
    else:
        life = life - 1
        if life == 0:
            print("You have 0 life left. game over!")