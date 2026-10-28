from pathlib import Path
import shutil


RUTA_RECETAS = Path(__file__).parent / "Recetas"


def bienvenida(ruta):
    ruta = Path(ruta).resolve()
    categorias = []
    for elemento in ruta.iterdir():
        if elemento.is_dir():
            categorias.append(elemento)
    print(f"Bienvenido al recetario de Usuario\nEl recetario se encuentra en la siguiente ruta {ruta}")
    print(f"Hay {len(categorias)} categorias de Recetas")


bienvenida(RUTA_RECETAS)


def opcion_1():
    categorias = sorted(
        carpeta.name for carpeta in RUTA_RECETAS.iterdir()
        if carpeta.is_dir()
    )
    if not categorias:
        print("Todavia no hay categorias")
        return

    print("Estas son las categorias:")
    for numero, categoria in enumerate(categorias, start=1):
        print(f"{numero}. {categoria}")

    eleccion = input("Elige una opcion: ")
    if not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(categorias):
        print("Opcion no valida")
        return
    carpeta = RUTA_RECETAS / categorias[int(eleccion) - 1]
    recetas = sorted(carpeta.glob("*.txt"))
    if not recetas:
        print("Esta categoria no tiene recetas")
        return
    for numero, receta in enumerate(recetas, start=1):
        print(f"{numero}. {receta.stem}")
    eleccion = input("Elige una receta: ")
    if not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(recetas):
        print("Opcion no valida")
        return
    with open(recetas[int(eleccion) - 1], "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(f"Contenido de la receta: {contenido}")




def opcion_2():
    categorias = sorted(
        carpeta.name for carpeta in RUTA_RECETAS.iterdir()
        if carpeta.is_dir()
    )
    if not categorias:
        print("Todavia no hay categorias")
        return

    for numero, categoria in enumerate(categorias, start=1):
        print(f"{numero}. {categoria}")

    eleccion = input("Elige una categoria: ")
    if not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(categorias):
        print("Opcion no valida")
        return

    categoria = categorias[int(eleccion) - 1]
    nombre = input("Nombre de la receta:")
    contenido = input("Contenido de la receta:")
    if not nombre or not contenido:
        print("Opcion no valida")
        return
    nombre_archivo = nombre if nombre.endswith(".txt") else nombre + ".txt"
    ruta_receta = RUTA_RECETAS / categoria / nombre_archivo
    with open(ruta_receta, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print("La receta se creo correctamente")


def opcion_3():
    nombre_categoria = input("Nombre de la categoria:")
    if not nombre_categoria or nombre_categoria in {".",".."}or Path(nombre_categoria).name != nombre_categoria:
        print("Opcion no valida")
        return
    carpeta_categoria = RUTA_RECETAS / nombre_categoria

    if carpeta_categoria.exists():
        print("Ya existe un categoria en la ruta")
        return
    carpeta_categoria.mkdir(parents=True, exist_ok=True)
    print("Categoria creada")


def opcion_4():
    categorias = sorted(
        carpeta.name for carpeta in RUTA_RECETAS.iterdir()
        if carpeta.is_dir()
    )
    if not categorias:
        print("Todavia no hay categorias")
        return

    print("Estas son las categorias:")
    for numero, categoria in enumerate(categorias, start=1):
        print(f"{numero}. {categoria}")

    eleccion = input("Elige una categoria: ")
    if not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(categorias):
        print("Opcion no valida")
        return

    carpeta = RUTA_RECETAS / categorias[int(eleccion) - 1]
    recetas = sorted(carpeta.glob("*.txt"))
    if not recetas:
        print("Esta categoria no tiene recetas")
        return

    for numero, receta in enumerate(recetas, start=1):
        print(f"{numero}. {receta.stem}")

    eleccion = input("Elige la receta que quieres eliminar: ")
    if not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(recetas):
        print("Opcion no valida")
        return

    receta_elegida = recetas[int(eleccion) - 1]
    confirmacion = input(f"¿Seguro que quieres eliminar {receta_elegida.stem}? (s/n): ")
    if confirmacion.lower() == "s":
        receta_elegida.unlink()
        print("La receta se elimino correctamente")
    else:
        print("No se elimino la receta")


def opcion_5():
    categorias = sorted(
        carpeta.name for carpeta in RUTA_RECETAS.iterdir()
        if carpeta.is_dir()
    )
    if not categorias:
        print("Todavia no hay categorias")
        return

    print("Estas son las categorias:")
    for numero, categoria in enumerate(categorias, start=1):
        print(f"{numero}. {categoria}")

    eleccion = input("Elige la categoria que quieres eliminar: ")
    if not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(categorias):
        print("Opcion no valida")
        return

    carpeta_categoria = RUTA_RECETAS / categorias[int(eleccion) - 1]
    confirmacion = input(
        f"¿Seguro que quieres eliminar la categoria {carpeta_categoria.name} "
        "y todas sus recetas? (s/n): "
    )
    if confirmacion.lower() == "s":
        shutil.rmtree(carpeta_categoria)
        print("La categoria se elimino correctamente")
    else:
        print("No se elimino la categoria")



def menu():
    while True:
        eleccion = input("""1.Leer Recetas
2.Crear Receta
3.Crear Categoria
4.Eliminar Receta
5.Eliminar Categoria
6.Salir
Elige una opcion:""")
        if eleccion == "1":
            opcion_1()
            break
        elif eleccion == "2":
            opcion_2()
            break
        elif eleccion == "3":
            opcion_3()
            break
        elif eleccion == "4":
            opcion_4()
            break
        elif eleccion == "5":
            opcion_5()
            break
        elif eleccion == "6":
            print("Hasta luego")
            break
        else:
            print("Opcion no valida")
menu()





