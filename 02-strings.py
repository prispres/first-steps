texto = "Hola Mundo"
print(texto.upper())
print(texto.lower())
print(texto.find("M")) #caracter sensitive "M" "m"
print(texto.replace("Mundo", "pris")) 
nuevoTexto = texto.replace("Mundo", "pris")
print(texto, nuevoTexto)
print("Mundo" in texto)

"""
Metodos de strings
Las variables de texto pueden tener
metodos
Un metodo es una función incluida
en un objeto
Son las modificaciones que se le hicieron
a texto / upper lower find replace
"""