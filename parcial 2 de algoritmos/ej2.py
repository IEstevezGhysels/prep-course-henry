#metodo burbuja
lista=[9, 3, 4, 8, 1,]
for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if lista[j]>lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux
print(lista)
#burbuja mejorado
lista2=[9, 3, 4, 8, 1,]
band=1
j=0
while(band==1):
    band=0
    for l in range(len(lista)-1):
        if lista[l]>lista[l+1]:
            aux=lista[l]
            lista[l]=lista[l+1]
            lista[l+1]=aux
            band=1
    j+=1
print(lista)
#metodo de seleccion:
#Consiste en recorrer una lista, tomando el primer elemento y compararlo contra el resto. Si el elemento es mayor, 
#cambiarlo de lugar. De esta manera, al finalizar el proceso, el menor quedará colocado en el lugar que le corresponde​

# Lista de ejemplo
lista = [9, 3, 4, 8, 1]
print("Lista original:", lista)

# Implementación del método de selección
n = len(lista)

# Recorremos toda la lista
for i in range(n):
    # Suponemos que el primer elemento no ordenado es el menor
    min_index = i
    
    # Buscamos el menor elemento en la sublista no ordenada
    for j in range(i + 1, n):
        if lista[j] < lista[min_index]:
            min_index = j
            
    # Intercambiamos el elemento encontrado con el primer elemento no ordenado
    lista[i], lista[min_index] = lista[min_index], lista[i]

print("Lista ordenada:", lista)


# Lista de ejemplo metodo de insercion
lista = [9, 3, 4, 8, 1]
print("Lista original:", lista)

# Implementación del método de inserción
for i in range(1, len(lista)):
    key = lista[i]
    j = i - 1
    
    # Mover los elementos de lista[0..i-1], que son mayores que la clave,
    # una posición adelante de su posición actual
    while j >= 0 and key < lista[j]:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = key

print("Lista ordenada:", lista)

#separar en digitos
lista=[]
a=1845
while a>=0:
    lista.append(a%10)
    a=a//10
    if a==0:
        break
print(lista)

def busqueda_binaria_interactiva(lista):
    """
    Realiza una búsqueda binaria en una lista ordenada. Si el número no está en la lista,
    solicita al usuario que ingrese otro número hasta que el número ingresado esté en la lista.

    Parámetros:
    lista (list): La lista ordenada donde se realizará la búsqueda.

    Retorna:
    int: El índice del elemento si se encuentra en la lista.
    """
    while True:
        objetivo = int(input("Ingresa el número que deseas buscar en la lista: "))
        
        izquierda, derecha = 0, len(lista) - 1
        
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            valor_medio = lista[medio]
            
            if valor_medio == objetivo:
                return medio
            elif valor_medio < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        
        print(f"El número {objetivo} no está en la lista. Inténtalo de nuevo.")

# Ejemplo de uso
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

indice = busqueda_binaria_interactiva(lista_ordenada)
print(f"El número se encuentra en el índice {indice}.")
