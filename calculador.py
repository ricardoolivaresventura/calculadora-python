n1 = float(input("Introduce tu primer número: ") );
n2 = float(input("Introduce tu segundo número: ") );

def suma(n1, n2):
    print("Resultado de la suma: ",n1, " + ",n2," es igual a: ",n1 + n2)
    return n1 + n2

def resta(n1, n2):
    print("Resultado de la resta: ",n1, " - ",n2, " es igual a: ",n1 - n2)
    return n1 - n2

def multiplicacion(n1, n2):
    print("Resultado de la multiplicacion: ",n1, " * ", n2, " es igual a: ",n1 * n2)
    return n1 * n2

def division(n1, n2):
    print("Resultado de la division: ",n1, " / ", n2, " es igual a: ",n1/n2)
    return n1/n2

def callAllFunctions():
    suma(n1, n2)
    resta(n1, n2)
    multiplicacion(n1, n2)
    division(n1, n2)

callAllFunctions()