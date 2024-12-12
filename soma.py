def calcular_crescimento(pa, pb, ta, tb):
    ano = 2021
    while pa <= pb:
        pa += pa * (ta / 100)
        pb += pb * (tb / 100)
        ano += 1
        if ano > 3000:  # Limite arbitrário para evitar loop infinito
            return "População menor não ultrapassará a maior."
    return ano

pa = int(input("População de A em 2021: "))
pb = int(input("População de B em 2021: "))
ta = float(input("Taxa de crescimento de A (%): "))
tb = float(input("Taxa de crescimento de B (%): "))
if pa < pb:
    ano = calcular_crescimento(pa, pb, ta, tb)
else:
    ano = calcular_crescimento(pb, pa, tb, ta)
print(f"A população menor ultrapassará a maior no ano: {ano}")