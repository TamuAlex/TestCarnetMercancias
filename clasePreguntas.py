import json


class Pregunta(object):
    def __init__(self, key, cod, pregunta, resA, resB, resC, resD, resE, resF, resG, resH, sol, norma):
        self.key = key
        self.cod = cod
        self.pregunta = pregunta
        self.resA = resA
        self.resB = resB
        self.resC = resC
        self.resD = resD
        self.resE = resE
        self.resF = resF
        self.resG = resG
        self.resH = resH
        self.sol = sol
        self.norma = norma


    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

class Encoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
