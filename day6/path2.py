from pathlib import Path
from os import system

base = Path.home()
guia = Path(base, "America", "Mexico", Path("Tamaulipas", "Tampico.txt"))
guia2 = Path.with_name(guia, "CiudadMadero.jpg")
guia3 = Path.with_suffix(guia, ".pdf")
guia4 = Path.with_stem(guia, "CiudadMadero")
print(guia)
print(guia2)
print(guia3)
system("cls")
print(guia4)
