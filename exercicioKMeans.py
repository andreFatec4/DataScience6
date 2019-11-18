import random
from matplotlib import pyplot as plt

# 1. Implemente a seguinte função. Ela deve devolver uma lista de comprimento n que contém
# tuplas no formato (x, y) com x , y∈ℤ . Cada tupla representa a localização da residência de
# um funcionário da DataSciescenter. x representa a quantidade de quarteirões ao norte e y
# representa a quantidade de quarteirões ao leste em relação ao centro da cidade, da residência de
# um funcionário. A função deve gerar uma lista com as seguintes restrições.

def gera_base (n):
    lista = []
    i = 1
    while i <= n:
        # 1.1 Para o primeiro terço da lista: -50 <= x <= -40 e 0 <= y <= 10.
        # Alterei para uma lista: -50 <= x <= -25 e 10 <= y <= 20.
        if (i <= n/3):
            q_norte = random.randint(-50, -25) 
            q_leste = random.randint(10, 20) 
            tupla = (q_norte, q_leste)
            lista.append(tupla)
            i += 1
        # 1.2 Para o segundo terço da lista: -45 <= x <= -35 e 5 <= y <= 20.
        # Alterei para uma lista: -20 <= x <= 15 e 5 <= y <= 15.
        elif (i <= (2*n)/3):
            q_norte = random.randint(-20, 15) 
            q_leste = random.randint(5, 15) 
            lista.append((q_norte, q_leste))
            i += 1
        # 1.3 Para o último terço da lista: 20 <= x <= 30 e 20 <= y <= 30.
        else:
            q_norte = random.randint(20, 30) 
            q_leste = random.randint(20, 30)  
            lista.append((q_norte, q_leste))
            i += 1
    #print (lista)
    return lista

# 2. Implemente a seguinte função. Ela recebe uma lista tal qual aquela gerada pela função do
# exercício 1 e exibe, usando um gráfico de dispersão (scatter), os pontos em um plano. Cada terço
# deve ser exibido com uma cor e símbolo diferente, já que cada um deles representa uma vizinhança diferente.
def exibe_grafico ():
    lista = gera_base(21)
    #print (lista)
    l1_1 = lista[:7]  
    l1 = [i[0] for i in l1_1]
    l2 = [i[1] for i in l1_1]
    plt.scatter (l1, l2, marker='^')
    l1_2 = lista[7:14]  
    l1 = [i[0] for i in l1_2]
    l2 = [i[1] for i in l1_2]
    plt.scatter (l1, l2, marker='o')
    l1_3 = lista[14:]  
    l1 = [i[0] for i in l1_3]
    l2 = [i[1] for i in l1_3]
    plt.scatter (l1, l2, marker='*')
    plt.title ("Vizinhança da Cidade")
    plt.xlabel ("Quarteirões à leste")
    plt.ylabel ("Quarteirôes ao norte")
    plt.show()

# 3. Implemente a seguinte função. Trata-se de uma adaptação da função do exercício 2. Ela deve
# executar o algoritmo KMeans a fim de obter os representantes de cada grupo. Use k=3. Ao final,
# ela deve exibir todos os elementos da base em um gráfico de dispersão, bem como os
# representantes de cada um deles obtidos pelo KMeans. Os representantes devem ser exibidos
# com o símbolo “+”.
#def exibe_grafico_e_representantes (base):



# 4 (Desafio, entrega não obrigatória) Para cada grupo obtido, desenhe um círculo com centro no
# seu representante e cujo raio seja suficiente para englobar todas as suas instâncias.

def main():
    #gera_base(12)
    exibe_grafico ()
main()