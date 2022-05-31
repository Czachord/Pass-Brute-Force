import string

def passInput():
    password = input("Enter your password (max 5 characters):\n")

def letters():
    alphabet = list(string.ascii_letters)
    return alphabet

def combinations(numbers1, numbers2):
    if numbers2 == len(letters()):
        numbers1 += 1
        numbers2 = 0



def main():
    print(letters())

if __name__ == "__main__":
    main()