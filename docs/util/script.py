from re import *
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def doSubs(dictionary, linha):
  for elem in dictionary:
    linha = sub(rf'{elem}', rf'{dictionary[elem]}', linha)
  return linha


def processaFicheiroTraducoes(nameFileTrad):
    file = open(nameFileTrad, "r").read()

    file = split(r'\s*;\s*', file)
    subs = {}

    for linha in file:
        if linha:
            mode, iN, out, _ = split(r'\/', linha)
            if mode=='s':
                subs[iN] = out
    return subs


print(os.getcwd())

print("Insira o nome do ficheiro de texto a traduzir.")
fileName = input(">> ")

print("Insira o nome do ficheiro de traduções.")
tradFileName = input(">> ")

file = open(fileName, 'r').read()

subs = processaFicheiroTraducoes(tradFileName)

novoTexto = doSubs(subs, file)

file = open(f"out-{fileName}", 'w')
file.write(novoTexto)
file.close()

print("O ficheiro de tradução já se encontra guardado! (ENTER para fechar)")
input()