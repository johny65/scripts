#!/usr/bin/python3
# -*- coding: utf8 -*-

#TODO:
#parsear archivos
#elegir qué caracter termina la url (" o espacio, etc)
#agregar filtro

import sys

def limpiar(contenido):
    res = []
    for l in contenido:
        if "<a " in l:
            res.append(l)
    return res
    
def extraer_links(contenido):
    res = []
    for l in contenido:
        buscar(l, "http://", res)
        buscar(l, "https://", res)
    for l in res:
        print(l)

def buscar(l, s, res):
    posini = l.find(s)
    while posini != -1:
        posfinal = l.find('"', posini)
        res.append(l[posini:posfinal])
        posini = l.find(s, posfinal)
    
def leer_entrada():
    return sys.stdin.readlines()

if __name__ == "__main__":
    if sys.argv[1:] and sys.argv[1] == "-a":
        extraer_links(limpiar(leer_entrada()))
    else:
        extraer_links(leer_entrada())
