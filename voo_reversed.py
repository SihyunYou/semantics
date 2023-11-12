import sys
import re
from colorama import init, Fore, Back, Style

init(autoreset = True)

with open(sys.argv[1], 'r', encoding = 'UTF-8') as f:
    lignes = ''.join(f.readlines()).split('&')

mots = []
for ligne in lignes:
    mots.append(ligne.split('|')[::-1])

del mots[-1]
import random

def foo(_s):
    s = _s.lower().replace('à', 'a').replace('â', 'a').replace('æ', 'ae').replace('é', 'e').replace('è', 'e').replace('ë', 'e').replace('ê', 'e').replace('î', 'i').replace('ï', 'i').replace('ô', 'o').replace('œ', 'oe').replace('û', 'u').replace('ù', 'u').replace('ç', 'c').replace('(', '').replace(')', '')
    s = re.sub(r'\[[^)]*\]', '', s)
    s = re.sub(r'\([^)]*\)', '', s)
    s = s.replace('  ', ' ').strip()
    return s

def too(_a, _b):
    a = [foo(x) for x in _a.split(', ')]
    b = [foo(x) for x in _b.split(', ')]
    if sorted(a) == sorted(b):
        return True
    return False
                

while len(mots) > 0:
    random.shuffle(mots)
    p = random.randint(0, len(mots) - 1)
    #print(foo(mots[p][0]))
    print(Fore.GREEN + str(len(mots)) + '. ' + mots[p][1])
    s = input().strip()
    
    if foo(mots[p][0]) == s or too(mots[p][0], s) or s == 'foo':
        print(Fore.CYAN + Back.LIGHTWHITE_EX + "정답입니다. " + mots[p][0] + '\n')
        del mots[p]
    else:
        print(Fore.RED + Back.LIGHTWHITE_EX + "오답입니다. " + mots[p][0])
        while True:
            print("다시 한번 적어보세요.")
            t = input().strip()
            if foo(mots[p][0]) == t or too(mots[p][0], t) or t == 'foo':
                break
        print()
