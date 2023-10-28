class Persona:
    
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self, otra_persona):
        return print("Hola " + otra_persona.nombre + ", me llamo " + self.nombre)


def main():
    daniel = Persona('Daniel', 24)
    ashley = Persona('Ashley', 18)

    daniel.saludar(ashley)


if __name__ == '__main__':
    main()