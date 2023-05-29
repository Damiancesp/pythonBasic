lista = [50, "Mensaje" , 3.1415,[1,2,3]]

print(lista[3])

a = [90, "Python", 3.87]
print(a[-1])

lista = [1,2]
lista.append(3)
print(lista) #[1,2, 3]

lista = [1, 2]
lista.extend([3, 4])
print(lista) #[1,2,3, 4]

lista = [1,3]
lista.insert(1, 2)
print(lista) #[3,2, 1]

lista = [1,5,25,100,500]
print(lista)

#Append()= Agregar un dato al final de la lista
lista = [1,5,25,100,500]
print("inicial: ",lista)
lista.append(250)
print("Appened: ",lista)

#Extend()= Permite añadir una segunda lista a una lista inicial
lista2 = [75,125]
lista.extend(lista2)
print("extend: ",lista)

#Insert()= Permite añadir un dato en una posicion determinado
lista.insert(2,400)
print("insert: ",lista)

#Remove()= Permite recibir como argumento un objeto y lo borra de la lista
lista.remove(400)
print("remove: ",lista)

#Pop()= Elimina el ultimo elemento de la lista 
lista.pop()
print("pop: ",lista)

#Pop Posicion()= Elimina el elemento que se encuentra en la posicion ingresada
lista.pop(2)
print("pop(2): ",lista)

#Reverse()= Permite invertir el orden de la lista
lista.reverse()
print("reverse: ",lista)

#Sort()= Permite ordenar la lista de menor a mayor
lista.sort()
print("sort:    ",lista)

#Sort()= Permite ordenar la lista de mayor a menor (Colocando = reverse=true)
lista.sort(reverse=True)
print("sort(r): ",lista)





