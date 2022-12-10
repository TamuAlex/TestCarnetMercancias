from parserPreguntas import ParserCM
from clasePreguntas import Pregunta
import os
import colors
import random
import main


def menu():
    print("========================================================================================")
    print("|                                 PREGUNTAS MERCANCIAS                                 |")
    print("========================================================================================")
    print("| \033[94m 1. Batería de Preguntas A\033[00m                                                           |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 2. Batería de Preguntas B\033[00m                                                           |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 3. Batería de Preguntas C\033[00m                                                           |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 4. Batería de Preguntas D\033[00m                                                           |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 5. Batería de Preguntas E\033[00m                                                           |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 6. Batería de Preguntas F\033[00m                                                           |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 7. Batería de Preguntas G\033[00m                                                           |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 8. Batería de Preguntas H\033[00m                                                           |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 9. ALEATORIO\033[00m                                                                        |")
    print("----------------------------------------------------------------------------------------")
    print("| \033[94m 10. Salir\033[00m                                                                            |")
    print("========================================================================================")



def pedirOpcion():
    return input("Selecciona una opción [1,2,3,4,5,6,7,8,9,10]: ")

def opcionIncorrecta():
    colors.prRed("Opción incorrecta, por favor, elige un numero del 1 al 10")


def test(preguntas):
     acertadas = 0
     falladas = 0
     for i in range(0,30):
         pregunta = random.choice(preguntas)
         os.system('cls')
         print("========================================================================================")
         print("|                                 PREGUNTA " + str(i + 1) + "                                 |")
         print("========================================================================================")
         print("")
         print(pregunta.pregunta)
         print("========================================================================================")
         print("|                                      RESPUESTAS                                      |")
         print("========================================================================================")
         print("RESPUESTA A")
         print(pregunta.resA)
         print("")
         print("RESPUESTA B")
         print(pregunta.resB)
         print("")
         print("RESPUESTA C")
         print(pregunta.resC)
         print("")
         print("RESPUESTA D")
         print(pregunta.resD)
         print("")
         print("RESPUESTA E")
         print(pregunta.resE)
         print("")
         print("RESPUESTA F")
         print(pregunta.resF)
         print("")
         print("RESPUESTA G")
         print(pregunta.resG)
         print("")
         print("RESPUESTA H")
         print(pregunta.resH)
         print("")
         colors.prCyan("Introduce tu respuesta [A,B,C,D,E,F,G,H]")
         respuesta = input()
         respuesta = respuesta.capitalize()

         while(respuesta!='A' and respuesta!='B' and respuesta!='C' and respuesta!='D' and respuesta!='E' and respuesta!='F' and respuesta!='G' and respuesta!='H'):
          colors.prRed("Por favor, elige una respuesta de la A a la H")
          respuesta = input()
          respuesta = respuesta.capitalize()
         
         if (respuesta==pregunta.sol[20]):
          colors.prGreen("CORRECTO")
          acertadas+=1
         else:
          colors.prRed("INCORRECTO, la respuesta correcta era: " + pregunta.sol[20])
          falladas+=1
         colors.prLightPurple(pregunta.norma)
     
         colors.prGreen("ACERTADAS: " + str(acertadas))
         colors.prRed("FALLADAS: " + str(falladas))
         
         print("Pulsa intro para continuar")
         input()

     os.system('cls')
     print("========================================================================================")
     print("|                                 TEST FINALIZADO                                      |")
     print("========================================================================================")
     colors.prGreen("ACERTADAS: " + str(acertadas))
     colors.prRed("FALLADAS: " + str(falladas))
     print("")
     colors.prCyan("Pulsa intro para continuar")
     input()
     main.main()
def testPreguntasInit():#function of the button
     #tkinter.messagebox.showinfo("Greetings","Hello! Welcome to PythonGeeks.")



    parserCM = ParserCM()
    preguntas1A = parserCM.parse("cm/cm1A.txt")
    preguntas1B = parserCM.parse("cm/cm1B.txt")
    preguntas1C = parserCM.parse("cm/cm1C.txt")
    preguntas1D = parserCM.parse("cm/cm1D.txt")
    preguntas1E = parserCM.parse("cm/cm1E.txt")
    preguntas1F = parserCM.parse("cm/cm1F.txt")
    preguntas1G = parserCM.parse("cm/cm1G.txt")
    preguntas1H = parserCM.parse("cm/cm1H.txt")
    
    os.system('cls')
    menu()
    opcion = pedirOpcion()

    while (opcion!='1' and opcion!='2' and opcion!='3' and opcion!='4' and opcion!='5' and opcion!='6' and opcion!='7' and opcion!='8' and opcion!='9' and opcion!='10'):
     opcionIncorrecta()
     opcion = pedirOpcion()

    if opcion=='1':
     test(preguntas1A)
    elif opcion=='2':
     test(preguntas1B)
    elif opcion=='3':
     test(preguntas1C)
    elif opcion=='4':
     test(preguntas1D)
    elif opcion=='5':
     test(preguntas1E)
    elif opcion=='6':
     test(preguntas1F)
    elif opcion=='7':
     test(preguntas1G)
    elif opcion=='8':
     test(preguntas1H)
    elif opcion=='9':
     test(preguntas1A + preguntas1B + preguntas1C + preguntas1D + preguntas1E + preguntas1F + preguntas1G + preguntas1H)
    elif opcion=='10':
     main.main()