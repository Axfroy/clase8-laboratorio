import numpy as np 
import os 
os.system ("cls")
# # a = np.array([[1,2,3],[4,5,6]])
# # print (a)


# # b = np.zeros((3,4))
# # print (b)


# # c = np.ones((2,3))
# # print(c)

# # d = np.eye(4)
# # print(d)

# # e = np.random.random((3,2))
# # print(e)

# # f = np.random.randint(0,10, size =(2,3))
# # print(f)

# # g = np. linspace(0,1,5)
# # print (g)

# # h = np.array([[1,2,3],[4,5,6]])
# # i = np.transpose(h)
# # print (i)

# # lista  =([[1,2,3],[4,5,6],[7,8,9]])
# # a = np.array(lista)
# # print (a[0])

# # b = np.arange(20).reshape((4,5))
# # print (b)

# # arr_vacio = np.empty((2,3))
# # print("arrray vacio:\n",arr_vacio)
# # arr_ceros = np.zeros ((2,3))
# # print("arrray ceros:\n",arr_ceros)

# # arr_unos = np.ones((2,3))
# # print ("arrray unos:\n",arr_unos)

# # arr_sietes = np.full((2,3),7)
# # print("arrray sietes:\n",arr_sietes)

# # mat_identidad = np.identity(3)
# # print ("mat identidad:\n",mat_identidad)

# # arr_secuencia = np.arange(10)
# # print("arrray secuancia:\n",arr_secuencia)

# # arr_salteado = np.arange(2,11,2)
# # print ("arrray salteado:\n",arr_salteado)

# # arr_espaciado = np.linspace(0,1,5)
# # print("arrray espaciado:\n",arr_espaciado)

# # arr_aleatorio = np.random.random((2,3))
# # print("arrray aleatorio:\n",arr_aleatorio)

# "hacer una matriz de una sola fila, llenarla con datos aleatorios"

# a = np.array([7,8,2,1,9,3,4,23,23])
# print(np.sort(a))

# unicos = []
# for n in a:
#     if n not in unicos:
#         unicos.append(n)

# print (unicos)
# unicos = np.array (unicos)
# unicos=np.sort(unicos)

# print (unicos[-2])

# # potencia
# print(np.power(unicos,3))
# print(np.array(unicos.min()))

# lista=[78,5,1,3,9,4,6,7,8,2,1,9,7,4]
# matriz = np.array([[1,2],[4,5]])
# matrizb = np.array([[10,11],[7,8]])

# # print(np.concatenate((lista, matriz)))

# # print (np.add(lista, matriz))
# # print (lista+matriz)
# # print (np.subtract(lista, matriz))
# # print (np.multiply(lista, matriz))
# # print (np.divide(lista, matriz))

# print(matriz.dot(matrizb))

# blyat = np.random.choice([100,200])
# print (blyat)

# blyat = np.random.choice(([100,200]),size= 4)
# print (blyat)

"hacer un adivinanumeros"
matriz = np.array([1,2,3,4,5,6,7,8,9,10])
numero_random = np.random.choice(matriz)
print(numero_random)
numero_correcto = False

def ingresarNumero():
    return int(input("Ingrese un número del 1 al 10 "))
    
# if(ingresarNumero() == numero_random):
#     numero_correcto = True
#     print(f'Acertaste, el número correcto era: {numero_random}')
# elif numero_correcto == False:
#     ingresarNumero()

    
while numero_correcto == False:
    if(ingresarNumero() == numero_random):
        numero_correcto = True
        print(f'Acertaste! el número correcto era: {numero_random}')
    else:
        print("Número incorrecto, vuelva a ingresar un número")
        ingresarNumero()