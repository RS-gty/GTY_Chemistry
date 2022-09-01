# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 17:31
# @Author  : 之落花--falling_flowers
# @File    : Chem_Restructure.py
# @Software: PyCharm
import re
import numpy as pd
from typing import *

elements = dict(H=1, He=4, Li=7, Be=9, B=11, C=12, N=14, O=16, F=19, Ne=20, Na=23, Mg=24, Al=27, Si=28, P=31, S=32, Cl=35.5, Ar=40, K=39, Ca=40, Sc=45, Ti=48, V=51, Cr=52, Mn=55, Fe=56, Co=59, Ni=59, Cu=64, Zn=65, Ga=70, Ge=73, As=75, Se=79, Br=80, Kr=85, Rb=85.5, Sr=88, Y=89, Zr=91, Nb=93, Mo=96, Tc=99, Ru=101, Rh=103, Pd=106.5, Ag=108, Cd=112.5, In=115, Sn=119, Sb=122, Te=128, I=127, Xe=131, Cs=133, Ba=137, LANTHANIDE=0, Hf=178.5, Ta=181, W=184, Re=186, Os=190, Ir=192, Pt=195, Au=197, Hg=200.5, Tl=204, Pb=207, Bi=209, Po=209, At=210, Rn=222)


def get_information(compound: AnyStr, n: int = 1) -> tuple[int, dict]:
    """
    计算化学式相对质量和各元素数量,返回一个元组包含质量和元素数量字典

    :param compound: 物质化学式
    :param n: 物质数量
    :return: tuple: (int: 相对质量, dict: 元素个数)
    """
    quality, elements_amonunt = 0, {e: 0 for e in re.findall('[A-Z][a-z]*', compound)}
    for part in compound.split('.'):
        n *= int(re.findall(r'^\d*', part)[0]) if re.findall(r'^\d*', part).pop(0) else 1
        part_quality, part_elements_amount = 0, {e: 0 for e in re.findall('[A-Z][a-z]*', compound)}
        for one_element in re.findall(r'\(.*\)[0-9]*|[A-Z][a-z]*[0-9]*', part):
            part_quality += get_information(re.findall(r'\((.*)\)', one_element)[0], int(re.findall(r'\d*$', one_element)[0]))[0] if '(' in one_element else ((int(re.findall(r'\d*$', one_element)[0]) if re.findall(r'\d*$', one_element)[0] else 1) * elements[re.findall(r'[A-Z][a-z]*', one_element)[0]])
            if '(' not in one_element:
                part_elements_amount[re.findall(r'[A-Z][a-z]*', one_element)[0]] += int(re.findall(r'\d*$', one_element)[0]) if re.findall(r'\d*$', one_element)[0] else 1
            else:
                result = get_information(re.findall(r'\((.*)\)', one_element)[0], int(re.findall(r'\d*$', one_element)[0]))[1]
                for key in result.keys():
                    part_elements_amount[key] += result[key]
        quality += part_quality * n
        for key in part_elements_amount.keys():
            elements_amonunt[key] += part_elements_amount[key] * n
    return quality, elements_amonunt


def equation(reactants_tuple: Tuple[AnyStr, ...], product_tuple: Tuple[AnyStr, ...]) -> Tuple[int, ...]:
    """
    打印配平后的方程式,返回配平系数的元组(只限于基础方程式,不保证一定正确!)

    :param reactants_tuple: 反应物元组
    :param product_tuple: 生成物元组
    :return: 配平系数元组
    """
    general_list, elements_amonunt = [], {x: 0 for x in elements.keys()}
    for substance_list, list_type in zip((reactants_tuple, product_tuple), (1, 0)):
        for part in substance_list:
            part_elements_amonunt_dict, part_elements_amonunt = elements_amonunt.copy(), get_information(part, 1)[1]
            for key in part_elements_amonunt.keys():
                part_elements_amonunt_dict[key] = part_elements_amonunt[key]
            general_list.append(list(part_elements_amonunt_dict.values()) + [0]) if list_type else general_list.append([x for x in map(lambda x: -x, part_elements_amonunt_dict.values())] + [0])
    general_list[-1][-1] = 1
    coefficient_array = pd.dot(pd.linalg.pinv(pd.array(general_list).T), pd.array([0] * 72 + [1]))
    for multiplier in range(1, 1024):
        for coefficient in coefficient_array * multiplier:
            if abs(round(coefficient) - coefficient) > 0.0001:
                break
        else:
            coefficient_array *= multiplier
            break
    string_list, return_tuple = [], []
    for compound, coefficient in zip(reactants_tuple + product_tuple, coefficient_array):
        string_list += [str(round(coefficient)), compound, ' + ']
        return_tuple.append(int(round(coefficient)))
    string_list[len(reactants_tuple) * 3 - 1] = ' ----> '
    string_list = [i for i in string_list[:-1] if i != '1']
    print(''.join(string_list))
    return tuple(return_tuple)


if __name__ == '__main__':
    print(get_information('(NH4)2SO4.2H2O'))
    equation(('(NH4)2SO4.2H2O', 'NaOH'), ('NH3', 'H2O', 'Na2SO4'))
    equation(('KMnO4', 'H2O2', 'H2SO4'), ('K2SO4', 'O2', 'MnSO4', 'H2O'))
