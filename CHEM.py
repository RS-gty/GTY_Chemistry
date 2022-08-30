# import numpy as np
# from numpy import sqrt
# from itertools import combinations
# import decimal
import re


# Constants

# common_ions

# List Operating

# String Operating
def MergeListToString():
    pass


def ReplaceElementsInString(string: str, old: str, new: str) -> str:
    split_string = string.split(old)
    count_parts = len(split_string)
    counter = 1
    merged_string = ''
    for Part in split_string:
        merged_string += Part
        if counter < count_parts:
            merged_string += new
        counter += 1
    return merged_string


def ClearElementInString(string: str, element: str) -> str:
    pass


def IsMultipleCapitalLetters(string: str) -> bool:
    counter = 0
    for s in string:
        if s.isupper():
            counter += 1
        else:
            pass
    if counter > 1:
        return True
    else:
        return False


# Calculate
def GCD(a, b) -> int:
    """最大公因数"""
    if a < b:
        temp = b
        b = a
        a = temp
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return GCD(remainder, b)


def LCM(a, b) -> int:
    """最小公倍数"""
    g = GCD(a, b)
    a_ = a / g
    b_ = b / g
    return int(a_ * b_ * g)


def testifitworks():
    pass

# Operations
def SeparateMatterIntoElements(compound: str):
    # divide coordination compound
    compound = ReplaceElementsInString((ReplaceElementsInString(compound, '[', '{')), ']', '}')

    separation_step1 = compound.split('.')
    print(separation_step1)
    # remove parentheses
    for separated_parts in separation_step1:
        print(re.findall('[{][A-Za-z1-9()]*[}][0-9]', separated_parts))
    separation_step2 = re.findall('[A-Z][^A-Z][0-9]*|[(][a-zA-Z1-9]*[)][0-9]*', 'Cu14(OH)12(SO4)13')
    print(separation_step2)


# Atom Class
class Atom(object):
    def __init__(self, element: str, charge: int):
        self.element = element
        self.charge = 0
        self.value = [self.element, self.charge]
        if charge == 0:
            self.name = element
        else:
            if self.charge > 0:
                if self.charge == 1:
                    self.name = self.element + '+'
                else:
                    self.name = self.element + ' ' + str(self.charge) + '+'
            else:
                if self.charge == -1:
                    self.name = self.element + '-'
                else:
                    self.name = self.element + ' ' + str(-self.charge) + '-'

    def display(self):
        print(self.name)

    def r(self):
        return self.name


# Compound Class
class IonicCompound(object):
    def __init__(self, cation: Atom, anion: Atom):
        self.cation = cation.value
        self.anion = anion.value
        if abs(self.cation[1]) == abs(self.anion[1]):
            if self.cation == ['H', 1] and self.anion == ['OH', -1]:
                self.name = 'H2O'
            elif self.cation == ['NH4', 1] and self.anion == ['OH', -1]:
                self.name = 'NH3.H2O'
            else:
                self.name = self.cation[0] + self.anion[0]
            self.cation_count = 1
            self.anion_count = 1
        else:
            cation_coefficient = abs(int(LCM(self.cation[1], abs(self.anion[1])) / self.cation[1]))
            anion_coefficient = abs(int(LCM(self.cation[1], abs(self.anion[1])) / self.anion[1]))
            self.cation_count = cation_coefficient
            self.anion_count = anion_coefficient
            if IsMultipleCapitalLetters(self.cation[0]) and cation_coefficient != 1:
                cation_element = '(' + self.cation[0] + ')'
            else:
                cation_element = self.cation[0]
            if IsMultipleCapitalLetters(self.anion[0]) and anion_coefficient != 1:
                anion_element = '(' + self.anion[0] + ')'
            else:
                anion_element = self.anion[0]
            if cation_coefficient == 1:
                self.name = cation_element + anion_element + str(anion_coefficient)
            elif anion_coefficient == 1:
                self.name = cation_element + str(cation_coefficient) + anion_element
            else:
                self.name = cation_element + str(cation_coefficient) + anion_element + str(anion_coefficient)
        self.value = [self.cation, self.anion]

    def display(self):
        print(self.name)

    def r(self):
        return self.name


class MolecularCompound(object):
    def __init__(self):
        self.element_count = []
        self.element = []


if __name__ == '__main__':
    M1 = 'Cu2(OH)2CO3'
    M2 = 'KAl(SO4)3.12H2O'
    M3 = '[Ag(NH3)2]2SO4'
    SeparateMatterIntoElements(M1)
    SeparateMatterIntoElements(M2)
    SeparateMatterIntoElements(M3)
