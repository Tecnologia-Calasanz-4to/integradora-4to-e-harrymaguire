nom = str(input("Ingrese nombre"))
nivel= int(input("ingrese nivel"))
arma =

# ===== PARTE A =====
def nombre_valido(nom):
    
    return len(nom) >= 2 and nom.isalpha()
def crear_codename(nom, nivel):
    cn = nom[0: 3] + "-Lv" + int(nivel)
    return cn    # TODO: nombre[0:3].upper() + "-Lv" + str(nivel)
def vida_maxima(nivel):
    VM = 100 + nivel ** 2 * 5
    return VM    # TODO: 100 + nivel ** 2 * 5

# ===== PARTE B =====
def clasificar_arma(poder):
    if arma == legendaria:
        d
    elif arma == media:
        d
    elif arma == debil:
        d
    else:
        print("Error")
    return    # TODO: if/elif/else -> "Legendaria"/"Media"/"Debil"
def es_critico(es_magica, nivel):
    if arma == es_magica or nivel >= 10:
        
    return    # TODO: es_magica or nivel >= 10
def dano_base(ataque, poder, defensa):
    db = (ataque + poder) - defensa
    return db    # TODO: (ataque + poder) - defensa
def dano_total(ataque, poder, defensa, critico):
    if dano_base() * 2:
        d
    else:
        d
    
    return    # TODO: si critico -> dano_base(...) * 2 ; si no -> dano_base(...)

# ===== PARTE C =====
def porcentaje_vida(actual, maxima):
    pass    # TODO: actual / maxima * 100
def estado_vida(porcentaje):
    pass    # TODO: if/elif/else -> "CRITICO"/"HERIDO"/"SANO"
def comprar_pociones(monedas, precio):
    pass    # TODO: monedas // precio  y  monedas % precio

# ===== PARTE D =====
def puede_atacar(energia, esta_aturdido):
    pass    # TODO: energia > 0 and not esta_aturdido
def vida_restante(vida, dano):
    pass    # TODO: si vida - dano < 0 -> 0 ; si no -> vida - dano
def gana(vida_heroe, vida_enemigo):
    pass    # TODO: vida_heroe > 0 and vida_enemigo <= 0

# ===== PROGRAMA PRINCIPAL=====
# TODO: pedir nombre y nivel, validar, crear el heroe.
# TODO: elegir dificultad del enemigo con if/else.
# TODO: turno 1, turno 2 y resultado final.

    
    
