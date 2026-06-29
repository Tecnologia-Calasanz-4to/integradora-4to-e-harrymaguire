def clasificar_arma(poder):
    if poder>1000 or poder==1000:
        return "legendaria"
    elif poder<1000 or poder>=500:
        return "media"
    elif poder<500:
        return "debil"
    
def es_critico(es_magica, nivel):
    if es_magica or nivel >= 10:
        return "true"
    else:
        return "false"
    
def dano_base(ataque, poder, defensa):
        return  (ataque + poder) - defensa

def dano_total(ataque, poder, defensa, critico):
    if critico==True:
        return dano_base(ataque, poder, defensa) * 2
    else:
        return dano_base(ataque, poder, defensa)
