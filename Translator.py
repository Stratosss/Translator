# Offline Translator
from translate import Translator
from deep_translator import GoogleTranslator
import tkinter.filedialog
import tkinter as tk

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

if Q==1:
    try:
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        my_file = tkinter.filedialog.askopenfile(mode='r')
        x = my_file.read()
        translator = Translator(to_lang="el")
        translation = translator.translate(x)                      #translate a text
        # translation = translator.translate("This is a pen.")     #translate a sentence
        print(translation)
        while True:
            query = input("Do you want to save the translated file (Y/N)? ")
            if query.upper() == "Y":
                with open("Translated_file.txt", "w", encoding="utf-8") as new_file:
                    for line in translation:
                        new_file.write(line)
                    break
            elif query.upper() == "N":
                break
            else:
                print("Please time Y or N to continue...")
    except AttributeError:
        print("No file was selected. App will now terminate.")
else:
    try:
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        my_file = tkinter.filedialog.askopenfile(mode='r')
        x = my_file.read()
        to_translate = x
        translation= GoogleTranslator(source='auto', target='el').translate(to_translate)
        print(translation)
        while True:
            query = input("Do you want to save the translated file (Y/N)? ")
            if query.upper() == "Y":
                with open("Translated_file.txt", "w", encoding="utf-8") as new_file:
                    for line in translation:
                        new_file.write(line)
                    break
            elif query.upper() == "N":
                break
            else:
                print("Please time Y or N to continue...")
    except AttributeError:
        print("No file was selected. App will now terminate.")
   

    

