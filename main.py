# Catbots par skolas vesturi


def izglitibas_programmas():
    # saruna par V2V izglitibas programmam
    print("programmas coming soon!")


def direktori():
    # saruna par V2V direktoriem
    print("direktori coming soon!")



def tradicijas():
    # saruna par skolas tradicijam
    print("tradicijas coming soon!")



def eka():
    # saruna par eku
    print("ekas coming soon!")



def izvelne(vards):
    print(vards + " izvēlies par ko gribi uzzināt? Izvēlies un ievadi vērtību ")
    x = input( "1 - Izglitibas programmas\n2-Direktori \n3-Tradicijas\n4-Skolas ēka")
    lietotaja_izvele = int(x)
    if lietotaja_izvele == 1:
        izglitibas_programmas()
    if lietotaja_izvele == 2:
        direktori()
    if lietotaja_izvele == 3:
        tradicijas()
    if lietotaja_izvele == 4:
        eka()
    else:
        exit(0)


def sasveicinaties(vards):
    return print("Sveiki, " + vards)


if __name__ == '__mai' \
               'n__':
    print("Sveiki, es esmu V2V catbots Pēterītis! Es Tev pastāstīšu vairāk par šo skolu")
    vards = input("Kā sauc Tevi?")
    sasveicinaties(vards)
    izvelne(vards)

