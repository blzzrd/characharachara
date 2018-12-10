# char.py
# go through an amount of times and create a list of possible character combinations
# featuring a-z, 0-9, and '_'. 


# A few constants of our parameters.
BASE = 48 # Want to start at 48 ASCII
RANGE = 123 # Don't want to go over 123 ASCII
AFTERNUM = 58 # After the numbers on ASCII
UNDERSCORE = 95 # Underscore in ASCII
LETTERSBASE = 97 # Where the letters start in ASCII)
allcombos = [] # List that holds all the options

# Wrapper function that will input basic information.
def chara(count):
    string = ""    
    return chara_R(string, count, 1)

# Actual Recursive go through to PRINT all possible elements.
def chara_R(string, count, stage):
    total = 0

    c = BASE
    if count != stage:
        while c < RANGE:
            if c == AFTERNUM:
                c = UNDERSCORE
            if c == (UNDERSCORE + 1):
                c = LETTERSBASE
            total += chara_R(string + chr(c), count, stage + 1)
            c += 1
            
    else:
        while c < RANGE:
            if c == AFTERNUM:
                c = UNDERSCORE
            if c == (UNDERSCORE + 1):
                c = LETTERSBASE


            allcombos.append(string + chr(c))
            # print(string + chr(c))
            total += 1
            c += 1

    return total


# getDigits will get the amount of characters there will be.
def getDigits(override = False):
    print("X = 1 | XX = 2 | XXX = 3 ... So on...")
    digits = input("How many characters should this be out of? ")

    if not override:
        if digits > 10:
            print("Too many computations. Toggle Override.")
            exit()
    
    return digits




# Where the work begins

n = getDigits()  # Use getDigits(true) for longer combinations.
combos = chara(n)

# A-Z + 0-9 + '_' potential combinations to the n'th.
potential = (26 + 10 + 1) ** n

print("Found {} combinations out of the possible {} combinations.".format(combos, potential))

for items in allcombos:
    print(items)


# THE HARD CODED METHOD.
'''
def two():
    count = 0
    a = 48
    while a < 123:
        if a == 58:
            a = 95
        if a == 96:
            a = 97
        
        b = 48
        while b < 123:
            if b >= 58 and b <= 94:
                b = 95
            if b == 96:
                b = 97

            print(chr(a) + chr(b))
            count += 1
            b += 1
        a += 1
    return count


total = two()
print("total outputs: " + str(total))
'''