import speech_recognition as sr
from termcolor import colored 
from recursos import banner
import os, sys, time
import webbrowser

applications = {
    'chrome': '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"',
    'brave': '"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"',
    'firefox': '"C:\\Program Files\\Mozilla Firefox\\firefox.exe"',
    'ópera': '"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"',
    'visual': '"C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"',
    'notepad': '"C:\\Windows\\notepad.exe"',
    'telegram': '"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"'
}
apps = ['chrome', 'brave', 'firefox', 'ópera', 'visual', 'notepad', 'telegram']

urls = {
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "music": "https://music.youtube.com",
    "hackthebox": "https://academy.hackthebox.com",
    "whatsapp": "https://web.whatsapp.com/",
    "kik": "https://kick.com/",
    "twitch": "https://www.twitch.tv/"
}
paginas = ['youtube', 'facebook', 'instagram', 'music', 'hackthebox', 'whatsapp', 'kik', 'twitch']


funciones = {
    'apagar': 'shutdown /s',
    'reiniciar': 'shutdown /r'    
}
comandos = ['apagar', 'reiniciar']


def salida_programa() -> None:
    print(colored("Saliendo del programa de manera forzada..", "red"))
    os.system("cls")
    sys.exit(1)
    
def abrir_aplicaciones(text) -> None:
    
    text = text.lower()
    frases = text.split()
    
    for n in apps:
        for frase in frases:
            if frase == n:
                os.system(applications[frase])
                os.system("cls")

        
def entrar_link(text) -> None:        
    text = text.lower()
    frases = text.split()

    for n in paginas:
        for frase in frases:
            if frase == n:
                webbrowser.open_new_tab(urls[frase])
                os.system("cls")


def funcion_dispositivo(text) -> None:
    text = text.lower()
    frases = text.split()
    
    for n in comandos:
        for frase in frases:
            if frase == n:
                os.system(funciones[frase])
                os.system("cls")

if __name__ == "__main__":
    try:
        while True:
            banner.banner()
            try:
                r = sr.Recognizer()
                text = ""
                time.sleep(1)
                with sr.Microphone() as source:
                    print("Que necesitas?: ")
                    
                    audio = r.listen(source)
                    text = r.recognize_google(audio, language='es-ES')
                    
                    print(text)
                    if "aplicación" in text:
                        abrir_aplicaciones(text)
                    
                    elif "link" in text:
                        entrar_link(text)
                        
                    elif "función" in text:
                        funcion_dispositivo(text)
                        
                    elif 'salir' in text.lower():
                        exit(0)
                        
                    else:
                        os.system("cls")
                        continue
                    
            except sr.UnknownValueError:
                print("No se entiende lo que dices")
                os.system("cls")
                continue    

    except KeyboardInterrupt:
        salida_programa()
        
        

        


