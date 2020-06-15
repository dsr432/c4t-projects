import random

def rpc():
    number = random.randint(0, 2)
    rpclist = ["rock", "paper", "scissors"]
    global choice
    choice = rpclist[number]

def lost():
    play_again = input("oh, you lost... would you like to play again?  Respond \"yes\" or \"no\". ")
    if play_again == "yes":
        game()
    if play_again == "no":
        print("oh, ok, come again soon :>")
        quit()

def win():
    play_again = input("Wow you won!  Would you like to play again? Respond \"yes\" or \"no\". ")
    if play_again == "yes":
        game()
    if play_again == "no":
        print("oh... ok :< come again soon :>")
        quit()

def game():
    user = input("rock, paper, scissors! ")
    rpc()
    print("you chose " + user + ", your opponent chose " + choice + ". ")
    if user == "paper" and choice == "scissors":
        lost()
    elif user == "rock" and choice == "paper":
        lost()
    elif user == "scissors" and choice == "rock":
        lost()
    elif user == "paper" and choice == "rock":
        win()
    elif user == "rock" and choice == "scissors":
        win()
    elif user == "scissors" and choice == "rock":
        win()
    elif user == choice:
        print("Wow!  It looks like we picked the same thing!")
        game()
    else:
        print("there was an error... are you sure you provided propper input?  Let's try that again.")
        game()

def main():
    x = input("Would you like to play a game of rock paper scissors? Respond \"yes\" or \"no\". ")
    if x == "yes":
        y = input("Great! Let's play a game! First, would you like to review the rules? Respond \"yes\" or \"no\". ")
        if y == "yes":
            z = input("Ok.  After the countdown of \"rock, paper, scissors\", respond with either \"rock\", \"paper\", or \"scissors\".  Rock beats scissors, scissors beats paper, and paper beats rock.  Are you ready to play? Respond \"yes\" or \"no\". ")
            if z == "yes":
                print("yeeeee less goooo!!!!")
                game()
            elif z == "no":
                print("oh, ok :< do come again :>")
                quit()
            else:
                print("It looks like you entered an invalid response.  Please try again. ")
                main()
        elif y == "no":
            print("coolio!  Less play!")
            game()
        else:
            print("It looks like you entered an invalid response.  Please try again. ")
            main()
    elif x == "no":
        print("Okay :< come again soon :>")
        quit()
    else:
        print("It looks like you entered an invalid response.  Please try again. ")
        main()

main()
