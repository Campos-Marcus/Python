secret_number = 4
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    
    if guess == secret_number:
        print("you found the number")
        break

else:
    print("you have failed")


