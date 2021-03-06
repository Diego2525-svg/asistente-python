import pyttsx3 #pip
import speech_recognition as sr #pip
import datetime
import wikipedia #pip
import webbrowser #pip
import os
import random
import pywhatkit#pip
opcion=int
opcion=random.randrange(10)
parlante = pyttsx3.init("sapi5")#define parlante
voices= parlante.getProperty("voices")
voices= parlante.setProperty("voz", voices[1].id)
usuario=("Diego")

asis=True
print ("Iniciando asistente")
#Funcion para que el asistente hable
def hablar (text):
    parlante.say(text)
    parlante.runAndWait()
#Funcion para la hora y la bienvenida
def Buenas():
    hora=int(datetime.datetime.now().hour)
    print(hora)
    if hora>=0 and hora<12:
        hablar("Buenos dias"+ usuario+"...")
    elif hora>=12 and hora<18:
        hablar("Buenas tardes"+ usuario+"...")
    else:
        hablar("Buenas noches"+ usuario+"...")
#Funcion para recepcion de ordenes
def recibir():
    r=sr.Recognizer()
    with sr.Microphone() as recurso:
        print("Escuchando instrucciones")
        audio=r.listen(recurso)
    try:
        print("Reconociendo instruccion")
        ins=r.recognize_google (audio)
        print("Se entendio ",ins)
        asis==True
    except Exception:
        print("No se entendio ninguna instruccion")
        ins=None
    return ins  
hablar ("Iniciando asistente...")   
Buenas()     
while asis==True:
#poner aqui while para mantener el asistente activo
 print("Escuchando instrucciones")
 ins = recibir()
#Inicio busqueda wikipedoa
 if "wikipedia" in ins.lower():
     hablar("Que desea buscar en wikipedia...")
     ins=ins.replace("wikipedia","")
     resultado= wikipedia.summary(ins,sentences=2)
     print(resultado)
     hablar(resultado)
#Cambiar a español
#Fin busqueda wikipedia
#Inicio hora
 elif "hora" in ins.lower():
     tiempo=datetime.datetime.now().strftime("%H:%M:%S")
     hablar(usuario+"la hora es"+tiempo+"...")
     print(usuario+"la hora es"+tiempo+"...")
#Fin hora
#Inicio recomendaciones de musica de youtube
 elif"musica" in ins.lower():
    print(opcion)
    if opcion==0:
     webbrowser.open("https://www.youtube.com/watch?v=PzlVjgKzyBY")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==1:
     webbrowser.open("https://www.youtube.com/watch?v=hUq6KNkZcUY")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==2:
     webbrowser.open("https://www.youtube.com/watch?v=x4-ZD1mvzUI")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==3:
     webbrowser.open("https://www.youtube.com/watch?v=k8U8gjFx9Vk")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==4:
     webbrowser.open("https://www.youtube.com/watch?v=k8U8gjFx9Vk")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==5:
     webbrowser.open("https://www.youtube.com/watch?v=iqxoJuY-T_E")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==6:
     webbrowser.open("https://www.youtube.com/watch?v=nZfmAFB5cgY")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==7:
     webbrowser.open("https://www.youtube.com/watch?v=CIZ5S2cgh0Y")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==8:
     webbrowser.open("https://www.youtube.com/watch?v=HkbG39-T4H0")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==9:
     webbrowser.open("https://www.youtube.com/watch?v=lj4O63Swowo")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    elif opcion==10:
     webbrowser.open("https://www.youtube.com/watch?v=DkX5Hzzb9N4")
     hablar("Que te parece esta sugerencia"+usuario+"...")
    else:
     hablar("En estos momentos no se me ocurre ninduna sugerencia...")
#Fin recomendaciones musica Youtube
#Inicio Abrir paginas web
 elif "youtube" in ins.lower():
     webbrowser.open("https://www.youtube.com")
     hablar("Abriendo Youtube...")
 elif"facebook" in ins.lower():
     webbrowser.open("https://www.facebook.com")
     hablar("Abriendo Facebook...")
 elif "esemtia" in ins.lower():
     webbrowser.open("https://edu.esemtia.ec/LoginEsemtia.aspx")
     hablar("Abriendo esemtia...")
 elif "moodle" in ins.lower():
     webbrowser.open("https://tecnicosalesiano.esemtia.net/moodle/login/index.php")
     hablar("Abriendo moodle...")
 #Fin abrir paginas web
 #Inicio reproducir musica
 elif "escuchar" in ins.lower():
     cancion=ins.replace("escuchar")
     hablar ("reproduciiendo" + cancion)
     pywhatkit.playonyt(cancion)
 #Fin reproducir musica
 #Inicio abrir carpetas
 elif "soporte" in ins.lower() :
     os.startfile("C:\\Users\\DAVID.LAPTOP-R39HS99T.000\\Desktop\\Soporte Tecnico")
     hablar("Abriendo carpeta de soporte tecnico...")
 elif "programacion" in ins.lower():
     os.startfile("C:\\Users\\DAVID.LAPTOP-R39HS99T.000\\Desktop\\Programacion")
     hablar("Abriendo carpeta de programacion...")
 elif "web"  in ins.lower():
     os.startfile("C:\\Users\\DAVID.LAPTOP-R39HS99T.000\\Desktop\\Diseño y Desarollo web")
     hablar("Abriendo carpeta de diseño web...")
 elif "biologia" in ins.lower():
     os.startfile("C:\\Users\\DAVID.LAPTOP-R39HS99T.000\\Desktop\\Biologia")
     hablar("Abriendo carpeta de biologia...")
 elif "ciudadania" in ins.lower():
     os.startfile("C:\\Users\\DAVID.LAPTOP-R39HS99T.000\\Desktop\\Ciudadania")
     hablar("Abriendo carpeta de ciudadania...")
 elif "fisica" in ins.lower():
     os.startfile("C:\\Users\\DAVID.LAPTOP-R39HS99T.000\\Desktop\\Fisica")
     hablar("Abriendo carpeta de fisica...")
 elif "historia" in ins.lower():
     os.startfile("C:\\Users\\DAVID.LAPTOP-R39HS99T.000\\Desktop\\Historia")
     hablar("Abriendo carpeta de historia...")
 elif "ingles" in ins.lower():
     os.startfile("C:\\Users\\DAVID.LAPTOP-R39HS99T.000\\Desktop\\Ingles")
     hablar("Abriendo carpeta de ingles...")
 #Fin abrir carpetas
 #Finalizar
 elif "desactivar" in ins.lower():
     hablar("Hasta la proxima")
     asis==False