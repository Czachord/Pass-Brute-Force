import getpass
import string
import time
import keyboard
import datetime

def passInput(letters:list):
    """
    It takes a list of letters as an argument, then prompts the user to enter a password, and if the
    password contains any characters that are not in the list of letters, it will exit the program and
    tell the user which character(s) are not allowed. If the password is longer than 5 characters, it
    will also exit the program and tell the user that the password must be 5 characters or less. If the
    password is valid, it will return the password and the length of the password
    """
    password = getpass.getpass(prompt="Enter your password:", stream=None)
    wrongLetters = []
    for i in range(len(password)):
        if password[i] not in letters:
            wrongLetters.append(password[i])
    if len(wrongLetters) > 0: exit(f'The character(s) {str(wrongLetters)} is not allowed,\nThe only characters allowed are "{string.ascii_letters}"')
    if len(password) > 5: exit("Password must be 5 characters or less.")
    length = len(password)
    print("\n")
    return password, length

def last_index(input_list:list) -> int:
    return len(input_list) - 1

def letters():
    """
    It creates two lists of the alphabet, one uppercase and one lowercase, then combines them into one
    list, and returns that list as a string
    """
    uppercaseList, lowercaseList = list(string.ascii_uppercase), list(string.ascii_lowercase)
    alphabet = []
    for i in range(len(lowercaseList)):
        alphabet.append(lowercaseList[i])
        alphabet.append(uppercaseList[i])
    return listToString(alphabet).replace(" ", "")

def listToString(list:list):
    str1 = " "
    return (str1.join(list))

def combPermutation(combination:list, index:int):
    """
    If the current letter is "Z", then change it to "a" and move to the previous letter. If the previous
    letter is not "Z", then change it to the next letter in the alphabet.
    """
    while combination[index] == "Z":
        combination[index] = "a"
        index -= 1
        if combination[index] != "Z":
            next_index = list(letters()).index(combination[index]) + 1
            combination[index] = letters()[next_index]

def passStriker(password:string, length:int):
    """
    It takes a password and the length of the password, and then it tries every possible combination of
    letters until it finds the password.
    """
    check, tries = [], 1
    for i in range(length):
        check.append(letters()[0])
    while True:
        for i in range(len(letters())):
            strCheck = listToString(check).replace(" ", "")
            index = last_index(check)
            check[index] = letters()[i]
            tries += 1
            alert(tries, strCheck)
            if strCheck == password:
                return strCheck, tries, True
            if check[index] == "Z":
                combPermutation(check, index)

def alert(number:int, text:str):
    """
    It checks if the key 'q' is pressed, if it is, it prints the text and number of tries
    """
    if keyboard.is_pressed('q'):
        print(f'The combination checked is {text} and number of tries is {number}')
        time.sleep(0.1)

def main():
    alphabet = string.ascii_letters
    passwd = passInput(alphabet)
    print("Press Q for current data.")
    start = datetime.datetime.now()
    guessedPass = passStriker(passwd[0], passwd[1])
    finish = datetime.datetime.now()
    if guessedPass[2] == True:
        print(f'I found a password! The password is {guessedPass[0]}.\nI guessed it in the {guessedPass[1]} time. Computation time is {finish-start}')

if __name__ == "__main__":
    main()