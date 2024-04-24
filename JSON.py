import json
from os import system

# Usando raw string para la ruta del archivo
ruta_archivo = r"C:\Users\USUARIO\Desktop\TRABAJOS_GuerreroMiguel\Python\DIA 11\large-file.json"

try:
    with open(ruta_archivo, encoding="utf-8") as file:
        Datos = json.load(file)
    print(Datos)
    
except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{ruta_archivo}'. Verifica la ruta y asegúrate de que el archivo exista")
    
except Exception as e:
    print(f"Ocurrió un error: {e}")

ListaEventos = {
"CreateEvent"
"WatchEvent"
"ReleaseEvent"
"PullRequestEvent"
"IssuesEvent"
"ForkEvent"
"GollumEvent"
"IssueCommentEvent"
"DeleteEvent"
"MemberEvent"
"PullRequestReviewCommentEvent"
"PublicEvent"
"CommitCommentEvent"
"PushEvent"
}

#Bienveida al usuario
name=input("Ingresa tu nombre: ")
print("Bienvenido ",name)

#menu que e le mostrara al usuario
menu = True
while menu==True:
    print("================================================================")
    print("                          MENU                                  ")
    print("================================================================")
    print("1. ver eventos ")
    print("2. finalizar programa ")
    Option = int(input("seleccione una opcion (1,2)\n"))
    system("cls")
    
    if Option == 1:
    
        print("Tengo estos eventos:")
        print("""
            1. CreateEvent
            2. WatchEvent
            3. ReleaseEvent
            4. PullRequestEvent
            5. IssuesEvent
            6. ForkEvent
            7. GollumEvent
            8. IssueCommentEvent
            9. DeleteEvent
            10. MemberEvent
            11. PullRequestReviewCommentEvent
            12. PublicEvent
            13. CommitCommentEvent
            14. PushEvent
        """)
    
        opcion = input("Selecciona una opción del 1 al 14: ")
        system("cls")
        
        if opcion:
            print("Has seleccionado",ListaEventos )
            print("¿Que deseas hacer?")
            print("""
                1. crear
                2. eliminar
                3. actualizar
                4. leer
            """)
        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 14.")
              
    if Option==2:
        print("Gracias por usarme :D")
        menu==False
    break

#Creado por Miguel Guerrero C.C 1090381839