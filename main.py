from tkinter import filedialog, Tk

def abrirArchivo():
    archivo = filedialog.askopenfile(
        title = "Seleccionar archivo LFP",
        initialdir = "./",
        filetypes = {
            ("Archivos LFP", "*.lfp"),
            ("Todos los archivos", "*.*")
        }
    )
    texto = archivo.read()
    archivo.close()
    print('Lectura exitosa')
    return(texto)

if __name__ == '__main__':
    print('Commit no vacío')