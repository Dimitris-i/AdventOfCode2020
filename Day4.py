# Day 4 - Advent of code
import re

def processPassports(filename):
    with open(filename) as file:
        lines = file.readlines()
    # Add an empty char as the last entry since it is used as a delimiter for the passport reading
    lines.append('')

    passport = {}
    passportKeys = []
    passportValues = []
    numOfValidPassports = 0
    validFields = ['byr','iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for line in lines:
        dataLine = line.strip()
        # use the converted \n to '' as a delimiter for a new passport entry
        if dataLine == '':
            validPassport = True
            passport = dict(zip(passportKeys, passportValues))
            for field in validFields:
                if field not in passport:
                    validPassport = False
                    break
                if field == 'byr':
                    match = re.search(r'[0-9]{4}', passport[field])
                    byr = int(passport[field])
                    if not match or (byr < 1920 or byr > 2002 ):
                        validPassport = False
                elif field == 'iyr':
                    match = re.search(r'[0-9]{4}', passport[field])
                    iyr = int(passport[field])
                    if not match or (iyr < 2010 or iyr > 2020 ):
                        validPassport = False 
                elif field == 'eyr':
                    match = re.search(r'[0-9]{4}', passport[field])
                    eyr = int(passport[field])
                    if not match or (eyr < 2020 or eyr > 2030 ):
                        validPassport = False  
                elif field == 'hgt':
                    match = re.search(r'^([0-9]{2}(in){1}|[0-9]{3}(cm){1})', passport[field])
                    if not match:
                        validPassport = False
                    else:
                        hgt = passport[field]
                        hgt_value = int(hgt[:-2])
                        if hgt[-2:] == 'cm' and (hgt_value > 193 or hgt_value < 150):
                            validPassport = False  
                        elif hgt[-2:] == 'in' and (hgt_value > 76 or hgt_value < 59):
                            validPassport = False 
                elif field == 'hcl':
                    match = re.search(r'#[a-zA-Z0-9_.-]{6}$', passport[field])
                    if not match:
                        validPassport = False
                elif field == 'ecl':
                    match = re.search(r'\b(amb|blu|brn|gry|grn|hzl|oth)\b', passport[field])  
                    if not match:
                        validPassport = False
                elif field == 'pid':
                    match = re.search(r'(?<!\d)\d{9}(?!\d)', passport[field])
                    if not match:
                        validPassport = False         

            if validPassport:
                numOfValidPassports += 1
                
            passport = {}
            passportKeys = []
            passportValues = []
        else:
            passportFields = re.split(':| ', dataLine)
            passportKeys = passportKeys + passportFields[::2]
            passportValues = passportValues + passportFields[1::2]
        
    return numOfValidPassports

print(processPassports('Day4_Input.txt'))
