import re

def findOccurancesOfLetter(inputString, letter):
    occurances = 0
    for inputCharacter in inputString:
        if inputCharacter == letter:
            occurances += 1
    return occurances

def readInputLine(input):
    minOcc, maxOcc, letter, _, password = re.split('-|:| ', input)
    return int(minOcc), int(maxOcc), letter, password

def readInput(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

def checkPasswordValidity(fileName):
    validPasswords = 0
    content = readInput(fileName)
    
    for line in content:
        minOcc, maxOcc, letter, password = readInputLine(line)
        charOccurance = findOccurancesOfLetter(password, letter)
        if charOccurance <= maxOcc and charOccurance >= minOcc:
            validPasswords += 1
    
    return validPasswords

def checkValidityOnCharacterPosition(inputString, letter, positions):

    indexFound = False
    for idx, inputCharacter in enumerate(inputString):
        if inputCharacter == letter and (idx + 1 == positions[0] or idx + 1 == positions[1]):
            if not indexFound:
                indexFound = True
            else:
                return False
    
    return indexFound

def checkPasswordValidityForPosition(fileName):
    validPasswords = 0
    content = readInput(fileName)
    for line in content:
        posOne, posTwo, letter, password = readInputLine(line)
        if checkValidityOnCharacterPosition(password, letter, [posOne, posTwo]):
            validPasswords += 1
    
    return validPasswords

print(checkPasswordValidity('Day2_Input.txt'))
print(checkPasswordValidityForPosition('Day2_Input.txt'))

