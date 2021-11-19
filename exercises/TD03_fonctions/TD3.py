#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    x = temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3]
    return x

"""temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))"""

def secondeEnTemps(seconde):
    temps = []
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    a = seconde // 86400
    reste = seconde % 86400     
    #temps.append(a)
    
    b = reste // 3600
    reste = reste % 3600
    #temps.append(b)

    c = reste // 60
    reste = reste % 60
    #temps.append(c)

    #temps.append(reste) 
    elements = (a,b,c,reste)
    return (elements)



"""temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")"""

#fonction auxiliaire ici

def afficheTemps(temps):
    if temps[0] > 1:
        print(temps[0], "jours ", end="")
    elif temps[0] == 1:
        print(temps[0], "jour ", end="")
    else:
        print(" ", end="")

    if temps[1] > 1:
        print(temps[1], "heures ", end="")
    elif temps[1] == 1:
        print(temps[1], "heures ", end="")
    else:
        print(" ", end="")

    if temps[2] > 1:
        print(temps[2], "minutes ", end="")
    elif temps[2] == 1:
        print(temps[2], "minute ", end="")
    else:
        print(" ", end="")

    if temps[3] > 1:
        print(temps[3], "secondes", end="")
    elif temps[3] == 1:
        print(temps[3], "secondes", end="")
    else:
        print(" ", end="")
    
"""afficheTemps((1,0,14,23))"""

def demandeTemps():
    temps2=[]
    a=int(input("Entrer le nombre de jours"))
    temps2.append(a)

    b=int(input("Entrer le nombre d'heures"))
    while b >= 24:
        b=int(input("ERREUR ! Entrer un nombre d'heures valable"))
    else :
        temps2.append(b)

    c=int(input("Entrer le nombre de minutes"))
    while c >= 60:
        c=int(input("ERREUR ! Entrer un nombre de minutes valable"))
    else :
        temps2.append(c)

    d=int(input("Entrer le nombre de secondes"))
    while d >= 60:
        d=int(input("ERREUR ! Entrer un nombre de seconde valable"))
    else :
        temps2.append(d)

    return temps2

"""afficheTemps(demandeTemps())"""


"""def sommeTemps(temps1,temps2):
   temps1=[2,3,4,25]
    temps2=[3,22,57,1]
    sommeTemps=[]

    jour = temps1[0] + temps2[0]
    heure = temps1[1] + temps2[1] 
    min = temps1[2] + temps2[2]
    sec = temps1[3] + temps2[3]

    while sec >= 60:
        sec -= 60
        min += 1

    while min >= 60:
        min -=60
        heure += 1
    
    while heure >= 24:
        heure -= 24
        jour += 1

    sommeTemps.append(jour)
    sommeTemps.append(heure)
    sommeTemps.append(min)
    sommeTemps.append(sec)

    print sommeTemps()

sommeTemps((2,3,4,25),(5,22,57,1))"""

def sommeTemps(temps1,temps2):
    conversion1 = tempsEnSeconde(temps1)
    conversion2 = tempsEnSeconde(temps2)
    somme = conversion1 + conversion2
    temps_final = secondeEnTemps(somme)
"""sommeTemps((2,3,4,25),(5,22,57,1))"""


def proportionTemps(temps,proportion):
    a = tempsEnSeconde(temps)
    seconde = a * proportion
    b = secondeEnTemps(seconde)
    return b
"""afficheTemps(proportionTemps((2,0,36,0),0.2))"""
#appeler la fonction en échangeant l'ordre des arguments (flemme)

def tempsEnDate(temps):
    tempsC = tempsEnSeconde(temps)

    i = tempsC // 31536000
    reste = tempsC % 31536000 

    a = reste // 86400
    reste = reste % 86400     
    
    b = reste // 3600
    reste = reste % 3600

    c = reste // 60
    reste = reste % 60

    elements = (a,b,c,reste)
    return (elements)

def afficheDate(date = -1):
    if temps[0]==0:
        print("",end="")
    elif temps[0]==1:
        print(temps[0]+1970,"année", end="")
    else:
        print(temps[0]+1970, "années", end="")

    if temps[1]==0:
        print("",end="")
    elif temps[1]==1:
        print(temps[1],"jour", end="")
    else:
        print(temps[1],"jours", end="")

    if temps[2]==0:
        print("",end="")
    elif temps[2]==1:
        print(temps[2],"heure", end="")
    else:
        print(temps[1],"heures", end="")

    if temps[3]==0:
        print("",end="")
    elif temps[3]==1:
        print(temps[3],"minute", end="")
    else:
        print(temps[1],"minutes", end="")

    if temps[4]==0:
        print("",end="")
    elif temps[4]==1:
        print(temps[4],"seconde", end="")
    else:
        print(temps[4],"secondes", end="")
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

#PAAS FINIIIII
