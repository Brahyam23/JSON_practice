ruta = r"D:\Multimedia\Documents\Python's works\VSC\Archivos"


archivo = open(ruta + r"\Mi Mascota.txt", "w")

mascota= {}

mascota["nombre"] = input("Introduce el nombre de tu mascota: ")
mascota["clase"] = input("Que animal es?: ")
mascota["edad"] = input("Cuantos años tiene?: ")

archivo.write (mascota["nombre"] +"\n"+ mascota["clase"] +"\n"+ str(mascota["edad"]))

archivo.close()