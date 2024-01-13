num1 = 20
num2 = 4
print("la suma es: ", (num1+num2))
print("la resta es: ", (num1-num2))
print("la multiplicacion es: ", (num1*num2))
print("la divicion exacta es: ", (num1//num2))
print("la divicion es: ", (num1/num2))
print("la potencia es: ", (num1**num2))

#Concatenacion en python

texto1 = "hola"
texto2 = "mundo"
textoFinal = texto1 + " "+ texto2
print(textoFinal)
print("el saludo es: %s %s" %(texto1,texto2))
saludoFinal = 'saludo {} {}'.format(texto1,texto2)
print(saludoFinal)
saludoFinal2 = 'Saludo 2: {y} {x}'.format(x=texto1,y=texto2)
print(saludoFinal2)