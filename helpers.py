elemendid = []

# lisame ELEMENT juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus in nimetused:
        print("Element {} on juba olemas".format(nimetus))
    else:
        elemendid.append({"nimetus":nimetus, "hind": hind, "kogus": kogus})



# lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

#loeme ELEMENDID korraga, aga nii, et tagastame iga kord üks element
def loe_elemendid():
    global elemendid
    loetud_elemendid = []
    for element in elemendid:
        loetud_elemendid.append(element)
    return loetud_elemendid

#loeme KONKREETNE element
def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
            nimetused.append(list(element.values())[0])
    print(nimetused)
    if nimetus not in nimetused:
        return "Element {} ei eksisteeri".format(nimetus)
    else:
        return elemendid[(nimetused.index(nimetus))]

#uuendame KONKREETSE elemendi
def uuenda_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print( "Elementi {} ei saa uuendada, sest seda ei eksisteeri".format(nimetus))
    else:
        elemendid[(nimetused.index(nimetus))] = {"nimetus":nimetus, "hind":hind, "kogus":kogus}

#kustutame KONKREETSE elemendi
def kustuta_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print( "Elementi {} ei saa kustutada, sest seda ei eksisteeri".format(nimetus))
    else:
        elemendid.remove(elemendid[(nimetused.index(nimetus))])

#kustutame KÕIK elemendid
def kustuta_elemendid():
    global elemendid
    elemendid.clear()


def main():
    #loome katseandmestiku
    katse_elemendid = [
        {"nimetus": "leib", "hind": 0.80, "kogus": 20},
        {"nimetus": "piim", "hind": 0.50, "kogus": 15},
        {"nimetus": "vein", "hind": 5.60, "kogus": 5},
    ]

    #testime elementide lisamist
    lisa_elemendid(katse_elemendid)

    #testime elemendi lisamist
    lisa_element("kohupiim", 0.60, 15)
    lisa_element("vein", 0.80, 5)

    #testime elementide lugemist
    #print(loe_element("kohupiim"))
    #print(loe_element("kirss"))

    #testime elemendi uuendamist
    uuenda_element("vein", 10.0, 10)
    print(loe_element("vein"))

    #testime elemendi kustutamist
    kustuta_element("leib")
    print(loe_element("leib"))

    #testime elementide kustutamist
    kustuta_elemendid()
    print(elemendid)



#käivitame
if __name__ == "__main__":
    main()