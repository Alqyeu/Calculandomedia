# -*- coding: utf-8 -*-
"""Calculando média.ipynb
"""

n1 = float(input("Sua primeira nota: "))
n2 = float(input("Sua segunda nota: "))
if n1 < 6 and n1 + n2 < 12 and n1 <= n2:
        print("Voce vai fazer recuperação ://")
        n3 = float(input("Sua Terceira nota: "))
        n1, n3 = n3, n1
if n2 < 6 and n1 + n2 < 12:
        print("Voce vai fazer recuperação ://")
        n3 = float(input("Sua Terceira nota: "))
        n2, n3 = n3, n1
media = (n1+n2)/2
if media >=6:
        print("Parabéns!! você passou :D")
        print(f"A sua média é {media:.1f}!!")
else:
        print("Você reprovou D:")
        print(f"A sua média é {media:.1f}.")