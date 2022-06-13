from pynput import keyboard

stack = ''
def on_press(key):
    global stack
    try:
        if isinstance(key, keyboard.KeyCode) and ('a' <= key.char <= 'z'):
            stack = stack + key.char
            stack = stack[-4:]
            if stack == 'very':
                print( 'You have used very. Please think of something better.')
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


if __name__ == "__main__":
    print('Starting listening to key pressings')
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()

