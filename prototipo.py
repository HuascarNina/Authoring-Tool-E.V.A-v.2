# Importamos la biblioteca Tkinter para poder crear la interfaz de usuario
from tkinter import *
from urllib.request import *
from PIL import Image, ImageTk

# Creamos la ventana principal de la aplicación
root = Tk()
root.wm_title("Authoring Tool")

# Especificamos el ancho y alto de la ventana en píxeles
root.geometry("400x400")

# Creamos un canvas para insertar la imagen
imagen = Canvas(root)
imagen.pack()

# Definimos la URL de la imagen que queremos descargar
urlImagen = "https://ipfs.io/ipfs/QmdA8TNjLrukkE1vCNh5avaqnsBSqKorBNkCayzQuqBKAr?filename=derechos-de-autor.png"

# Descargamos la imagen y la guardamos en la ruta especificada
urlretrieve(urlImagen, "C:/Users/Huascar Nina/Desktop/E.V.A Segundo proyecto/imagen1.png")

# Creamos una etiqueta para mostrar un mensaje en la ventana
label = Label(root, text="Hola! Bienvenido a nuestro authoring tool para crear cuestionarios")
label.place(x=15,y=10)

# Creamos una caja de texto donde el usuario puede escribir la pregunta del cuestionario
labelQuestion = Label(root, text="Ingresa tu pregunta: ")
labelQuestion.place(x=15,y=60)
question_text = StringVar()
labelAnswer = Label(root, text="Ingresa tu respuesta: ")
labelAnswer.place(x=15,y=110)
question_input = Entry(root, textvariable=question_text)
question_input.config(width=35)
question_input.place(x=150,y=60)
answer_text = StringVar()
answer_input = Entry(root, textvariable=answer_text)
answer_input.config(width=35)
answer_input.place(x=150,y=110)


# Creamos una lista donde se almacenarán las preguntas y las opciones de respuesta del cuestionario
quiz = []

# Creamos una función que se ejecutará cuando se presione el botón de "Añadir pregunta y opciones de respuesta"

def add_to_quiz():
    # Obtenemos el texto de la pregunta y las opciones de respuesta
    question = question_text.get()
    answer = answer_text.get()

    if question != "" and answer != "" :
        # Agregamos la pregunta y las opciones de respuesta a la lista del cuestionario
        quiz.append((question, answer))

        # Limpiamos la caja de texto para la siguiente pregunta y opciones de respuesta
        question_text.set("")
        answer_text.set("")

        ventana = Tk()
        etiqueta = Label(ventana, text="Se agrego con exito")
        etiqueta.pack()
    else:
        ventana = Tk()
        etiqueta = Label(ventana, text="Alguno de los campos no se completo")
        etiqueta.pack()

def erase_quiz():
    if len(quiz) != 0 :
        ventana = Tk()
        quiz.clear()
        etiqueta = Label(ventana, text="Se vacio el cuestionario con exito")
        etiqueta.pack()
    else:
        ventana = Tk()
        etiqueta = Label(ventana, text="El cuestionario se encuentra vacio")
        etiqueta.pack()

def see_quiz():
    if len(quiz) == 0:
        ventana = Tk()
        etiqueta = Label(ventana, text="El cuestionario se encuentra vacio")
        etiqueta.pack()
    else:
        ventana = Tk()
        for elemento in quiz:
            etiqueta = Label(ventana, text=elemento)
            etiqueta.pack()

def go_scrom():
    if len(quiz) == 0:
        ventana = Tk()
        etiqueta = Label(ventana, text="El cuestionario se encuentra vacio")
        etiqueta.pack()
    else:
        ventana = Tk()
        etiqueta = Label(ventana, text="El paquete SCROM esta listo!")
        etiqueta.pack()

# Creamos un botón que permite al usuario agregar la pregunta y las opciones de respuesta al cuestionario
add_button = Button(root, text="Añadir pregunta y respuesta", command=add_to_quiz)

# Creamos un botón que permite al usuario eliminar todas las preguntas y respuestas al cuestionario
erase_button = Button(root, text="Vaciar cuestionario", command=erase_quiz)

# Creamos un botón que permite al usuario eliminar todas las preguntas y respuestas al cuestionario
see_quiz_button = Button(root, text="Ver cuestionario", command=see_quiz)

# Creamos un botón que permite al usuario eliminar todas las preguntas y respuestas al cuestionario
go_scrom_button = Button(root, text="Convertir a SCROM", command=go_scrom)

# Empaquetamos el botón
add_button.place(x=200,y=160)

# Empaquetamos el botón
erase_button.place(x=200,y=210)

# Empaquetamos el botón
see_quiz_button.place(x=200,y=260)

# Empaquetamos el botón
go_scrom_button.place(x=200,y=310)

# Carga la imagen original
original_image = Image.open("imagen1.png")

# Redimensiona la imagen a un tamaño de 200x200
resized_image = original_image.resize((100, 100))

# Crea una imagen Tkinter a partir de la imagen redimensionada
tk_image = ImageTk.PhotoImage(resized_image)

# Crea una etiqueta Tkinter y asigna la imagen redimensionada
labelImage = Label(root, image=tk_image)
labelImage.place(x=40, y=200)

# Iniciamos el bucle principal de la aplicación para que se ejecute hasta que se cierre la ventana
root.mainloop()