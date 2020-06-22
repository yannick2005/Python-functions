import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict["date"])
    output = "{0} attempts, date: {1}, the secret was {2}".format(
        str(score_dict["attempts"]),
        score_dict("date"),
        str(score_dict["secret"])
    )
    print(output)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append(
            {
                "attempts": attempts,
                "date": str(datetime.datetime.now()),
                "secret": secret
            }
        )
        
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
