from calculadora import *

#agregar test 
calculador = Calculadora()

#Test para división
def test_div():
    assert calculador.division(4,0) == Exception # Pasa
    assert calculador.division(4,2) == 2 # No pasa
    assert calculador.division(15,3) == 5 # No pasa
    assert calculador.division(1,3) == 0 # Pasa
    assert calculador.division(3,3) == 1 # No pasa

#Test para resta 
def test_resta():
    assert calculador.resta(5,1) == 4 # No pasa
    assert calculador.resta(3,0) == 3 # Pasa 
    assert calculador.resta(0,10) == -10# No para 

#Test para multiplicación 
def test_mult():
    assert calculador.multiplicacion(4,3) == 12# No pasa
    assert calculador.multiplicacion(3,1) == 3 # Pasa 
    assert calculador.multiplicacion(1,14) == 14 # No pasa
    assert calculador.multiplicacion(7,0) == 0 # No pasa
    assert calculador.multiplicacion(0,8) == 0 # No pasa

#Test para suma 

# test_div()
# test_resta()
# test_mult()