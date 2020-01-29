from pynput.keyboard import Listener, Key

def press(key):
    print(key)

def release(key):
    pass

with Listener(on_press=press, on_release=release) as listener:
    listener.join(

    )