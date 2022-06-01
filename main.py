# Instalar Biblioteca: SpeechRecognition, pyttsx3, PyAudio

#Bibliotecas

import speech_recognition as sr # Serve para reconhecimento de voz
import pyttsx3 # Serve para sintetizador de voz
import datetime # Serve para ter informação da data e hora
import wikipedia # Serve para buscar qualquer informação da wikipeida
import pywhatkit # Serve para assistir/ouvir musica e video

#Configuração do sistema

audio = sr.Recognizer() # Para receber o audio do usuario e reconhecer
maquina = pyttsx3.init() # iniciando a IA
maquina.say('Olá, eu sou a renata') # say é o metodo para a IA falar
maquina.say('Como posso ajudar?')
maquina.runAndWait() # Metodo para execultar a fala da IA

def executa_comando():

    # Bloco para conferir se a IA esta ouvindo

    try:

        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source) # Escultar o usuario
            comando = audio.recognize_google(voz, language = 'pt_BR') # A IA entender oque estamos pedindo
            comando = comando.lower() # Tudo oq o usuario falou se transformar em texto e as letras minuscula
            print(comando)

    except:

        print('Microfone não esta ok')

    return comando

def comando_usuario():


    comando = executa_comando()
    if 'horas' in comando:

        try:

            hora = datetime.datetime.now().strftime('%H:%M') # strftime formata a hora que vai ser falado
            maquina.say('Agora são' + hora)
            maquina.runAndWait()

        except:

            maquina.say('Desculpa não entendi')
            maquina.runAndWait()


    elif 'procure por' in comando:

        try:

            procurar = comando.replace('procure por', '')
            wikipedia.set_lang('pt') # para a IA pegar a pesquisa em pt (brasileiro)
            resultado = wikipedia.summary(procurar, 2) # metodo summary é pra falar pouca coisa no caso '2' linha da pesquisa
            print(resultado)
            maquina.say(resultado)
            maquina.runAndWait()

        except:

            maquina.say('Desculpa não entendi')
            maquina.runAndWait()

    elif 'toque' in comando:

            try:

                musica = comando.replace('toque', '')
                resultado = pywhatkit.playonyt(musica) # metodo playonyt ira pesquisar e tocar musica
                maquina.say('Tocando música')
                maquina.runAndWait()

            except:

                maquina.say('Desculpa não entendi')
                maquina.runAndWait()

    elif 'não obrigado' in comando:

        try:

            maquina.say('Tchau foi um prazer te ajudar')
            maquina.runAndWait()
            global controle
            controle = False

        except:

            maquina.say('Desculpa não entendi')
            maquina.runAndWait()


controle = True

while controle:

    try:

        comando_usuario()

        if controle == True:

            maquina.say('Posso te ajudar novamente?')
            maquina.runAndWait()

    except:

        maquina.say('Tchau foi um prazer te ajudar')
        maquina.runAndWait()
        controle = False