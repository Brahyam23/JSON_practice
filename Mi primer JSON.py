import json

##Escritura
data = {"usuarios": [{"usuario": "leonel", "edad": "24"}, {"usuario": "maria", "edad": "21"}, {"usuario": "soledad", "edad": "31"}]}

ruta = r"D:\Multimedia\Documents\Python's works\VSC\Archivos"

archivo = open(ruta + r"/usuarios.json", "w" )

json.dump(data, archivo, indent=2)

archivo.close()

##Lectura
archivo = open(ruta + r"/usuarios.json", "r")

data = json.load(archivo)

print(data["usuarios"][1]["usuario"]) #Parecido al ejercicio de dict

archivo.close()