from pathlib import Path

folder = Path("/Users/omontes/desarrollos/nuevo-portal/01desarrollos/python/bases/day6/log.txt")

if not folder.exists():
    print("El directorio no existe")
else:
    print("El directorio ya existe")
    print(folder.read_text())