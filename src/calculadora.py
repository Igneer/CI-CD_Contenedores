import os # importamos una libreria que no se usa para poder demostrar el Linteo del codigo para hacer mas robusta la integracion continua
class Calculadora:
    def __init__(self):
        print ("CALCULADORA CREADA")
              
    def division(self, a:int, b:int):
        if b == 0:
            return Exception
        return a//b #con error para luego aplicar CI
    
    def suma(self, a:int, b:int):
        return a + b
    
    def resta(self, a :int, b :int):
        return a - b
    
    def multiplicacion(self, a :int, b :int):
        return a * b 