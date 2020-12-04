import itertools
import re

with open('input4.txt') as f:
    passports = [list(map(lambda line: line.split(' '), passport.splitlines())) for passport in f.read().split('\n\n')]
    passports = [list(itertools.chain.from_iterable(passport)) for passport in passports]
    passports = [dict(map(lambda record: record.split(':'), passport)) for passport in passports]

def passport_has_all_records(passport, required_records=(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',))):
    return all(record in passport for record in required_records)

def n_digit_number(passport, key, n):
    if key in passport:
        value = passport[key]
        if len(value) == n:
            return int(value)
    return None

def passport_byr_valid(passport):
    byr = n_digit_number(passport, 'byr', 4)
    if byr is not None:
        return byr in range(1920, 2002 + 1)
    return False

def passport_iyr_valid(passport):
    iyr = n_digit_number(passport, 'iyr', 4)
    if iyr is not None:
        return iyr in range(2010, 2020 + 1)
    return False

def passport_eyr_valid(passport):
    iyr = n_digit_number(passport, 'eyr', 4)
    if iyr is not None:
        return iyr in range(2020, 2030 + 1)
    return False

def passport_hgt_valid(passport):
    if 'hgt' in passport:
        s = passport['hgt']
        if s[-2:] == 'cm':
            try:
                hgt = int(s[:-2])
            except:
                return False
            return hgt in range(150, 193 + 1)
        elif s[-2:] == 'in':
            try:
                hgt = int(s[:-2])
            except:
                return False
            return hgt in range(59, 76 + 1)
    return False

def passport_hcl_valid(passport):
    if 'hcl' in passport:
        hcl = passport['hcl']
        if len(hcl) == 7 and hcl[0] == '#':
            if re.match('[a-f0-9]{6}', hcl[1:]):
                return True
    return False

def passport_ecl_valid(passport):
    if 'ecl' in passport:
        ecl = passport['ecl']
        return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    return False

def passport_pid_valid(passport):
    pid = n_digit_number(passport, 'pid', 9)
    return pid is not None

def passport_valid(passport):
    valid = all(validation(passport) for validation in (
        passport_byr_valid, 
        passport_iyr_valid, 
        passport_eyr_valid, 
        passport_hgt_valid,
        passport_hcl_valid, 
        passport_pid_valid,
        passport_ecl_valid, 
    ))
    return valid

print(sum(passport_has_all_records(pp) for pp in passports))
print(sum(passport_valid(pp) for pp in passports))