#!/usr/bin/env python3
from lxml import etree
""" Получение данных из КПТ """
doc=etree.parse("0000.xml")

for elem in doc.iter("Cadastral_Block"):
    print(elem.get("CadastralNumber"))
for elem in doc.iter("Number"):
    print(elem.text)
for elem in doc.iter("Date"):
    print(elem.text)
for elem in doc.iter("Organization"):
    print(elem.text)
for elem in doc.iter("Cadastral_Block"):
    print(elem.get("CadastralNumber"))

    
for elem1 in doc.iter("Parcel"):
    print('=================================')
    #print(elem1.attrib)
    uchastok_number=elem1.get('CadastralNumber')
    print('Cadastr Number: '+uchastok_number)
    print(uchastok_number[12:])
    for elem2 in elem1.iter("Entity_Spatial"):
        #print('-------------------------')
        #print(elem2.attrib)
        print('----------------------------------')
        for elem3 in elem2.iter("Spelement_Unit"):
            for elem4 in elem3.iter("Ordinate"):
                X=elem4.get('X')
                Y=elem4.get('Y')
                print('Koord X: '+X)
                print('Koord Y: '+Y)
