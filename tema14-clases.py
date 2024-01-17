class OperacionesBasicas:
    #declaracion de propiedades clase
    num1 = 0
    num2 = 0
    rest = 0
    #declaracion de constructor
    def __init__(self) -> None:
        self.num1 = a
        self.num2 = b

    #declaracion de metodos de clase
    def suma(self):
        self.rest = self.num1 + self.num2
        print("la suma es: {}".format(self.rest))

def main():
    obj=OperacionesBasicas(3,4)
    obj.suma()

if __name__ == "__main__":
    main()