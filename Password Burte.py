import string
import datetime

def passInput(letters):
    password = input("Enter your password:\n")
    wrongLetters = []
    for i in range(len(password)):
        if password[i] not in letters:
            wrongLetters.append(password[i])
    if len(wrongLetters) > 0: exit(f'The character(s) {str(wrongLetters)} is not allowed,\nThe only characters allowed are "{string.ascii_letters}"')
    print("\n")
    return password

def clearList(list, znak):
    for e in range(len(list)):
        list[e] = znak

def passBreaking(letters, password):
    checkPass = [letters[0], ]
    while checkPass != password:
        for e in range(len(checkPass)):
            for i in range(len(letters)):
                checkPass[e] = letters[i]
                print(checkPass)
                if checkPass == list(password):
                    return checkPass
                checkPass[e] = letters[0]
        
        checkPass.append(letters[0])
        clearList(checkPass, letters[0])
        if len(checkPass) > 3: exit()

def main():
    alphabet = string.ascii_letters
    password = passInput(alphabet)
    print(str(passBreaking(alphabet, password)))

if __name__ == "__main__":
    main()