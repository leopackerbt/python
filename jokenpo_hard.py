"""
Jogo de jokenpo na dificuldade difícil

Sem uso de lógica de inteligência artificial, apenas probabilidade (fixa) baseada em qual elemento eu jogo
Por exemplo, se eu jogar pedra, a Elise terá 70% de probabilidade de jogar Papel.
"""
import time
from random import choices

s = "sim"
pd = "pedra"
pp = "papel"
t = "tesoura"
win1 = "Você venceu!"
win2 = "Elise venceu!"
jogadas = 0
empates = 0
vit_player = 0
vit_elise = 0
possibilidades = [0, 1, 2]
#papel, pedra, tesoura
prob_pedra = [10, 80, 10]
prob_papel = [80, 10, 10]
prob_tesoura = [10, 10, 80]

comecar = input("Deseja iniciar o jogo? ")
if comecar == s:
    play = input("pedra, papel, ou tesoura? ")
    if play == pd:
        play_elise = choices(possibilidades, prob_papel, k=1)
        if play_elise[0] == 0:
            jogada_final = pp
        elif play_elise[0] == 1:
            jogada_final = pd
        else:
            jogada_final = t
    if play == pp:
        play_elise = choices(possibilidades, prob_tesoura, k=1)
        if play_elise[0] == 0:
            jogada_final = pp
        elif play_elise[0] == 1:
            jogada_final = pd
        else:
            jogada_final = t
    if play == t:
        play_elise = choices(possibilidades, prob_pedra, k=1)
        if play_elise[0] == 0:
            jogada_final = pp
        elif play_elise[0] == 1:
            jogada_final = pd
        else:
            jogada_final = t
        
time.sleep(0.5)
print("Aguardando a resposta de Elise")

print("Elise jogou %s" % jogada_final)
time.sleep(0.5)

if play == jogada_final:
    print("Houve um empate!")
    empates += 1
elif play == pd and jogada_final == t:
    print(win1)
    vit_player += 1
elif play == pd and jogada_final == pp:
    print(win2)
    vit_elise += 1
elif play == t and jogada_final == pd:
    print(win2)
    vit_elise += 1
elif play == t and jogada_final == pp:
    print(win1)
    vit_player += 1
elif play == pp and jogada_final == pd:
    print(win1)
    vit_player += 1
else:
    print(win2)
    vit_elise += 1
    
jogadas += 1
time.sleep(0.5)
hist = input("Deseja ver o histórico de jogos? ")
if hist == s:
    print("Total de jogos: %d" % jogadas)
    print("Empates: %d" % empates)
    print("Suas vitórias: %d" % vit_player)
    print("Vitórias de Elise: %d" % vit_elise)

        

