import time
import random
import os

# Definice postav a jejich vlastností
postavy = [
    {"jméno": "Elf", "síla": 8, "magie": 12, "zručnost": 15, "zivoty": 25},
    {"jméno": "Válečník", "síla": 15, "magie": 4, "zručnost": 10, "zivoty": 31},
    {"jméno": "Kouzelník", "síla": 5, "magie": 20, "zručnost": 8, "zivoty": 27},
    {"jméno": "Průzkumník", "síla": 10, "magie": 6, "zručnost": 18, "zivoty": 26},
    {"jméno": "Nájemný vrah", "síla": 12, "magie": 8, "zručnost": 14, "zivoty": 26}
]

# Funkce pro získání náhodné místnosti
def ziskej_nahodnou_mistnost():
    mistnosti = [
        {"jméno": "Nepřítel", "zivoty": random.randint(1, 50), "odolnost_magii": random.randint(0, 20), "odolnost_zrucnosti": random.randint(0, 20),"sila": random.randint(0,20)},
        {"jméno": "Past", "minus_schopnosti": random.choice(["síla", "magie", "zručnost","zivoty"]), "minus_hodnota": random.randint(0, 7)},
        {"jméno": "Truhla", "bonus_schopnosti": random.choice(["síla", "magie", "zručnost","zivoty"]), "bonus_hodnota": random.randint(0, 7)},
        {"jméno": "Prázdná místnost"},
    ]
    return random.choice(mistnosti)

# Funkce pro útok hráče na nepřítele
def utoc_na_nepritele(postava, nepritel):
    postava_sila = postava['síla']
    postava_magie = postava['magie']
    postava_zrucnost = postava['zručnost']
    nepritel_zivoty = nepritel['zivoty']
    nepritel_odolnost_magii = nepritel['odolnost_magii']
    nepritel_odolnost_zrucnosti = nepritel['odolnost_zrucnosti']
    nepritel_sila = nepritel['sila']

    while postava['zivoty'] > 0 and nepritel_zivoty > 0:
        # Spočítejte bonus k síle na základě rozdílu odolností
        nepritel_bonus = max(0, nepritel_odolnost_magii - postava_magie) + max(0, nepritel_odolnost_zrucnosti - postava_zrucnost)
        bonus_sily = max(0, postava_magie - nepritel_odolnost_magii) + max(0, postava_zrucnost - nepritel_odolnost_zrucnosti)
        # Hráčův útok na nepřítele
        uder = random.randint(0, postava_sila + bonus_sily)
        nepritel_zivoty -= uder
        print("""-----------------------------------------------------------------------------------""")
        print(f"Udělili jste nepříteli {uder} poškození. Nepřítel má {nepritel_zivoty} životů.")
        time.sleep(2)
        
        if nepritel_zivoty <= 0:
            print("""-----------------------------------------------------------------------------------""")
            print(f"Tentokrát jste vyhrál {jmeno_postavy} a přežil.")
            time.sleep(2)
            break
        
        # Útok nepřítele na hráče
        uder_nepritele = random.randint(0, nepritel_bonus + nepritel_sila)
        postava['zivoty'] -= uder_nepritele
        print("""-----------------------------------------------------------------------------------""")
        print(f"Nepřítel vám způsobil {uder_nepritele} poškození. Máte {postava['zivoty']} životů.")
        time.sleep(2)
        
        if postava['zivoty'] <= 0:
            print("""-----------------------------------------------------------------------------------""")
            print(f"Snažíte se o rychlý nečekaný protiútok který by ještě mohl změnit výsledek ale je pozdě, umíráte{jmeno_postavy} . Hra končí.")
            input("Stisknete klávesu pro pokračování: ")
            return False
    input("Stisknete klávesu pro pokračování: ")
    print("""-----------------------------------------------------------------------------------""")
    return akce

# Výběr postavy a její vlastnosti
os.system('cls')
time.sleep(1)
print("""
---------------------------
Vítejte v hře!
---------------------------
""")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
zacatek = input("""
---------------------------                
Napiš "hrát" pro zapnutí hry:
---------------------------
""")
os.system('cls')

while zacatek != 'hrát':
    zacatek = input("""
---------------------------
Napiš 'hrát' pro zapnutí hry:
---------------------------
""")
    
print("""
--------------------------
Hra začíná    
--------------------------
""")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')

print("""
-------------------------
Vyber si postavu:
-------------------------
""")

for i, postava in enumerate(postavy, start=1):
    print(f"{i}) {postava['jméno']}")
    print(f"Síla: {postava['síla']}")
    print(f"Magie: {postava['magie']}")
    print(f"Zručnost: {postava['zručnost']}")
    print(f"Životy: {postava['zivoty']}")
    print("-------------------------")
    
while True:
    try:
        cislo = int(input("""
-------------------------
Zadejte číslo: """))

        if 1 <= cislo <= 5:
            break  # Výběr je v pořádku, ukonči smyčku
        else:
            print("Zadali jste číslo mimo povolený rozsah (1-5).")
    except ValueError:
        print("Zadali jste neplatné číslo. Zadejte prosím platné číslo (1-5).")

input("Stisknete klávesu pro pokračování: ")
os.system('cls')

print("""                      
-------------------------
Výborná volba
""")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')

jmeno_postavy = input("""
-------------------------
Zadejte jméno postavy: """)
time.sleep(1)
os.system('cls')
print(f"""
-------------------------
Jméno postavy: {jmeno_postavy}
-------------------------
Originální jméno
""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Avšak si nemůžete vybrat jak se narodíte""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Tak to nefunguje
""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
postava = random.choice(postavy)
print("""
-------------------------
Osud narození si nezvolíte ale můžete ovlivnit svoji cestu putování...
""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print(f"""
-------------------------
Narodili jste se jako {postava['jméno']}.
""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Už od mládí jste byly zvídavé dítě s touhou objevovat, která vám přetrvala až do teď
""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Tak jste se tu ocitl, před vstupem do tajemné legendárního podzemí které vám může přinést slávu a bohatství
""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Nebo smrt
""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Na krok zpátky už je pozdě, jste plně odhodlán ke vstupu
""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print(f"""
-------------------------
Jméno:{jmeno_postavy}
Síla: {postava['síla']}
Magie: {postava['magie']}
Zručnost: {postava['zručnost']}
Životy: {postava['zivoty']}
-------------------------
""")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Vstupujete do pozdemní s odhodlání a zvědavostí""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Ale to na co tam narazíte by vás nikdy nenapadlo""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
print("""
-------------------------
Jakmile se dostane do místnosti 25 vyhráli jste""")
print("-------------------------")
input("Stisknete klávesu pro pokračování: ")
os.system('cls')
misto = 1  # Počáteční místnost

while misto < 25:
    time.sleep(2)
    os.system('cls')  # Vyčistit obrazovku před zobrazením nové místnosti
    vybrana_mistnost = ziskej_nahodnou_mistnost()

    if vybrana_mistnost["jméno"] == "Nepřítel":
        print(f"V této místnosti je nepřítel s {vybrana_mistnost['zivoty']} životy")
        print(f"Sílou: {vybrana_mistnost['sila']}")
        print(f"Odolností proti magií: {vybrana_mistnost['odolnost_magii']}")
        print(f"Odolnosti proti zručnosti:{vybrana_mistnost['odolnost_zrucnosti']}")
        print("""--------------------------------------------------------------""")
        time.sleep(2)
        print(f"Vaše životy: {postava['zivoty']}")
        print(f"Vaše síla: {postava['síla']}")
        print(f"Vaše magie: {postava['magie']}")
        print(f"Vaše zručnost: {postava['zručnost']}")
        print("""--------------------------------------------------------------""")
        akce = input("Můžete zaútočit (Z) nebo utéct (jiné písmeno): ").upper()
        if akce == "Z":
            if utoc_na_nepritele(postava, vybrana_mistnost):
                print("Nepřítel byl poražen.")
                pruchod = input("Rozhodněte se, kterým směrem půjdete (doleva/doprava): ")
                time.sleep(1)
            else:
                break  # Hra končí, hráč zemřel
        else:
        # Hráč se pokouší utéct
            sance_na_utek = random.randint(1, 100)
            if sance_na_utek <= 25:
                print("Podařilo se vám utéct z místnosti.")
                print("""--------------------------------------------------------------""")
                pruchod = input("Rozhodněte se, kterým směrem půjdete (doleva/doprava): ")
                time.sleep(1)
            else:
                print("Bohužel, nezdařil se vám útěk, musíte bojovat.")
                time.sleep(1)
                if utoc_na_nepritele(postava, vybrana_mistnost):
                    print("Nepřítel byl poražen.")
                    pruchod = input("Rozhodněte se, kterým směrem půjdete (doleva/doprava): ")
                    time.sleep(1)
                else:
                    break  # Hra končí, hráč zemřel
            
    elif vybrana_mistnost["jméno"] == "Past":
        print(f"Upadli jste do pasti. Některé vaše vlastnosti budou sníženy.")
        print("""--------------------------------------------------------------""")
        vlastnost_ke_snizeni = vybrana_mistnost["minus_schopnosti"]
        minushodnota_bonus = vybrana_mistnost["minus_hodnota"]
        print(f"Původní {vlastnost_ke_snizeni} {postava[vlastnost_ke_snizeni]} ")
        postava[vlastnost_ke_snizeni] -= minushodnota_bonus
        print(f"Aktuální {vlastnost_ke_snizeni} {postava[vlastnost_ke_snizeni]}.")
        print("""--------------------------------------------------------------""")
        time.sleep(1)
        print(f"{jmeno_postavy} {postava['jméno']} ")
        print("""--------------------------------------------------------------""")
        print(f"Jste v místnosti číslo {misto}.")
        print(f"Vaše životy: {postava['zivoty']}")
        print(f"Vaše síla: {postava['síla']}")
        print(f"Vaše magie: {postava['magie']}")
        print(f"Vaše zručnost: {postava['zručnost']}")
        print("""--------------------------------------------------------------""")
        if postava['zivoty'] <= 0:
            break
        pruchod = input("Rozhodněte se, kterým směrem půjdete (doleva/doprava): ")
        time.sleep(1)
    elif vybrana_mistnost["jméno"] == "Truhla":
        print(f"Našli jste truhlu s předmětem který dává bonus vaším vlastnostem.")
        print("""--------------------------------------------------------------""")
        time.sleep(1)
        vlastnost_bonus = vybrana_mistnost["bonus_schopnosti"]
        hodnota_bonus = vybrana_mistnost["bonus_hodnota"]
        print(f"Původní {vlastnost_bonus} {postava[vlastnost_bonus]} ")
        postava[vlastnost_bonus] += hodnota_bonus
        print(f"Aktuální {vlastnost_bonus} {postava[vlastnost_bonus]}.")
        print("""--------------------------------------------------------------""")
        time.sleep(1)
        print(f"{jmeno_postavy} {postava['jméno']} ")
        print("""--------------------------------------------------------------""")
        print(f"Jste v místnosti číslo {misto}.")
        print(f"Vaše životy: {postava['zivoty']}")
        print(f"Vaše síla: {postava['síla']}")
        print(f"Vaše magie: {postava['magie']}")
        print(f"Vaše zručnost: {postava['zručnost']}")
        print("""--------------------------------------------------------------""")
        pruchod = input("Rozhodněte se, kterým směrem půjdete (doleva/doprava): ")
        time.sleep(1)
    elif vybrana_mistnost["jméno"] == "Prázdná místnost":
        print("Toto je prázdná místnost. Nebylo zde nic zajímavého.")
        print("""--------------------------------------------------------------""")
        time.sleep(1)
        print(f"{jmeno_postavy} {postava['jméno']} ")
        print("""--------------------------------------------------------------""")
        print(f"Jste v místnosti číslo {misto}.")
        print(f"Vaše životy: {postava['zivoty']}")
        print(f"Vaše síla: {postava['síla']}")
        print(f"Vaše magie: {postava['magie']}")
        print(f"Vaše zručnost: {postava['zručnost']}")
        print("""--------------------------------------------------------------""")
        pruchod = input("Rozhodněte se, kterým směrem půjdete (doleva/doprava): ")
        time.sleep(1)
    while pruchod.lower() != "doleva" and pruchod.lower() != "doprava":
        print("Neplatná volba. Zadejte prosím 'doleva' nebo 'doprava'.")
        print("""--------------------------------------------------------------""")
        pruchod = input("Rozhodněte se, kterým směrem půjdete (doleva/doprava): ")

    misto += 1
        

if misto >= 25:
    os.system('cls')
    print(f"Gratuluji {jmeno_postavy}, dorazili jste na konec dungeonu a získali magický předmět! Hra končí.")
    time.sleep(1)
    print("Vaše statistiky jsou:")
    print("""--------------------------------------------------------------""")
    time.sleep(1)
    print(f"Vaše životy: {postava['zivoty']}")
    print(f"Vaše síla: {postava['síla']}")
    print(f"Vaše magie: {postava['magie']}")
    print(f"Vaše zručnost: {postava['zručnost']}")
    input("Stisknete klávesu pro konce hry: ")

else:
    os.system('cls')
    print(f"Hra končí {jmeno_postavy}, nedostali jste se až na konec dungeonu.")
    time.sleep(1)
    print("""--------------------------------------------------------------""")
    print("Vaše statistiky jsou:")
    print("""--------------------------------------------------------------""")
    time.sleep(1)
    print(f"Vaše životy: {postava['zivoty']}")
    print(f"Vaše síla: {postava['síla']}")
    print(f"Vaše magie: {postava['magie']}")
    print(f"Vaše zručnost: {postava['zručnost']}")
    input("Stisknete klávesu pro konce hry: ")