import random
#----------------------------------------------------------------------------------------#



# 1- numero TOTAL de vertices do grafo;
graph_lenght = 12 #add a graph lenght here;

# 2- numero de cores;
def generate_colors(total):
    colors = []
    while len(colors) < total:
        color = tuple(random.sample(range(256), 3))
        if color not in colors:
            colors.append(color)
    return colors

# 3- numero de vertices com cores repetidas;


# 4- tamanho do motif, soma de todas as vezes que uma cor aparece no motif:
    #exemplo: o motif tem 1 amarelo, 2 vermelhos e 1 azul, logo o tamanho do motif é 4;

# 5 - quantas cores tem no motif.
#----------------------------------------------------------------------------------------#

