import random

def main():
    sentence = input("Enter (^madlib^): ").split()
        
    lines = int(input("Enter number of blank lines to hide the madlib: "))

    for i in range(lines):
        print("")

    newsentence = ""
    trigger = ""
    for word in sentence:
        if word.startswith("(^") and word.endswith("^)") and trigger == "":
            originalword = word[2:-2]
            newword = input("Enter comma-separated choices for " + originalword + ": ")
            newsentence += choose(newword) + " "
            trigger = ""
        elif word.startswith("(^") and not word.endswith("^)"):
            trigger += " " + word[2:]
        elif word.endswith("^)") and not word.startswith("(^"):
            trigger += " " + word[:-2]
            newword = input("Enter comma-separated choices for " + trigger + ": ")
            newsentence += choose(newword) + " "
            trigger = ""
        elif not trigger == "":
            trigger += " " + word
        else:
            newsentence += word + " "

    print(newsentence)

def choose(words):
    words = words.split(",")
    ran = random.randint(0, len(words) - 1)
    return words[ran].strip()

main()