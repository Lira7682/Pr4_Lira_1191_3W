print(" ")#espacio a agregar
print("Lira Hernandez Dayana 1191 3W")#datos del realizador
print(" ")#espacio a agregar
# Solicitar información de una persona
mensaje = input("ingresa nombre de la persona:")
mensaje1 = input("ingresa edad de la persona:")
mensaje2 = input ("ingresa sexo de la persona:")
mensaje3 = input("ingresa telefono de la persona:")
mensaje4 = input ("ingresa correo de la persona:")
# Crear un diccionario para almacenar los datos ingresados
Datos = {
"nombre :" : mensaje,
"edad :" : mensaje1,
"sexo :" : mensaje2,
"telefono :" : mensaje3,
"correo :" : mensaje4
}
# Imprimir los datos ingresados
for x, y in Datos.items():
  print(x, y)
print(" ")#espacio a agregar