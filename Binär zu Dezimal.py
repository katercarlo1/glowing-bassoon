'''Erstellen Sie ein Python-Programm, das Dualzahlen in das Dezimalsystem umrechnen kann
, Die letzte Ziffer einer Zahl können Sie löschen, wenn Sie die Zahl durch 10 dividieren und nur das ganzzahlige Ergebnis berücksichtigen.'''

'''************************************
****Dualzahlen ins Dezimalsystem******'''

# Variabeln festlegen
exponent = 0
wert = 0
ergebnisse = []
summe = 0

# Wert einlesen

wert = int(input("Bitte geben Sie ihren Dualen Werte ein: "))
# schleife

while wert != 0:
    letztezahl = wert % 10
    adition = letztezahl * 2**exponent
    ergebnisse.append(adition)
    wert = wert // 10
    exponent = exponent + 1

# zahlen addieren
for zahlen in ergebnisse:
    summe = summe + zahlen
print(summe)
