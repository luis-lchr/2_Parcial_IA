from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt


adj_list = {}

# Abre el archivo "grafo.txt" en modo lectura y lee su contenido línea por línea. 
# Para cada línea, divide la línea en partes, donde la primera parte es el nodo y 
# las partes restantes son los nodos adyacentes. Luego, almacena esta información 
# en el diccionario adj_list como una representación de lista de adyacencia. 
with open("grafo.txt", "r") as file:
    for line in file:
        parts = line.split()
        node = parts[0]
        neighbors = parts[1:]
        adj_list[node] = neighbors

# Se inicializan varios diccionarios y listas que se utilizarán en el recorrido BFS y DFS. 
# Estos diccionarios y listas se utilizan para realizar un seguimiento de los nodos visitados, 
# niveles en BFS, padres de nodos y resultados de recorridos.
visited = {}
level = {}
parent = {}
bfs_output = []
queue = Queue()

color = {}
parent = {}
dfs_output= []

# Se recorren todos los nodos del grafo y se inicializan los diccionarios visited, parent y level 
# para el recorrido BFS.
for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1 

# Se recorren todos los nodos del grafo y se inicializan los diccionarios color y parent para el 
# recorrido DFS.
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None

# Se inicializan diccionarios y listas para llevar un seguimiento de nodos visitados y el recorrido DFS. 
# El usuario ingresa un nodo inicial desde el cual comenzará el recorrido. Se verifica si el nodo inicial 
# ingresado existe en el grafo. Si no existe, se muestra un mensaje de error. Si existe, se continúa con 
# el recorrido. La función dfs_util(u) se llama con el nodo inicial u. Dentro de dfs_util(u), se marca 
# el nodo u como "G" (visitado y en proceso) y se agrega a la lista dfs_output. Luego, se exploran
#  los nodos adyacentes a u. Si un nodo adyacente v no ha sido visitado (marcado como "W"), se llama 
# recursivamente a dfs_util(v) desde u. Una vez que se han explorado todos los nodos adyacentes, el nodo u se
#  marca como "B" (visitado y completado). El proceso de exploración en profundidad continúa desde otros 
# nodos no visitados si los hay.
def dfs_util(u):
    color[u] = "G"
    dfs_output.append(u)

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"


# Se solicita  el nodo inicial desde el cual se realizarán los recorridos BFS y DFS.
s = input("Ingrese el nodo inicial: ")

# Se verifica si el nodo ingresado existe en el grafo. Si no existe, se muestra un mensaje de error. 
# Si existe, se procede con los recorridos.
if s not in adj_list:
    print("El nodo ingresado no existe en la lista de adyacencia.")
else:
    visited[s] = True       
    level[s] = 0            
    queue.put(s)            
    #Se inicializa una cola vacía queue para almacenar los nodos a visitar y se inicializan varios diccionarios 
    # y listas para llevar un seguimiento del proceso.El usuario ingresa un nodo inicial desde el cual comenzará 
    # el recorrido.Se verifica si el nodo inicial ingresado existe en el grafo. Si no existe, se muestra un mensaje 
    # de error. Si existe, se continúa con el recorrido.El nodo inicial se marca como visitado y se agrega a la 
    # cola.El ciclo principal comienza mientras la cola no esté vacía. En cada iteración del ciclo, se toma un nodo 
    # de la cola (u), se agrega a la lista bfs_output y se exploran sus nodos adyacentes.Para cada nodo 
    # adyacente (v), se verifica si ya ha sido visitado. Si no ha sido visitado, se marca como visitado, se establece 
    # el padre de v como u y se aumenta el nivel de v en uno con respecto al nivel de u.Se repite el proceso hasta 
    # que la cola esté vacía. Como resultado, bfs_output contendrá el orden en el que se visitaron los 
    # nodos desde el nodo inicial, siguiendo un patrón de exploración en anchura.
    while not queue.empty():
        u = queue.get()
        bfs_output.append(u)

        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.put(v)
    dfs_util(s) #Se llama a la función dfs_util(s) para realizar el recorrido DFS desde el nodo inicial ingresado, y los resultados se almacenan en dfs_output.
    print("Recorrido BFS desde el nodo inicial:", s)
    print(bfs_output)
    print("Recorrido DFS desde el nodo inicial:", s)
    print(dfs_output)

# Crear un grafo
G = nx.Graph()  

# Se carga el grafo desde el archivo "grafo.txt" utilizando la representación de lista de adyacencia 
# y se crea un diseño (layout) para el grafo utilizando spring_layout
with open("grafo.txt", "r") as file:
    for line in file:
        nodes = line.strip().split()
        if nodes:
            source = nodes[0]
            for target in nodes[1:]:
                G.add_edge(source, target)

# Dibujar el grafo
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
plt.title("Representación del Grafo")
plt.show()