from tkinter import filedialog, Tk

documento = None
nombre_curso = ""
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
        ingresado = input('Ingrese el numero de la accion que desee realizar: ')
        try:
            opcion = int(ingresado)
            if opcion == 1: # --> CARGA DE ARCHIVO Y ANÁLISIS
                documento = abrirArchivo()
                if documento is not None:
                    if len(documento)>0:
                        nombre_curso = ""
                        estudiantes = []
                        curso_registrado = False
                        estudiantes_registrados = False
                        nombre_aux = ""
                        nota_aux = ""
                        contador_comillas = 0
                        for c in documento:
                            if c == '"':
                                contador_comillas = contador_comillas + 1
                            if (contador_comillas % 2) == 1: # escribiendo el nombre del estudiante, admite TODOS los caracteres
                                if c != '"':
                                    nombre_aux = nombre_aux + c
                            else: # no es el nombre el que estamos leyendo
                                if c == ' ' or c == '\n' or c == '\t':
                                    pass
                                elif c == '=':
                                    curso_registrado = True
                                elif not curso_registrado:
                                    nombre_curso = nombre_curso + c
                                elif c == '{':
                                    pass
                                elif c == '}':
                                    estudiantes_registrados = True
                                elif not estudiantes_registrados:
                                    if c == ',' or c == ';':
                                        pass
                                    elif c == '<':
                                        nombre_aux = ""
                                        nota_aux = ""
                                    elif c == '>':
                                        nota_aux = float(nota_aux)
                                        student_aux = [nombre_aux, nota_aux]
                                        estudiantes.append(student_aux) # Se agrega al alumno con su nota
                                    else: # estamos escribiendo la nota
                                        if c != '"':
                                            if (c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or c == '.'):
                                                nota_aux = nota_aux + c
                                            else:
                                                print('--> La nota de', nombre_aux, 'contiene el caracter invalido', c + ', el cual se ignoró.')
                                else:
                                    pass # parametros
                        print('--> Lectura del archivo exitosa.\n')
                    else:
                        print("--> El documento no posee texto a analizar.\n")
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
                print("--> El numero ingresado no corresponde a ninguna accion.\n")
        except:
            print("--> Lo ingresado no corresponde a ninguna accion.\n")