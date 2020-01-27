import random
import time
# Exercícios básicos

# Ex 1
numero1 = input("Digite a nota 1: ")
numero2 = input("Digite a nota 2: ")
faltas = input("Numero de faltas: ")
nota1 = int(numero1)
nota2 = int(numero2)
numero_faltas = int(faltas)

media = (nota1 + nota2) / 2.0

if media == 10 and numero_faltas < 20:
    print ("Aprovado com nota máxima")
elif media >= 5 and numero_faltas < 20:
    print ("Aluno aprovado")
else:
    print ("Aluno reprovado")


# Ex 2 (jogo de Jokenpo manual)
print("##############################")
print("Bem-vindo ao Jokenpo do Packer")
print("##############################")

# Zerar variáveis
#jogos = 0
#win1 = 0
#win2 = 0
#

v1 = 0
v2 = 0
pd = "pedra"
t = "tesoura"
pp = "papel"
vence1 = "Jogador 1 venceu"
vence2 = "Jogador 2 venceu"
hist1 = "Jogador 1 tem %d  vitórias"
hist2 = "Jogador 2 tem %d  vitórias"
s = "sim"
n = "não"
#
p1 = input("Vez do jogador 1: ")
p2 = input("Vez do jogador 2: ")

if p1 == p2:
    print("Houve um empate!")
    jogos += 1
elif p1 == pd and p2 == t:
    print(vence1)
    win1 += 1
    print(hist1 % win1)
    jogos += 1
elif p1 == pd and p2 == pp:
    print(vence2)
    win2 += 1
    print(hist2 % win2)
    jogos += 1
elif p1 == t and p2 == pd:
    print(vence2)
    win2 += 1
    print(hist2 % win2)
    jogos += 1
elif p1 == t and p2 == pp:
    print(vence1)
    win1 += 1
    print(hist1 % win1)
    jogos += 1
elif p1 == pp and p2 == pd:
    print(vence1)
    win1 += 1
    print(hist1 % win1)
    jogos += 1
else:
    print(vence2)
    win2 += 1
    print(hist2 % win2)
    jogos += 1

hist = input("Deseja ver o histórico de jogos? ")
if hist == s:
    print("Total de jogos: %d" % jogos)
    print("Vitórias jogador 1: %d" % win1)
    print("Vitórias jogador 2: %d" % win2)

play = input("Deseja jogar novamente? ")
if play == s:
    runfile('C:/Users/leonardo.packer/Desktop/Curso/exercicios1.py',
            wdir='C:/Users/leonardo.packer/Desktop/Curso')
else:
    print("Encerrando o programa...")

# Ex 3 (Jokenpo aleatório)
print("##############################")
print("Bem-vindo ao Jokenpo Aleatório do Packer")
print("##############################")
random1 = random.randint(0,2)
random2 = random.randint(0,2)

if random1 == 0:
    p1 = pd
elif random1 == 1:
    p1 = t
else:
    p1 = pp
    
if random2 == 0:
    p2 = pd
elif random2 == 1:
    p2 = t
else:
    p2 = pp
    
jogar = input("Deseja iniciar o jogo? ")
if jogar == s:
    if p1 == p2:
        print("Houve um empate!")
        jogos += 1
    elif p1 == pd and p2 == t:
        print(vence1)
        win1 += 1
        print(hist1 % win1)
        jogos += 1
    elif p1 == pd and p2 == pp:
        print(vence2)
        win2 += 1
        print(hist2 % win2)
        jogos += 1
    elif p1 == t and p2 == pd:
        print(vence2)
        win2 += 1
        print(hist2 % win2)
        jogos += 1
    elif p1 == t and p2 == pp:
        print(vence1)
        win1 += 1
        print(hist1 % win1)
        jogos += 1
    elif p1 == pp and p2 == pd:
        print(vence1)
        win1 += 1
        print(hist1 % win1)
        jogos += 1
    else:
        print(vence2)
        win2 += 1
        print(hist2 % win2)
        jogos += 1
else:
    print("Encerrando o programa")

if jogar == s:
    play = input("Deseja jogar novamente? ")
    if play == s:
        time.sleep(0.5)
        print("Reiniciando programa...")
        time.sleep(2)
        runfile('C:/Users/leonardo.packer/Desktop/Curso/exercicios1.py',
                wdir='C:/Users/leonardo.packer/Desktop/Curso')
    else:
        print("Encerrando o programa...")
