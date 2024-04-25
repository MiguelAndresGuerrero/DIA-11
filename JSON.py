import json

ruta_archivo = r"DIA 11\Json.json"

ListaEventos = [
    "CreateEvent", "WatchEvent", "ReleaseEvent", "PullRequestEvent",
    "IssuesEvent", "ForkEvent", "GollumEvent", "IssueCommentEvent",
    "DeleteEvent", "MemberEvent", "PullRequestReviewCommentEvent",
    "PublicEvent", "CommitCommentEvent", "PushEvent"
]

def cargar_json(ruta):
    try:
        with open(ruta, encoding="utf-8") as file:
            datos = json.load(file)
        return datos
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {ruta}")
        return None
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo JSON: {e}")
        return None

def crear_evento(evento_seleccionado):
    nombre_evento = input(f"Ingrese el nombre para el nuevo {evento_seleccionado}: ")
    print(f"Creando {evento_seleccionado} con nombre '{nombre_evento}'")

def main():
    datos = cargar_json(ruta_archivo)

    if not datos:
        return

    name = input("Ingresa tu nombre: ")
    print("Bienvenido", name)

    while True:
        print("================================================================")
        print("                          MENU                                  ")
        print("================================================================")
        print("1. Ver eventos ")
        print("2. Finalizar programa ")
        opcion = input("Selecciona una opción (1, 2): ")

        if opcion == '1':
            print("Tengo estos eventos:")
            for index, evento in enumerate(ListaEventos, start=1):
                print(f"{index}. {evento}")

            opcion_evento = input("Selecciona un evento (1-14): ")

            if opcion_evento.isdigit():
                opcion_evento = int(opcion_evento)
                if 1 <= opcion_evento <= len(ListaEventos):
                    evento_seleccionado = ListaEventos[opcion_evento - 1]
                    print("Has seleccionado", evento_seleccionado)

                    print("¿Qué deseas hacer?")
                    print("""
                        1. Crear
                        2. Eliminar
                        3. Actualizar
                        4. Leer
                    """)
                    
                    opcion_accion = input("Selecciona una opción (1-4): ")

                    if opcion_accion == '1':
                        crear_evento(evento_seleccionado)
                    elif opcion_accion == '2':
                        print(f"Eliminar {evento_seleccionado}")
                    elif opcion_accion == '3':
                        print(f"Actualizar {evento_seleccionado}")
                    elif opcion_accion == '4':
                        print(f"Leer {evento_seleccionado}")
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")

                else:
                    print("Opción no válida. Por favor, selecciona un número del 1 al 14")

            else:
                print("Opción no válida. Debes ingresar un número.")

        elif opcion == '2':
            print("Gracias por usar el programa :D")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

#Creado por Miguel Guerrero C.C 1090381839
