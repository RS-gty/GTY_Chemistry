# coding:utf-8
# Author:RS-gty

import re
import numpy as np

# Constants
ELEMENTS = [['H', 1], ['He', 4],

            ['Li', 7], ['Be', 9], ['B', 11], ['C', 12], ['N', 14], ['O', 16], ['F', 19],
            ['Ne', 20],

            ['Na', 23], ['Mg', 24], ['Al', 27], ['Si', 28], ['P', 31], ['S', 32],
            ['Cl', 35.5], ['Ar', 40],

            ['K', 39], ['Ca', 40], ['Sc', 45], ['Ti', 48], ['V', 51], ['Cr', 52],
            ['Mn', 55], ['Fe', 56], ['Co', 59], ['Ni', 59], ['Cu', 64], ['Zn', 65],
            ['Ga', 70], ['Ge', 73], ['As', 75], ['Se', 79], ['Br', 80], ['Kr', 85],

            ['Rb', 85.5], ['Sr', 88], ['Y', 89], ['Zr', 91], ['Nb', 93], ['Mo', 96],
            ['Tc', 99], ['Ru', 101], ['Rh', 103], ['Pd', 106.5], ['Ag', 108], ['Cd', 112.5],
            ['In', 115], ['Sn', 119], ['Sb', 122], ['Te', 128], ['I', 127], ['Xe', 131],

            ['Cs', 133], ['Ba', 137], 'LANTHANIDE', ['Hf', 178.5], ['Ta', 181], ['W', 184],
            ['Re', 186], ['Os', 190], ['Ir', 192], ['Pt', 195], ['Au', 197], ['Hg', 200.5],
            ['Tl', 204], ['Pb', 207], ['Bi', 209], ['Po', 209], ['At', 210], ['Rn', 222]]


# common_ions

# List Operating
def ListCheckDuplicates(list1: list) -> list:
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
        else:
            pass
    return list2


def MergeLists(list1: list, list2: list) -> list:
    list3 = []
    for i in list1:
        list3.append(i)
    for j in list2:
        list3.append(j)
    return list3


def GenerateList(integer: int, length: int) -> list:
    list1 = []
    for i in range(length - 1):
        list1.append(0)
    list1.append(integer)
    return list1


# Matrix Operating
def GenerateMatrix(integer: int, column: int) -> np.array:
    list1 = []
    for i in range(column - 1):
        list1.append([0])
    list1.append([integer])
    return np.array(list1)


# String Operating
def DivideStringWithInt(string: str):
    string1 = string
    if not re.findall('[0-9]', string):
        string1 += '1'
    else:
        pass
    list1 = [string1[-1], string1[0:-1]]
    return list1


def RemoveParentheses_1(string: str):
    string1 = re.findall('[{][A-Za-z0-9()]*[}]', string)[0][1:-1]
    coefficient1 = re.findall('[1-9]+', re.findall('[}][0-9]+', string)[0])[0]
    list1 = []
    for part in re.findall('[A-Z][^A-Z()]*[0-9]*|[(][a-zA-Z1-9]*[)][0-9]*|[{][A-Za-z1-9()]*[}][0-9]*', string1):
        list1.append(DivideStringWithInt(part)[1] + str(int(DivideStringWithInt(part)[0]) * int(coefficient1)))
    return list1


def RemoveParentheses_2(string: str):
    string1 = re.findall('[(][A-Za-z0-9]*[)]', string)[0][1:-1]
    coefficient1 = re.findall('[1-9]+', re.findall('[)][0-9]+', string)[0])[0]
    list1 = []
    for part in re.findall('[A-Z][^A-Z()]*[0-9]*|[(][a-zA-Z1-9]*[)][0-9]*|[{][A-Za-z1-9()]*[}][0-9]*', string1):
        list1.append([str(int(DivideStringWithInt(part)[0]) * int(coefficient1)), DivideStringWithInt(part)[1]])
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
def SeparateMatterIntoElements(compound: str) -> list:
    # divide coordination compound
    compound = ReplaceElementsInString((ReplaceElementsInString(compound, '[', '{')), ']', '}')
    separation_step1 = compound.split('.')
    # divide compound
    separation_step2 = []
    separation_step3 = []
    for parts_1 in separation_step1:
        for parts_2 in re.findall('[A-Z][^A-Z()]*[0-9]*|[(][a-zA-Z1-9]*[)][0-9]*|[{][A-Za-z1-9()]*[}][0-9]*', parts_1):
            separation_step2.append(parts_2)
    # remove parentheses
    for parts_3 in separation_step2:
        if '{' in parts_3:
            if '(' in parts_3:
                for p in RemoveParentheses_1(parts_3):
                    if '(' in p:
                        separation_step3 += (RemoveParentheses_2(p))
                    else:
                        separation_step3.append(DivideStringWithInt(p))
        elif '(' in parts_3:
            separation_step3 += (RemoveParentheses_2(parts_3))
        else:
            separation_step3.append(DivideStringWithInt(parts_3))
    return separation_step3


def CalculatingRelativeMolecularMass(compound: str) -> int:
    elements = SeparateMatterIntoElements(compound)
    index = 0
    mass = 0
    for element in elements:
        for form in ELEMENTS:
            if element[1] == form[0]:
                mass += int(element[0]) * ELEMENTS[index][1]
                break
            else:
                index += 1
        index = 0
    return mass


def SetCoefficientOfMatter(compound: str, elements: list):
    compound_list = SeparateMatterIntoElements(compound)
    element_list = GenerateList(0, len(elements))
    index = 0
    for i in compound_list:
        for j in elements:
            if i[1] == j:
                element_list[index] += int(i[0])
                break
            else:
                pass
            index += 1
        index = 0
    print(element_list)


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
        self.element_and_count = []


# Equation Class
class Equation(object):
    def __init__(self, reactant: list, resultant: list):
        self.reactants = reactant
        self.resultants = resultant
        self.matters = MergeLists(self.reactants, self.resultants)
        self.reactants_coefficients = []
        self.resultants_coefficients = []
        # self_balance
        elements = []
        for reactant in self.resultants:
            for elements_reactants in SeparateMatterIntoElements(reactant):
                elements.append(elements_reactants[1])
        elements = ListCheckDuplicates(elements)
        print(elements)


if __name__ == '__main__':
    E1 = Equation(['Cu', 'HNO3'], ['Cu(NO3)2', 'NO', 'H2O'])
    print(SetCoefficientOfMatter('H2SO4', ['H', 'S', 'O', 'C']))

