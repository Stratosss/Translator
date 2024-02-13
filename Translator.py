from translate import Translator
from deep_translator import GoogleTranslator
import tkinter.filedialog as fd
import tkinter as tk

def save_function():
    while True:
            query = input("Do you want to save the translated file (Y/N)? ")
            if query.upper() == "Y":
                new_file = fd.asksaveasfile(defaultextension=".txt", title="Save As",
                                       filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
                
                new_file_path = new_file.name
                with open(f"{new_file_path}", "w",  encoding="utf-8") as save_file:
                    for line in translation:
                        save_file.write(line)
                print(f"File was saved on {new_file_path}")
                break  
            elif query.upper() == "N":
                break
            else:
                print("Please time Y or N to continue...")


while True:
    Q=input('Which method do you wish to use? (type 1 for Offline Translator or 2 for Online Translator): ')
    try:
        Q=int(Q)
        if Q == 1 or Q == 2:
            break
        else:
            print("Please give the right value")
    except Exception:
        continue

if Q==1:            # Offline Translator
    try:
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        my_file = fd.askopenfile(mode='r')
        x = my_file.read()
        translator = Translator(to_lang="el")
        translation = translator.translate(x)                      #translate a text
        # translation = translator.translate("This is a pen.")     #translate a sentence
        print(translation)
        save_function()
    except AttributeError:
        print("No file was selected. App will now terminate.")
else:
    try:                # Google Translator
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        my_file = fd.askopenfile(mode='r')
        x = my_file.read()
        to_translate = x
        translation= GoogleTranslator(source='auto', target='el').translate(to_translate)
        print(translation)
        save_function()
    except AttributeError:
        print("No file was selected. App will now terminate.")
   

    

