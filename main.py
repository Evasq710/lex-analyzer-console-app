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
                            lista_aux = estudiantes[:]
                            estudiantes_ASC = bubbleSort_ascendente(lista_aux)
                            print("--> REPORTE ASC:")
                            for student in estudiantes_ASC:
                                print(student)
                            print("\n")
                        elif par.lower() == "desc":
                            lista_aux = estudiantes[:]
                            estudiantes_DESC = bubbleSort_descendente(lista_aux)
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
                            lista_aux = estudiantes[:]
                            estudiantes_menoramayor = bubbleSort_ascendente(lista_aux)
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
                            lista_aux = estudiantes[:]
                            estudiantes_mayoramenor = bubbleSort_descendente(lista_aux)
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
                if documento_guardado:
                    try:
                        students_html = ""
                        color = ""
                        contador_students = 0
                        for student in estudiantes:
                            contador_students = contador_students + 1
                            if student[1] >= 61:
                                color = 'style="color: blue;"'
                            else:
                                color = 'style="color: red;"'
                            students_html = students_html + """<tr>
                                            <th scope="row">"""+ str(contador_students) + """</th>
                                            <td style="text-align: left;">"""+student[0]+"""</td>
                                            <td """ + color + ">" + str(student[1]) + """</td>
                                            </tr>\n"""
                        parametros_html = ""
                        students_asc_html = '<tr><th scope="row">-</th><td style="text-align: left;">No se solicito este reporte</td><td>-</td></tr>'
                        students_desc_html = '<tr><th scope="row">-</th><td style="text-align: left;">No se solicito este reporte</td><td>-</td></tr>'
                        prom_html = 0
                        prom_solicitado = False
                        min_html = 0
                        students_min_html = ""
                        min_solicitado = False
                        max_html = 0
                        students_max_html = ""
                        max_solicitado = False
                        contador_apr = 0
                        students_apr_html = ""
                        apr_solicitado = False
                        contador_rep = 0
                        students_rep_html = ""
                        rep_solicitado = False
                        for par in parametros:
                            if par.lower() == "asc":
                                parametros_html = parametros_html + '<button type="button" class="btn btn-outline-dark" onclick="mostrarTablaASC()">ASC</button>\n'
                                lista_aux = estudiantes[:]
                                estudiantes_ASC = bubbleSort_ascendente(lista_aux)
                                contador_asc = 0
                                students_asc_html = ""
                                for student in estudiantes_ASC:
                                    contador_asc = contador_asc + 1
                                    students_asc_html = students_asc_html + """<tr>
                                                    <th scope="row">""" + str(contador_asc) + """</th>
                                                    <td style="text-align: left;">""" +student[0]+"""</td>
                                                    <td>"""+str(student[1])+"""</td>
                                                    </tr>"""
                            elif par.lower() == "desc":
                                parametros_html = parametros_html + '<button type="button" class="btn btn-outline-dark" onclick="mostrarTablaDESC()">DESC</button>\n'
                                lista_aux = estudiantes[:]
                                estudiantes_DESC = bubbleSort_descendente(lista_aux)
                                students_desc_html = ""
                                contador_desc = 0
                                for student in estudiantes_DESC:
                                    contador_desc = contador_desc + 1
                                    students_desc_html = students_desc_html + """<tr>
                                                    <th scope="row">"""+str(contador_desc)+"""</th>
                                                    <td style="text-align: left;">"""+student[0]+"""</td>
                                                    <td>"""+str(student[1])+"""</td>
                                                    </tr>"""
                            elif par.lower() == "avg":
                                parametros_html = parametros_html + '<button type="button" class="btn btn-outline-dark" onclick="mostrarPromedio()">AVG</button>\n'
                                prom_html = promedio(estudiantes)
                                prom_solicitado = True
                            elif par.lower() == "min":
                                parametros_html = parametros_html + '<button type="button" class="btn btn-outline-dark" onclick="mostrarMinimo()">MIN</button>\n'
                                min_solicitado = True
                                lista_aux = estudiantes[:]
                                estudiantes_menoramayor = bubbleSort_ascendente(lista_aux)
                                estudiantes_con_minima = []
                                estudiantes_con_minima.append(estudiantes_menoramayor[0])
                                for i in range(1, len(estudiantes)):
                                    if estudiantes_menoramayor[i][1] == estudiantes_con_minima[0][1]:
                                        estudiantes_con_minima.append(estudiantes_menoramayor[i])
                                    else:
                                        break
                                students_min_html = ""
                                if len(estudiantes_con_minima) > 1:
                                    min_html = estudiantes_con_minima[0][1]
                                    for student in estudiantes_con_minima:
                                        students_min_html = students_min_html + '<li>' + student[0] + '</li>\n'
                                else:
                                    min_html = estudiantes_con_minima[0][1]
                                    students_min_html = estudiantes_con_minima[0][0]
                            elif par.lower() == "max":
                                parametros_html = parametros_html + '<button type="button" class="btn btn-outline-dark" onclick="mostrarMaximo()">MAX</button>\n'
                                max_solicitado = True
                                lista_aux = estudiantes[:]
                                estudiantes_mayoramenor = bubbleSort_descendente(lista_aux)
                                estudiantes_con_maxima = []
                                estudiantes_con_maxima.append(estudiantes_mayoramenor[0])
                                for i in range(1, len(estudiantes)):
                                    if estudiantes_mayoramenor[i][1] == estudiantes_con_maxima[0][1]:
                                        estudiantes_con_maxima.append(estudiantes_mayoramenor[i])
                                    else:
                                        break
                                students_max_html = ""
                                if len(estudiantes_con_maxima) > 1:
                                    max_html = estudiantes_con_maxima[0][1]
                                    for student in estudiantes_con_maxima:
                                        students_max_html = students_max_html + '<li>'+student[0]+'</li>\n'
                                else:
                                    max_html = estudiantes_con_maxima[0][1]
                                    students_max_html = estudiantes_con_maxima[0][0]
                            elif par.lower() == "apr":
                                parametros_html = parametros_html + '<button type="button" class="btn btn-outline-dark" onclick="mostrarAprobados()">APR</button>\n'
                                apr_solicitado = True
                                estudiantes_APR = aprobados(estudiantes)
                                students_apr_html = ""
                                if len(estudiantes_APR) > 0:
                                    contador_apr = len(estudiantes_APR)
                                    for student in estudiantes_APR:
                                        students_apr_html = students_apr_html + '<li>'+ student[0] + ' - Nota: '+ str(student[1]) + '</li>\n'
                                else:
                                    contador_apr = 0
                            elif par.lower() == "rep":
                                parametros_html = parametros_html + '<button type="button" class="btn btn-outline-dark" onclick="mostrarReprobados()">REP</button>\n'
                                rep_solicitado = True
                                estudiantes_REP = reprobados(estudiantes)
                                students_rep_html = ""
                                if len(estudiantes_REP) > 0:
                                    contador_rep = len(estudiantes_REP)
                                    for student in estudiantes_REP:
                                        students_rep_html = students_rep_html + '<li>'+student[0] + ' - Nota: '+str(student[1])+ '</li>\n'
                                else:
                                    contador_rep = 0
                            else:
                                print("--> El parámetro", par, "no se reconoce como parámetro válido.\n")
                        if not prom_solicitado:
                            prom_html = 'No se solicito este reporte'
                        if not min_solicitado:
                            min_html = 'No se solicito este reporte'
                        if not max_solicitado:
                            max_html = 'No se solicito este reporte'
                        if not apr_solicitado:
                            contador_apr = 'No se solicito este reporte'
                        if not rep_solicitado:
                            contador_rep = 'No se solicito este reporte'
                    except:
                        print("--> Ocurrio un error en la lógica de la creación de reportes")
                    try:
                        reporte_html = open('Reporte.html', 'w')
                        reporte_html.write("""<!DOCTYPE html>
                        <html lang="es">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                            <link rel="stylesheet" href="estilos.css" type="text/css" />
                            <title>Reportes</title>
                        </head>
                        <body>
                            <h1 class="display-1" style="text-align: center; color: white;">Reportes</h1>
                            <div class="datos-archivo">
                                <h1>Nombre del curso: </h1><h1 class="display-6">"""+nombre_curso+"""</h1><br>
                                <div class="tabla-estudiantes">
                                    <table class="table table-striped table-hover">
                                        <thead style="background-color: black; color: white;">
                                            <tr>
                                            <th scope="col">#</th>
                                            <th scope="col" style="text-align: left;">Nombre del Estudiante</th>
                                            <th scope="col">Nota</th>
                                            </tr>
                                        </thead>
                                        <tbody>"""+students_html+
                                        """</tbody>
                                    </table>
                                </div>
                            </div>
                            <div class="reportes">
                                <h1>Reportes solicitados:</h1>
                                <div class="botones-reportes">
                                    <div class="btn-group" role="group" aria-label="First group">"""+ parametros_html +
                                        """<button type="button" class="btn btn-outline-dark" onclick="mostrarTodos()">Mostrar todos</button>
                                    </div>
                                </div>

                                <div class="reportes-individuales" id="reportes-individuales">
                                    <!-- Espacio para reportes -->
                                </div>

                                <div class="reportes-todos" id="reportes-todos" hidden>
                                    <div id="tabla-oculta-ASC">
                                        <h1 class="display-6"><b>Reporte ASC (ascendente)</b></h1>
                                        <div class="tabla-ASC">
                                            <table class="table table-striped table-hover">
                                                <thead style="background-color:rgb(66, 4, 4); color: white;">
                                                    <tr>
                                                    <th scope="col">#</th>
                                                    <th scope="col" style="text-align: left;">Nombre del Estudiante</th>
                                                    <th scope="col">Nota</th>
                                                    </tr>
                                                </thead>
                                                <tbody>"""+students_asc_html+
                                                """</tbody>
                                            </table>
                                        </div>
                                        <hr />
                                    </div>
                                
                                    <div id="tabla-oculta-DESC">
                                        <h1 class="display-6"><b>Reporte DESC (descendente)</b></h1>
                                        <div class="tabla-DESC">
                                            <table class="table table-striped table-hover">
                                                <thead style="background-color: rgb(66, 4, 4); color: white;">
                                                    <tr>
                                                    <th scope="col">#</th>
                                                    <th scope="col" style="text-align: left;">Nombre del Estudiante</th>
                                                    <th scope="col">Nota</th>
                                                    </tr>
                                                </thead>
                                                <tbody>"""+students_desc_html+
                                                """</tbody>
                                            </table>
                                        </div>
                                        <hr />
                                    </div>
                                
                                    <div id="promedio-oculto">
                                        <h1 class="display-6"><b>Reporte AVG</b></h1>
                                        <p>Promedio de nota de los estudiantes: <b>"""+str(prom_html)+"""</b></p>
                                        <hr />
                                    </div>
                                
                                    <div id="minimo-oculto">
                                        <h1 class="display-6"><b>Reporte MIN</b></h1>
                                        <p>Nota minima: <b>"""+str(min_html)+"""</b></p>
                                        <p style="line-height: 15px;">Estudiantes con nota minima:</p>
                                        <ul>"""+students_min_html+
                                        """</ul>
                                        <hr />
                                    </div>
                                
                                    <div id="maximo-oculto">
                                        <h1 class="display-6"><b>Reporte MAX</b></h1>
                                        <p>Nota maxima: <b>"""+str(max_html)+"""</b></p>
                                        <p style="line-height: 15px;">Estudiantes con nota maxima:</p>
                                        <ul>"""+students_max_html+
                                        """</ul>
                                        <hr />
                                    </div>
                                    
                                    <div id="aprobados-oculto">
                                        <h1 class="display-6"><b>Reporte APR</b></h1>
                                        <p>Cantidad de estudiantes aprobados: <b>"""+str(contador_apr)+"""</b></p>
                                        <ul>"""+students_apr_html+
                                        """</ul>
                                        <hr />
                                    </div>
                                    
                                    <div id="reprobados-oculto">
                                        <h1 class="display-6"><b>Reporte REP</b></h1>
                                        <p>Cantidad de estudiantes reprobados: <b>"""+str(contador_rep)+"""</b></p>
                                        <ul>"""+students_rep_html+
                                        """</ul>
                                        <hr />
                                    </div>
                                </div>
                            </div>
                            <footer>
                                <p>Elias Abraham Vasquez Soto - 201900131</p>
                                <p>Practica 1 - Laboratorio Lenguajes Formales y de Programacion B-</p>        
                                <p>Facultad de Ingenieria USAC</p>
                            </footer>
                            <script>
                                function mostrarTablaASC(){
                                    var divReporteASC = document.getElementById("reportes-individuales")
                                    var tablaOcultaASC = document.getElementById("tabla-oculta-ASC")
                                    divReporteASC.innerHTML = ""
                                    divReporteASC.innerHTML = tablaOcultaASC.innerHTML
                                }
                                function mostrarTablaDESC(){
                                    var divReporteDESC = document.getElementById("reportes-individuales")
                                    var tablaOcultaDESC = document.getElementById("tabla-oculta-DESC")
                                    divReporteDESC.innerHTML = ""
                                    divReporteDESC.innerHTML = tablaOcultaDESC.innerHTML
                                }
                                function mostrarPromedio(){
                                    var divReporteAVG = document.getElementById("reportes-individuales")
                                    var divPromedio = document.getElementById("promedio-oculto")
                                    divReporteAVG.innerHTML = ""
                                    divReporteAVG.innerHTML = divPromedio.innerHTML
                                }
                                function mostrarMinimo(){
                                    var divReporteMIN = document.getElementById("reportes-individuales")
                                    var divMinimo = document.getElementById("minimo-oculto")
                                    divReporteMIN.innerHTML = ""
                                    divReporteMIN.innerHTML = divMinimo.innerHTML
                                }
                                function mostrarMaximo(){
                                    var divReporteMAX = document.getElementById("reportes-individuales")
                                    var divMaximo = document.getElementById("maximo-oculto")
                                    divReporteMAX.innerHTML = ""
                                    divReporteMAX.innerHTML = divMaximo.innerHTML
                                }
                                function mostrarAprobados(){
                                    var divReporteAPR = document.getElementById("reportes-individuales")
                                    var divAprobados = document.getElementById("aprobados-oculto")
                                    divReporteAPR.innerHTML = ""
                                    divReporteAPR.innerHTML = divAprobados.innerHTML
                                }
                                function mostrarReprobados(){
                                    var divReporteREP = document.getElementById("reportes-individuales")
                                    var divReproabdos = document.getElementById("reprobados-oculto")
                                    divReporteREP.innerHTML = ""
                                    divReporteREP.innerHTML = divReproabdos.innerHTML
                                }
                                function mostrarTodos(){
                                    var divReportes = document.getElementById("reportes-individuales")
                                    var divTodos = document.getElementById("reportes-todos")
                                    divReportes.innerHTML = ""
                                    divReportes.innerHTML = divTodos.innerHTML
                                }
                            </script>

                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
                        </body>
                        </html>""")
                        reporte_html.close()
                    except:
                        print("--> Ocurrio un error en la creación del archivo HTML")
                    try:
                        estilos_css = open('estilos.css', 'w')
                        estilos_css.write("""body {
                                background-color:rgb(4, 42, 66);
                                padding-top: 20px;
                            }

                            .datos-archivo {
                                background-color: rgb(255, 255, 255);
                                padding-top: 20px;
                                padding-bottom: 20px;
                                padding-left: 50px;
                                margin: 30px;
                            }

                            .datos-archivo h1 {
                                display: inline;
                            }

                            .tabla-estudiantes {
                                padding-top: 20px;
                                padding-left: 100px;
                                padding-right: 120px;
                                text-align: center;
                                font-family: 'Segoe UI', Verdana, Tahoma, Geneva, sans-serif;
                                font-size: 20px;
                                letter-spacing: 1px;
                            }

                            .reportes {
                                background-color: rgb(255, 255, 255);
                                padding-top: 20px;
                                padding-bottom: 20px;
                                padding-left: 50px;
                                margin: 30px;
                            }

                            .reportes h1 {
                                display: inline;
                            }

                            .reportes p {
                                text-align: left;
                                line-height: 60px;
                                font-family: 'Segoe UI', Verdana, Tahoma, Geneva, sans-serif;
                                font-size: 30px;
                                letter-spacing: 1px;
                                color: rgb(63, 61, 61);
                            }

                            .reportes ul {
                                text-align: left;
                                line-height: 60px;
                                font-family: 'Segoe UI', Verdana, Tahoma, Geneva, sans-serif;
                                font-size: 30px;
                                letter-spacing: 1px;
                                color: rgb(63, 61, 61);
                            }

                            .botones-reportes {
                                text-align: center;
                                padding: 10px;
                            }

                            .reportes-individuales {
                                text-align: center;
                                padding-left: 75px;
                                padding-right: 150px;
                                padding-top: 25px;
                            }

                            .tabla-ASC {
                                padding-top: 20px;
                                padding-left: 50px;
                                padding-right: 50px;
                                font-family: 'Segoe UI', Verdana, Tahoma, Geneva, sans-serif;
                                font-size: 20px;
                                letter-spacing: 1px;
                            }

                            .tabla-DESC {
                                padding-top: 20px;
                                padding-left: 50px;
                                padding-right: 50px;
                                font-family: 'Segoe UI', Verdana, Tahoma, Geneva, sans-serif;
                                font-size: 20px;
                                letter-spacing: 1px;
                            }

                            footer {
                                background-color: black;
                                color: white;
                                line-height: 10px;
                                text-align: center;
                                padding-top: 10px;
                                padding-bottom: 5px;
                                font-size: 15px;
                                font-family: 'Segoe UI', Verdana, Tahoma, Geneva, sans-serif;
                            }""")
                        estilos_css.close()
                    except:
                        print("--> Ocurrio un error en la creación del archivo CSS")
                    print("--> Se generó el reporte HTML correctamente.\n")
                else:
                    print("--> No se ha cargado el archivo de notas.\n")
            elif opcion == 4:
                print('--> Gracias por usar esta aplicacion :)')
                break
            else:
                print("--> El numero ingresado no corresponde a ninguna accion.\n")
        except:
            print("--> Lo ingresado no corresponde a ninguna accion.\n")