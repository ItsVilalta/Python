"""                   """
#   Arnau Vilalta Puig  #
"""                   """

from prettytable import PrettyTable

import os

from colorama import Fore
    
# VARIABLES PER FER EL CODI MACO
sep = "=================="
sep2 = "========================"

fitxer = "agenda.txt"

OPCIONS_MENU = {1: "Alta", 2: "Llistat", 3: "Modificar", 4: "Baixa", 5: "Sortir"}

################################################################
"""                    FUNCIONS EXTRES CODI                  """


def neteja_pantalla() -> None:
    """Neteja la pantalla."""
    os.system("cls") if os.name == "nt" else os.system("clear")


def enter():
    """Enter per poder veure els resultats"""
    input("Prem enter per continuar...")


################################################################
"""              FUNCIONS COMPROVACIONS INPUTS               """


def input_int(text_input: str, *valors):
    """Funcionalitat: accepta el text de l'input, un valor mínim i un valor
    màxim, i demana un input a l'usuari, assegurant que és un sencer entre el
    valor mínim i el màxim, si el mínim i el màxim no s'han definit no els té en
    compte (pensa com fer-ho). Retorna aquest sencer."""

    # Valida el numero introduit. Si insereixes una lletra et fa repetir el input, i si insereixes el numero fora
    # del rang assignat tambe t'ho fa repetir

    num_valid = False
    while not num_valid:
        numero = input(text_input)
        try:
            numero = int(numero)

        except ValueError:

            print(f"\n {Fore.RED}El valor ha de ser un número enter.\n{Fore.RESET}")

        else:
            # Si valors te exactament dos valors, s'aplica el mínim i el máxim.
            if len(valors) == 2:
                minim = valors[0]
                maxim = valors[1]

                if numero in range(minim, maxim + 1):
                    num_valid = True

                else:

                    print(
                        f"\n {Fore.RED}El número ha de estar entre {minim} i {maxim}.\n{Fore.RESET}"
                    )

            else:
                num_valid = True

    return numero


def input_str(text_input2: str):

    """Valida que el que has inserit es una cadena de caracters, si no et fa repetir el input"""

    str_valid = False
    while not str_valid:

        cadena = input(text_input2)

        if cadena.isalpha():
            str_valid = True

        else:
            print(f"\n {Fore.RED}Has d'introduir una cadena de Caracters\n{Fore.RESET}")

            str_valid = False

    return cadena


def input_tele(input_tele: str):

    """Comprova que el Telegram que introdueixes començi amb '@', si no es aixi et fa repetir el imput."""

    str_valid = False
    while not str_valid:

        tele = input(input_tele)

        try:

            if input_tele != "":

                if tele[0] == "@":
                    str_valid = True
                else:
                    print(f"\n {Fore.RED}Has d'introduirt un @Telegram Incorrecte")
                    print(f"\n {Fore.BLUE}Ha de començar per '@'{Fore.RESET}")
                    str_valid = False

        except:
            print(f"\n {Fore.RED}Has d'introduirt un @Telegram Incorrecte")
            print(f"\n {Fore.BLUE}Ha de començar per '@'{Fore.RESET}")
            str_valid = False

    return tele


def input_email(email: str):

    """Verifica que el email introduit sigui correcte, si no es aixi, et fa repetir el input"""

    email_valid = False

    while not email_valid:

        email2 = input(email)

        try:

            usuari, domini = email2.split("@")
            parts_domini = domini.split(".")
            if len(usuari) > 0 and len(parts_domini) > 1:

                return email2

        except:
            print(f"\n {Fore.RED}Has d'introduir un EMAIL incorrecte !!!")
            print(
                f"\n{Fore.GREEN}Utilitza la seguent estroctura\n      exemple@domini.com\n{Fore.RESET}"
            )

        else:
            print(f"\n {Fore.RED}Has d'introduir un EMAIL incorrecte !!!")
            print(
                f"\n{Fore.GREEN}Utilitza la seguent estroctura\n      exemple@domini.com\n{Fore.RESET}"
            )
            email_valid = False


################################################################
"""                  FUNCIONS CREACIO MENU                   """
"""              FUNCIONS COMPROVACIONS FITXER               """


def crea_menu(opcions):

    """Crea el menu utilizant un diccionari"""

    neteja_pantalla()

    print(f"\n{sep}")
    print("Menu".center(len(sep)))
    print(f"{sep}\n")

    for opcio in opcions:
        print("", opcio, ": ", opcions[opcio])

    print(sep)

    op = input_int("Introdueix una opcio vàlida: ", 1, len(opcions))

    return op


def comprovaArxiu(fitxer):

    """Comprova que el arxiu agenda.txt funciona correctement per no tenir problemes durant el programa"""

    ok = True
    try:
        with open(fitxer) as f:
            pass

    except FileNotFoundError:
        print()
        print("L'arxiu no existeix!!!")
        input()
        ok = False

    except:
        print()
        print("No s'ha pogut obrir l'arixu!!")
        print("Comprova el nom del arxiu")
        input()
        ok = False

    return ok


################################################################
"""              FUNCIONS PROGRAMA PRINCIPAL               """


def alta(fitxer):

    """Dona d'alta un contacte"""

    print(sep)
    print("Afegint Contacte".center(len(sep)))
    print(sep)

    # Utilitzant inputs segurs, guarda en cada variable cada apartat del contacte
    nom = input_str("Introduex el nom: ")
    cognom = input_str("Introdueix el Cognom: ")
    email = input_email("Introdueix el email: ")
    tlf = input_int("Introdueix el telèfon: ", 100000000, 999999999)
    tele = input_tele("Introdueix el @Telegram: ")

    alta_a = [nom, cognom, email, str(tlf), tele]

    # Obre el fitxer en mode append
    with open(fitxer, "a") as f:
        linia_nova = ""

        # Utilitzant la llista guarda en ordre cada apartat del contacte.
        for i in alta_a:
            linia_nova += str(i) + ","
        linia_nova = linia_nova[0 : len(linia_nova) - 2] + "\n"
        f.write(linia_nova)

    print(f"\n{sep}")
    print("Contacte Afegit".center(len(sep)))
    print(sep)
    enter()


def llistat(fitxer):

    """Ensenya la Agenda de manera maca"""

    sepll = sep2 + "============================================="
    print(f"\n{sepll}")
    print(Fore.GREEN, "LECTURA AGENDA".center(len(sepll)))
    print(f"{Fore.RESET}{sepll}")

    # Obre el fitxer en mode lectura
    with open(fitxer, "r") as f:

        # Utilitzant PrettyTable definim els apartats de la agenda
        x = PrettyTable()
        x.field_names = ["Nº", "Nom", "Cognom", "Email", "Telefon", "@Telegram"]
        linia_nova = ""
        cont = 0

        # For que imprimeix l'agenda
        for line in f:
            cont += 1
            linia_nova = str(cont) + "," + "".join(line)

            row = linia_nova.strip().split(",")
            x.add_row(row)

        linies = f.readlines()
    print(x)
    print()


def modifica(fitxer):

    with open(fitxer, "r") as file:
        lines = file.readlines()

    llistat(fitxer)

    n_contacte = int(input("Introdueix el numero de contacte que vols editar: "))
    contacte_actual = lines[n_contacte - 1].strip().split(",")

    # Inputs que guarden el nou nom i el nou cognom, si fem un enter normal es guarda el anteriror
    n_nom = (
        input("Introdueix ekl nou nom (Deixa en blanc per deixar l'actual): ")
        or contacte_actual[0]
    )
    n_cognom = (
        input("Introdueix el nou cognom (Deixa en blanc per deixar l'actual): ")
        or contacte_actual[1]
    )

    # Imputs que s'envien a comprovar si son correctes, la part de deixarla en blanc la guarda pero al utilitzar
    # Els imputs segurs no se com fer que amb un enter guardi el que hi havia anteriorment
    n_email = input_email("Introdueix el nou email: ") or contacte_actual[2]
    n_tlf = (
        input_int("Introdueix el nou Telefon: ", 100000000, 999999999)
        or contacte_actual[3]
    )
    n_tele = input_tele("Introdueil nou @Telegram: ") or contacte_actual[4]

    # Ajunta el que hi ha en els inputs anteriors i ho guarda en la variable
    nou_contacte = f"{n_nom},{n_cognom},{n_email},{n_tlf},{n_tele}\n"
    lines[n_contacte - 1] = nou_contacte

    # Obre e fitxer i escriu la linea modificada
    with open(fitxer, "w") as file:
        file.writelines(lines)


def baixa(fitxer):

    """Dona de baixa un contacte"""

    sis = ["S", "Y", "YES", "SI"]

    llistat(fitxer)

    # Guarda en lineas el arxiu
    linies = []
    with open(fitxer, "r") as file:
        linies = file.readlines()

    # Demana de forma segura a qui volem deonar de baixa
    op = input_int("A qui vols donar de Baixa?: ", 1, len(linies))

    op_s = input_str("Estas segur? (S/N): ").upper()

    if op_s in sis:

        # Borra e contacte seleccionat
        with open(fitxer, "w") as f:
            for i, linia in enumerate(linies):
                if i != op - 1:  # n es el número de la línea a eliminar
                    f.write(linia)
    else:
        print(f"\n{sep2}\nNO S'HA BORRAT\n{sep2}")

    enter()


################################################################
"""                     FUNCIONS MAIN                        """


def main():
    neteja_pantalla()
    if comprovaArxiu(fitxer):
        exitt = False

        while not exitt:
            neteja_pantalla()
            op = crea_menu(OPCIONS_MENU)
            if op == 1:
                neteja_pantalla()
                alta(fitxer)

            elif op == 2:
                neteja_pantalla()
                llistat(fitxer)
                enter()

            elif op == 3:
                neteja_pantalla()
                modifica(fitxer)
                enter()
            elif op == 4:
                neteja_pantalla()
                baixa(fitxer)

            elif op == 5:
                exitt = True

            else:
                print(f"\n{sep2}\nOPCIO INCORRECTE\n{sep2}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n{sep2}\nHas tancat el programa!!\n{sep2}")

        print(Fore.RED, e, Fore.RESET)
