#Parte 1
def nombre_valido(nombre):
    return len(nombre)>=2 and nombre.isalpha()
    
def crear_codename(nombre, nivel):
    return nombre[0:3].upper()+str(int(nivel))

def vida_maxima(nivel):
    vida= 100+nivel**2*5
    return vida 

#Parte 2
def clasificar_arma(poder):
    if poder >= 1000:
        return "legendaria"
    elif poder<1000 or poder>=500:
        return "media"
    elif poder<500:
        return "debil"
    
def es_critico(es_magica, nivel):
    if es_magica or nivel >= 10:
        return True
    else:
        return False
    
def dano_base(ataque, poder, defensa):
        return  (ataque + poder) - defensa

def dano_total(ataque, poder, defensa, critico):
    if critico==True:
        return dano_base(ataque, poder, defensa) * 2
    else:
        return dano_base(ataque, poder, defensa)
    
#Parte 3
def porcentaje_vida(actual, maxima):    
    porc= actual / maxima *100
    return porcentaje

def estado_vida(porcentaje):
    if porc<=25:
        return "critico"
    elif porc<= 50:
        return "herido"
    else:
        return "Sano"
    
def comprar_pociones(monedas, precio):
    cantidad= monedas//precio
    vuelto= monedas%precio
    return cantidad,vuelto
    
#Parte 4 
def puede_atacar(energia, esta_aturdido):
    if energia > 0 and esta_aturdido == false:
        return True
  
def vida_restante(vida, daño):
    vida_heroe = vida - daño
    if vida_heroe <= 0:
        print("Moriste")
    return vida_heroe

def gana(vida_heroe, vida_enemigo):
    if vida_heroe > vida_enemigo:
        return True



nombre = str(input("Ingrese el nombre"))
nivel = int(input("Ingrese el nivel"))


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
        nombre_enemigo = "Dragon"
        nivel_enemigo = 20
        ataque_enemigo = 120
        poder_enemigo = 900
        defensa_enemigo = 80
        vida_enemigo = 100000
else:
        nombre_enemigo = "Maguire"
        nivel_enemigo = 8
        ataque_enemigo = 40
        poder_enemigo = 250
        defensa_enemigo = 20
        vida_enemigo = 25000

print("Enemigo:", nombre_enemigo)
print("Nivel:", nivel_enemigo)
print("Vida:", vida_enemigo)

critico = es_critico(False, nivel)

dano = dano_total(ataque_enemigo, defensa_enemigo, poder_enemigo, critico)

vida_r_enemigo = vida_restante(vida_enemigo, dano)

print("Vida restante del enemigo:", vida_r_enemigo)

if gana(vida_m, vida_r_enemigo):
    print("Ganaste")
else:
    print("El enemigo sigue vivo")
print(codename)
