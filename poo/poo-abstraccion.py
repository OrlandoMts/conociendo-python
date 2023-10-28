from abc import ABC, abstractmethod


class Avion(ABC):
    # La clase Avion ya no podra ser instanciada directamente

    # Cuando un metodo sea abstracto lo tengo que "reedefinir" o volver a declarar en las clases que
    # hereden de la clase Avion
    # Si no lo hago, no funcionará el programa
    @abstractmethod
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.clase = ""
        self.capacidadCarga = ""
        self.capacidadPasajeros = 130
        self.kmRecorridos = 0
        self.aeropuertosVisitados = []
        self.antiguedad = 0

    @abstractmethod
    def volar(self, destino, km):
        print(f"Vuelo con direccion a {destino}")

    @abstractmethod
    def capacidadMaximaPasajeros(self):
        print(f"El avion {self.nombre} tiene una capacidad máxima de {self.capacidadPasajeros} personas")

    # Si un metodo es muy simple, no es necesario hacerlo abstracto
    def llenarAsientos(self, pasajeros):
        self.capacidadPasajeros -= pasajeros

    
    def mantenimiento(self):
        if self.kmRecorridos >= 20:
            print(f"El avion estaba en mantenimiento, ahora tiene {self.kmRecorridos} km recorridos")
        else:
            print(f"Aun no necesita mantenimiento. ")
    
    def verAeropuertosVisitados(self):
        for i in self.aeropuertosVisitados:
            print(i)


class Airbus(Avion):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.capacidadPasajeros = 150 #En la clase abstracta Avion tiene por defecto 130
        self.antiguedad = 0.7
        self.pasajeros = 0

    def llenarAsientos(self, pasajeros):
        self.pasajeros += pasajeros
        asientosDisponibles = self.capacidadPasajeros - self.pasajeros
        print(f"Llenando el avion... Tiene {asientosDisponibles} asientos disponibles todavia")
        return super().llenarAsientos(pasajeros)
    
    def volar(self, destino, km):
        self.aeropuertosVisitados.append(destino)
        self.kmRecorridos += km
        
        super().mantenimiento()
        return super().volar(destino, km)

    def capacidadMaximaPasajeros(self):
        return super().capacidadMaximaPasajeros()

    def verAeropuertosVisitados(self):
        return super().verAeropuertosVisitados()


def main():
    airbus319 = Airbus("Aribus 319")
    airbus319.llenarAsientos(100)
    airbus319.volar("MEXICO", 10)
    airbus319.volar("GDL", 5)
    airbus319.volar("MTY", 15)
    airbus319.verAeropuertosVisitados()


if __name__ == '__main__':
    main()