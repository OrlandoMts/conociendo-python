class car:

    def __init__(self, model, color) -> None:
        self.model = model
        self.color = color

        self.start()

    
    def start(self):
        print(self.model + " auto registrado desde la funcion start")



myCar = car("rav4", "red")
print("Info desde la instancia: " + myCar.model + ' ' + myCar.color)


# myCar2 = car("versa", "gray")
# print(myCar2.color + ' ' + myCar2.model)