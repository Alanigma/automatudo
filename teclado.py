import pynput
from pynput.keyboard import Key, Controller
from pynput import keyboard

linguagem = 'python'
tecla = ''
comando = ''
primeiro = True
segundo = False
frase = 'nada'
etapa = 0
controle = Controller()

def executar():
    global frase
    global etapa
    if etapa == 0:
        print('Qual comando executar?\n[f] For\n[w] While')
        etapa = 1

def on_press(key):
    global linguagem
    global etapa
    global comando
    global tecla
    global primeiro
    global segundo

    if etapa == 1:
        try:
            if key.char == 'f':
                controle.press(Key.backspace)
                controle.release(Key.backspace)
                if linguagem == 'python':
                    controle.type('for c in range ():\n\t')
                if linguagem == 'c':
                    controle.type('for (c = 0; c < 10; ++c)\n{\n\t\n}')
                etapa = 0
            elif key.char == 'w':
                controle.press(Key.backspace)
                controle.release(Key.backspace)
                if linguagem == 'python':
                    controle.type('while True:\n\t')
                if linguagem == 'c':
                    controle.type('while (1 == 1)\n{\n\t\n}')
                etapa = 0
            else:
                print('comando cancelado')
                etapa = 0
        except:
            print('comando cancelado')
            etapa = 0

    if key == tecla:
        executar()
    if primeiro == True:
        tecla = key
        print(f'{key} definido como tecla de execução\nselecione uma linguagem:\n[p] Python\n[c] C')
        primeiro = False
        segundo = True
    elif segundo == True:
        try:
            if key.char == 'c':
                controle.press(Key.backspace)
                controle.release(Key.backspace)
                linguagem = 'c'
                print('C selecionado')
            if key.char == 'p':
                controle.press(Key.backspace)
                controle.release(Key.backspace)
                print('Python selecionado')
            segundo = False
        except:
            segundo = False
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()