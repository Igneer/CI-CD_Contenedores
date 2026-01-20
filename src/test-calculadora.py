from calculadora import *

#agregar test 
calculador = Calculadora()

assert calculador.division(4,0) == Exception # este pasa
assert calculador.division(4,2) == 2 # este no pasa
assert calculador.division(15,3) == 5 # este no pasa
assert calculador.division(1,3) == 0 # este si pasa
assert calculador.division(3,3) == 1 # este no pasa
