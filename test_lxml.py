#!/usr/bin/env python3
import os
from lxml import etree
""" Данные со всех файлов КПТ в текущей папке """
path_to_file='.'
dir_list = os.listdir(path=path_to_file)
txt_file=open(path_to_file[2:]+'data.txt', mode='w')

for file_name in dir_list:
    if (file_name[-3:])=='xml':
        doc=etree.parse(file_name)
        txt_file.write('-----------------------------------------------------\n')

        for elem in doc.iter("Cadastral_Block"):
            print(elem.get("CadastralNumber"))
            txt_file.write('Кадастровый номер: '+elem.get("CadastralNumber")+'\n')
        for elem in doc.iter("Number"):
            txt_file.write(elem.text+'\n')
        for elem in doc.iter("Date"):
            temp_elem=elem.text
            year=temp_elem[0:4]
            months=temp_elem[5:7]
            day=temp_elem[-2:]
            txt_file.write(day+'.'+months+'.'+year+'\n')
            
        for elem in doc.iter("Organization"):
            txt_file.write(elem.text+'\n')
txt_file.close()
