class JugadorFutbol:
    
    def __init__(self, nombre, edad, posicion, condicionFisica, equipo="sin asignar") -> None:
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.condicionFisica = condicionFisica
        self.equipo = equipo

    def __str__(self) -> str:
        return f'Que tal, soy {self.nombre} y juego en el equipo como {self.posicion}'

    def campoDeAccion(self):
        if self.posicion == 'portero':
            return f'Soy el {self.posicion} y evito que el balon entre a la porteria.'
        elif self.posicion == 'defensa':
            return f'Soy el {self.posicion} y trato que el balon no pase hacia el portero.'
        elif self.posicion == 'medio':
            return f'Soy el {self.posicion} y en el centro, pasando el balon al delantero'
        elif self.posicion == 'delantero':
            return f'Soy el {self.posicion} y trato de anotar gol.'
        else:
            return 'Esa posicion no ha sido asignada'

    def competir(self, otroJugador):
        pass


def creacionDeJugador():
    try:
        porteroFrancisco = JugadorFutbol('Franciso Perez', 25, 'portero', 93)
        defensaMarcos = JugadorFutbol('Marcos Avila', 30, 'xd', 87)
        medioMessi = JugadorFutbol('Messi Chido', 32, 'delantero', 95)
        delanteroRonaldo = JugadorFutbol('Cristiano Ronaldo', 30, 'delantero', 96)
        
        print(str(medioMessi))
        print(porteroFrancisco.campoDeAccion())
        print(defensaMarcos.campoDeAccion())
    except TypeError:
        print("Falto algun argumento, revisa de nuevo")
        

def main():
    creacionDeJugador()


if __name__ == '__main__':
    main()