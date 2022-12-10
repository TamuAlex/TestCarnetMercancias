from clasePreguntas import Pregunta, Encoder
import json





class ParserCM(object):

    def __init__(self):

        pass
    def parse(self, rutaArchivo):
        preguntas = []
        with open(rutaArchivo, encoding='utf-8') as fichero:
            key=0
            cod = ''
            pregunta = ''
            resA = ''
            resB = ''
            resC = ''
            resD = ''
            resE = ''
            resF = ''
            resG = ''
            resH = ''
            sol = ''
            norma =''
            flag = ''
            for linea in fichero.readlines():
                if linea in ['\n', '\r\n']:
                    flag =''

                elif linea.startswith('COD'):
                    cod = linea
                elif linea.startswith('PREGUNTA'):
                    flag = 'PREG'
                elif linea.startswith('RESPUESTA A'):
                    flag = 'resA'
                elif linea.startswith('RESPUESTA B'):
                    flag = 'resB'
                elif linea.startswith('RESPUESTA C'):
                    flag = 'resC'
                elif linea.startswith('RESPUESTA D'):
                    flag = 'resD'
                elif linea.startswith('RESPUESTA E'):
                    flag = 'resE'
                elif linea.startswith('RESPUESTA F'):
                    flag = 'resF'
                elif linea.startswith('RESPUESTA G'):
                    flag = 'resG'
                elif linea.startswith('RESPUESTA H'):
                    flag = 'resH'
                elif linea.startswith('SOLUCION'):
                    sol=linea
                elif linea.startswith('NORMA'):
                    norma = linea
                    key +=1
                    preguntas.append(Pregunta(key,cod,pregunta,resA,resB,resC,resD,resE,resF,resG,resH,sol,norma))
                    cod = ''
                    pregunta = ''
                    resA = ''
                    resB = ''
                    resC = ''
                    resD = ''
                    resE = ''
                    resF = ''
                    resG = ''
                    resH = ''
                    sol = ''
                    norma =''
                    flag = ''

                elif flag == 'PREG':
                    pregunta += linea
                elif flag == 'resA':
                    resA+=linea
                elif flag == 'resB':
                    resB+=linea
                elif flag == 'resC':
                    resC+=linea
                elif flag == 'resD':
                    resD+=linea
                elif flag == 'resE':
                    resE+=linea
                elif flag == 'resF':
                    resF+=linea
                elif flag == 'resG':
                    resG+=linea
                elif flag == 'resH':
                    resH+=linea

        return preguntas

class ParserPM(object):

    def __init__(self):

        pass
    def parse(self, rutaArchivo):
        preguntas = []
        with open(rutaArchivo, encoding='utf-8') as fichero:
            key=0
            cod = ''
            pregunta = ''
            resA = ''
            resB = ''
            resC = ''
            resD = ''
            sol = ''
            norma =''
            flag = False
            for linea in fichero.readlines():
                if linea in ['\n', '\r\n']:
                    flag = True

                elif linea.startswith('COD'):
                    cod = linea
                elif linea.startswith('PREGUNTA'):
                    pregunta = linea
                elif linea.startswith('A'):
                    resA = linea
                elif linea.startswith('B'):
                    resB = linea
                elif linea.startswith('C'):
                    resC = linea
                elif linea.startswith('D'):
                    resD = linea
                elif linea.startswith('SOLUCION'):
                    sol = linea
                elif linea.startswith('NORMA'):
                    norma = linea

                if flag:
                    preguntas.append(Pregunta(key,cod,pregunta,resA,resB,resC,resD,'','','','',sol,norma))
                    cod = ''
                    pregunta = ''
                    resA = ''
                    resB = ''
                    resC = ''
                    resD = ''
                    sol = ''
                    norma =''
                    flag = False


        return preguntas



