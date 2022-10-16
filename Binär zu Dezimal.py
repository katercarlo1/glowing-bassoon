
'''************************************
****binär to dual******'''


exponent = 0
wert = 0
ergebnisse = []
summe = 0



wert = int(input("Bitte geben Sie ihren Dualen Werte ein: "))


while wert != 0:
    letztezahl = wert % 10
    adition = letztezahl * 2**exponent
    ergebnisse.append(adition)
    wert = wert // 10
    exponent = exponent + 1


for zahlen in ergebnisse:
    summe = summe + zahlen
print(summe)
