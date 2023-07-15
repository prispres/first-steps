lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
lenguajes.insert(3, "Go")
lenguajes.insert(0, "C")
lenguajes.remove("Ruby")  #para eliminar ocupa el valor no el indice de la variable
print("PHP" in lenguajes) #preguntar por elementos en el listado
# lenguajes.clear() //elimina el contenido de la lista


print(len(lenguajes))