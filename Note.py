 
import pyperclip
import keyboard
import time
 
def copy_text():
    text = pyperclip.paste()
    with open('c:/python/Tools/clipboard_history.txt', 'a') as f:
        f.write(text + '\n')
    print('Text copied to clipboard history')

# copy_text()


 
 
 

copy_text()



 
 
