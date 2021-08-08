from tkinter import filedialog, Tk

documento = None
documento_guardado = False
nombre_curso = ""
estudiantes = []
parametros = []

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

def bubbleSort_ascendente(lista_alumnos):
    student_aux = []
    while (True):
        cambios = False
        for i in range(1, len(lista_alumnos)):
            if lista_alumnos[i][1] < lista_alumnos[i-1][1]: #nota siguiente es menor a la nota antecesora
                student_aux = lista_alumnos[i]
                lista_alumnos[i] = lista_alumnos[i-1] #pasando el mayor una posición adelante
                lista_alumnos[i-1] = student_aux #pasando al menor una posición atras
                cambios = True
        if not cambios: #lista ordenada
            return lista_alumnos

def bubbleSort_descendente(lista_alumnos):
    student_aux = []
    while (True):
        cambios = False
        for i in range(1, len(lista_alumnos)):
            if lista_alumnos[i][1] > lista_alumnos[i-1][1]: #nota siguiente es mayor a la nota antecesora
                student_aux = lista_alumnos[i]
                lista_alumnos[i] = lista_alumnos[i-1] #pasando el menor una posición adelante
                lista_alumnos[i-1] = student_aux #pasando al mayor una posición atras
                cambios = True
        if not cambios: #lista ordenada
            return lista_alumnos
        
def promedio(lista_alumnos):
    suma_notas = 0
    for i in range(len(lista_alumnos)):
        suma_notas = suma_notas + lista_alumnos[i][1]
    promedio = suma_notas/len(lista_alumnos)
    return promedio

def aprobados(lista_alumnos):
    alumnos_aprobados = []
    for student in lista_alumnos:
        if student[1] >= 61:
            alumnos_aprobados.append(student)
    return alumnos_aprobados

def reprobados(lista_alumnos):
    alumnos_reprobados = []
    for student in lista_alumnos:
        if student[1] < 61:
            alumnos_reprobados.append(student)
    return alumnos_reprobados

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
                        parametros = []
                        curso_registrado = False
                        estudiantes_registrados = False
                        nombre_aux = ""
                        nota_aux = ""
                        contador_comillas = 0
                        parametro_aux = ""
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
                                    if c == ',':
                                        parametros.append(parametro_aux)
                                        parametro_aux = ""
                                    else:
                                        parametro_aux = parametro_aux + c
                        if parametro_aux != "":
                            parametros.append(parametro_aux)
                        documento_guardado = True
                        print('--> Lectura del archivo exitosa.\n')
                    else:
                        print("--> El documento no posee texto a analizar.\n")
                else:
                    print("--> No se selecciono ningun archivo.\n")
            elif opcion == 2:
                if documento_guardado:
                    print("\nNombre del curso:", nombre_curso)
                    for student in estudiantes:
                        print(student)
                    print("Estudiantes en el curso:", len(estudiantes))
                    print("\nReportes solicitados:")
                    for par in parametros:
                        if par.lower() == "asc":
                            estudiantes_ASC = bubbleSort_ascendente(estudiantes)
                            print("--> REPORTE ASC:")
                            for student in estudiantes_ASC:
                                print(student)
                            print("\n")
                        elif par.lower() == "desc":
                            estudiantes_DESC = bubbleSort_descendente(estudiantes)
                            print("--> REPORTE DESC:")
                            for student in estudiantes_DESC:
                                print(student)
                            print("\n")
                        elif par.lower() == "avg":
                            prom = promedio(estudiantes)
                            print("--> REPORTE AVG:")
                            print("El promedio de los estudiantes es de", prom, "\n")
                        elif par.lower() == "min":
                            print("--> REPORTE MIN:")
                            estudiantes_menoramayor = bubbleSort_ascendente(estudiantes)
                            estudiantes_con_minima = []
                            estudiantes_con_minima.append(estudiantes_menoramayor[0])
                            for i in range(1, len(estudiantes)):
                                if estudiantes_menoramayor[i][1] == estudiantes_con_minima[0][1]:
                                    estudiantes_con_minima.append(estudiantes_menoramayor[i])
                                else:
                                    break
                            if len(estudiantes_con_minima) > 1:
                                print("Nota mínima:", estudiantes_con_minima[0][1], "- Estudiantes con nota mínima:")
                                for student in estudiantes_con_minima:
                                    print("*" + student[0])
                                print("\n")
                            else:
                                print("Nota mínima:", estudiantes_con_minima[0][1], "- Estudiante con nota mínima:")
                                print("*" + estudiantes_con_minima[0][0])
                                print("\n")
                        elif par.lower() == "max":
                            print("--> REPORTE MAX:")
                            estudiantes_mayoramenor = bubbleSort_descendente(estudiantes)
                            estudiantes_con_maxima = []
                            estudiantes_con_maxima.append(estudiantes_mayoramenor[0])
                            for i in range(1, len(estudiantes)):
                                if estudiantes_mayoramenor[i][1] == estudiantes_con_maxima[0][1]:
                                    estudiantes_con_maxima.append(estudiantes_mayoramenor[i])
                                else:
                                    break
                            if len(estudiantes_con_maxima) > 1:
                                print("Nota maxima:", estudiantes_con_maxima[0][1], "- Estudiantes con nota maxima:")
                                for student in estudiantes_con_maxima:
                                    print("*" + student[0])
                                print("\n")
                            else:
                                print("Nota maxima:", estudiantes_con_maxima[0][1], "- Estudiante con nota maxima:")
                                print("*" + estudiantes_con_maxima[0][0])
                                print("\n")
                        elif par.lower() == "apr":
                            estudiantes_APR = aprobados(estudiantes)
                            print("--> REPORTE APR:")
                            if len(estudiantes_APR) > 0:
                                print("Aprobaron", len(estudiantes_APR), "estudiantes:")
                                for student in estudiantes_APR:
                                    print(student)
                                print("\n")
                            else:
                                print("Ningún estudiante aprobó el curso.\n")
                        elif par.lower() == "rep":
                            print("--> REPORTE REP:")
                            estudiantes_REP = reprobados(estudiantes)
                            if len(estudiantes_REP) > 0:
                                print("Reprobaron", len(estudiantes_REP), "estudiantes:")
                                for student in estudiantes_REP:
                                    print(student)
                                print("\n")
                            else:
                                print("Ningún estudiante reprobó el curso.\n")
                        else:
                            print("--> El parámetro", par, "no se reconoce como parámetro válido.\n")
                    print("--> Reportes finalizados.\n")
                else:
                    print("--> No se ha cargado el archivo de notas.\n")
            elif opcion == 3:
                print('Caso 3\n')
            elif opcion == 4:
                print('--> Gracias por usar esta aplicacion :)')
                break
            else:
                print("--> El numero ingresado no corresponde a ninguna accion.\n")
        except:
            print("--> Lo ingresado no corresponde a ninguna accion.\n")