print("Welcome to my computer quiz!")

authenticate = input("Do you want to play?: ")

if authenticate.lower() != "yes":
    quit()

print("Great! Let's play:)")
score = 0

answer = input("What does CPU stand for?: ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?: ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?: ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What do we call this symbol * ?: ")
if answer.lower() == "asterisk":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PDF stand for?: ")
if answer.lower() == "portable document format":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPS stand for?: ")
if answer.lower() == "global positioning system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does USB stand for?: ").lower()
if answer == "universal serial bus":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct! ")
print("You got " + str((score / 7) * 100) + "%.")
