def pocet_slov():
    jmena = open("names.txt")
    text = jmena.read()
    pocet = len(text.split())
    return pocet
print(pocet_slov())