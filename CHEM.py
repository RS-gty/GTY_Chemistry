# import numpy as np
# from numpy import sqrt
# from itertools import combinations
# import decimal
import re


# Constants

# common_ions

# List Operating

# String Operating
def DivideStringWithInt(string: str):
    string1 = string
    if not re.findall('[0-9]', string):
        string1 += '1'
    else:
        pass
    print(string1)
    list1 = [string1[-1], string1[0:-1]]
    return list1


def RemoveParentheses(string: str):
    string1 = re.findall('[(][A-Za-z0-9]*[)]', string)[0][1:-1]
    coefficient1 = re.findall('[1-9]+', re.findall('[)][0-9]+', string)[0])[0]
    list1 = []
    for part in re.findall('[A-Z][^A-Z()]*[0-9]*|[(][a-zA-Z1-9]*[)][0-9]*|[{][A-Za-z1-9()]*[}][0-9]*', string1):
        list1.append([int(DivideStringWithInt(part)[0])*int(coefficient1), DivideStringWithInt(part)[1]])
    return list1


def MergeListToString(operation_list: list):
    merged_string = ''
    for strings in operation_list:
        merged_string += strings
    return merged_string


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
    return MergeListToString(string.split(element))


def GetCompletedList(string1: str, string2: str):
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
    g = GCD(a, b)
    a_ = a / g
    b_ = b / g
    return int(a_ * b_ * g)


# Operations
def SeparateMatterIntoElements(compound: str):
    # divide coordination compound
    compound = ReplaceElementsInString((ReplaceElementsInString(compound, '[', '{')), ']', '}')
    separation_step1 = compound.split('.')
    # divide compound
    separation_step2 = []
    for parts_1 in separation_step1:
        for parts_2 in re.findall('[A-Z][^A-Z()]*[0-9]*|[(][a-zA-Z1-9]*[)][0-9]*|[{][A-Za-z1-9()]*[}][0-9]*', parts_1):
            separation_step2.append(parts_2)

    print(RemoveParentheses('(SO4)3'))


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
    #M2 = 'KAl(SO4)3.12H2O'
    #M3 = '[Ag(NH3)2]2SO4'
    SeparateMatterIntoElements(M1)
    #SeparateMatterIntoElements(M2)
    #SeparateMatterIntoElements(M3)
