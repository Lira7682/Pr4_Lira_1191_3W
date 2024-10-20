print(" ")#espacio a agregar
print("Lira Hernandez Dayana 1191 3W")#datos del realizador
print(" ")#espacio a agregar
#inicio del diccionario
thisdict = {  
    "hola": "hello", #palabra a traducir
    "adios": "goodbye", #palabra a traducir
    "gracias": "thanks", #palabra a traducir
    "zapato": "shoe", #palabra a traducir
    "silla": "chair", #palabra a traducir
    "ventana": "window" #palabra a traducir
}#cierre de diccionario
#solicita al usuario ingresar una palabra
palabra = input("ingresa la palabra en español")
resultado = [] 
for palabra in palabra.split():
#si la palabra esta en el diccionario traducir si no dejarla sin traducir
    if palabra in thisdict:
        resultado.append(thisdict[palabra])
    else:
        resultado.append(palabra)#dejar la palabra sin traducir
print("la traduccion es:", " ".join(resultado))
#traduccion a mostrar
print(" ")#espacio a agregar