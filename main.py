from tkinter import filedialog, Tk

documento = None
nombreCurso = ''
estudiantes = []

def abrirArchivo():    
    Tk().withdraw()
    print('--> Se ha abierto la ventana para seleccionar el archivo')
    archivo = filedialog.askopenfile(
        title = "Seleccionar archivo LFP",
        initialdir = "./",
        filetypes = {
            ("Archivos LFP", "*.lfp"),
            ("Todos los archivos", "*.*")
        }
    )
    try:
        texto = archivo.read()
        archivo.close()
        print('--> Lectura del archivo exitosa')
        return texto
    except:
        return None

if __name__ == '__main__':
    while True:
        print("============ MENU ============")
        print("1. Cargar archivo")
        print("2. Mostrar reporte en consola")
        print("3. Exportar reporte")
        print("4. Salir de la aplicacion")
        print("==============================")
        ingresado = input('Ingrese el numero de la accion que desee realizar:')
        try:
            opcion = int(ingresado)
            if opcion == 1: # CARGA DE ARCHIVO
                documento = abrirArchivo()
                if documento is not None:
                    print(documento)
                else:
                    print("--> No se selecciono ningun archivo.\n")
            elif opcion == 2:
                print('Caso 2\n')
            elif opcion == 3:
                print('Caso 3\n')
            elif opcion == 4:
                print('--> Gracias por usar esta aplicacion :)')
                break
            else:
                print("El numero ingresado no corresponde a ninguna accion.\n")
        except:
            print("Lo ingresado no corresponde a ninguna accion.\n")