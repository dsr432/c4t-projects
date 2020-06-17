#TODO: def wanna go through and shorten this whole thing up a bit lol
import random

oalph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def getrankey():
    alphnum = random.randint(0, 25)
    global key
    key = alph[alphnum]

def enq():
    global message
    message = list(input("Please input a message to be encoded: ").lower())
    gira = input ("Do you have a key? Yes or no? ")
    if gira == "yes":
        global key
        key = input("What is the starting letter of the key? ").lower()
        en()
    elif gira == "no":
        getrankey()
        en()
    else:
        print("You must have misstyped, please try again. ")
        enq()

def en():
    while alph.index(key) != 0:
        alph.append(alph[0])
        alph.remove(alph[0])
    mlen = len(message)
    x = 0
    while x < mlen:
        if message[x] in alph:
            message[x] = alph[oalph.index(message[x])]
            x += 1
        else:
            x += 1
    messagefinal = "".join(str(e) for e in message)
    print(messagefinal)

def deq():
    global message
    message = list(input("Please input a message to be decoded: ").lower())
    gira = input ("Do you have a key? Yes or no? ")
    if gira == "yes":
        global key
        key = input("What is the starting letter of the key? ").lower()
        de()
    elif gira == "no":
        print("get ready to do some reading then cuz we be doin all dem")
        deall()
    else:
        print("You must have misstyped, please try again. ")
        deq()

def de():
    while alph.index(key) != 0:
        alph.append(alph[0])
        alph.remove(alph[0])
    mlen = len(message)
    x = 0
    while x < mlen:
        if message[x] in alph:
            message[x] = oalph[alph.index(message[x])]
            x += 1
        else:
            x += 1
    messagefinal = "".join(str(e) for e in message)
    print(messagefinal)

def deall():
    #TODO: uhhh ok so for some reason this has one repeat of the correct response every time and im so confused help. 
    for key in oalph:
        alph = oalph.copy()
        while alph.index(key) != 0:
            alph.append(alph[0])
            alph.remove(alph[0])
        mlen = len(message)
        x = 0
        while x < mlen:
            if message[x] in alph:
                message[x] = oalph[alph.index(message[x])]
                x += 1
            else:
                x += 1
        messagefinal = "".join(str(e) for e in message)
        print(messagefinal)

def main():
    ende = input("would you like to encode or decode a message?")
    if ende == "encode":
        enq()
    elif ende =="decode":
        deq()
    else:
        print("You did not input a proper response... please try again")
        main()

main()
