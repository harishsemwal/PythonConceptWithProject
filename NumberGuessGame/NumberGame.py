import random
number = random.randint(1, 100)
count = 1;
while True:
    userChoice = (input("Guess The number between 1 to 100 & Quit(Q): "))
    if(userChoice == 'Q'):
        print("Quit the Game Sucessfully...")
        break
    userChoice = int(userChoice)
    if userChoice < number :
        print("Your number is Small...")
        print("Choose Big Number: ")
        count += 1
    elif(userChoice > number):
        print("Your number is Big...")
        print("Choose Small Number: ")
        count+=1
    elif(userChoice == number):
        print("Congratulation...")
        print("You Guess The Correct Number")
        print("Tune number ", count , " Bari mai Nikala.")
        break