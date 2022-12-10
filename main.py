

import preguntasMercancias
import preguntasPracticas
import colors
from colorama import init



def intro():
    print("========================================================================================")
    print("|                                    TEST MERCANCIAS                                   |")
    print("========================================================================================")

    print("| \033[94m 1. Preguntas Mercancías\033[00m                                                             |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 2. Casos Prácticos\033[00m                                                                  |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 3. Salir\033[00m                                                                            |")
    print("========================================================================================")

def pedirOpcion():
    return input("Selecciona una opción [1,2,3]: ")

def opcionIncorrecta():
    colors.prRed("Opción incorrecta, por favor, elige un numero del 1 al 3")

def main():
   
    init(convert=True)
    intro()
    opcion = pedirOpcion()

    while (opcion!='1' and opcion!='2' and opcion!='3'):
        opcionIncorrecta()
        opcion = pedirOpcion()
        print(opcion)

    if (opcion=='1'):
        preguntasMercancias.testPreguntasInit()
    if (opcion=='2'):
        preguntasPracticas.testPreguntasInit()
    if (opcion == '3'):
        print("Adios")
    

if __name__=="__main__":
    main()