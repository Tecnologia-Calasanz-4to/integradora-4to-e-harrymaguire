#Parte 1
def nombre_valido(nombre):
    if len(nombre)>=2 and nombre.isalpha():
        return True
    
def crear_codename(nombre, nivel):
    nombre[0:3].upper()+str(nivel)
    return True

def vida_maxima(nivel):
    vida= 100+nivel**2*5
    return vida 

#Parte 2
#Parte 3
#Parte 4 
def puede_atacar(energia, esta_aturdido):
    if energia > 0 and esta_aturdido == false:
        return True
  
def vida_restante(vida, daño):
    vida_r = vida - daño
    if vida_r <= 0:
        print("Moriste")
    return vida_heroe

def gana(vida_heroe, vida_enemigo):
    if vida_heroe > vida_enemigo:
        return True

nombre = str(input("Ingrese el nombre"))
nivel = float(input("Ingrese el nivel"))


if nombre_valido(nombre):
    nom = nombre
else:
    nom = "Invitado"

nom = nombre.capitalize()

codename = crear_codename(nombre, nivel)

vida_m = vida_maxima(nivel)

print("Elija la dificultad")
print("1. Difìcil")
print("2. Fàcil")
dif = int(input("ingrese la dificultad"))

if dif == 1:
    print("1")    

    
    
print(codename + clasificacion_arma)
