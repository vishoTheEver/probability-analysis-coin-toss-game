import random

def main():
    n = int(input("What's n?: "))
    sequence = generate_cointoss(n)
    aliceScore, bobScore = calculate_scores(sequence)
    print(sequence)
    print("Alice scored " + str(aliceScore/n) + " & Bob scored " + str(bobScore/n))
    if aliceScore > bobScore:
        print("Alice is the Winner")
    elif bobScore > aliceScore:
        print("Bob is the Winner")

def generate_cointoss(n):
    sequence = ""
    for i in range(n):
        if (random.choice(["H", "T"]) == "H"):
            sequence += "H"
        else:
            sequence += "T"
    return sequence

def calculate_scores(s):
    a, b = 0, 0
    for i in range(len(s)-1):
        occurance = s[i:i+2]
        if occurance == "HH":
            a += 1
        elif occurance == "HT":
            b += 1
    return (a, b)

main()