from translate import Translator
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException
import tkinter.filedialog as fd
import tkinter as tk

VALID_LANGUAGE_CODES = {
    'en', 'es', 'fr', 'de', 'it', 'pt', 'nl', 'ru', 'zh', 'ja', 'ko',
    'ar', 'tr', 'pl', 'cs', 'sv', 'da', 'fi', 'no', 'he', 'el', 'hi',
    'id', 'th', 'uk', 'vi', 'fa', 'ro', 'bg', 'ms', 'sr', 'hu', 'sk',
    'lt', 'lv', 'et', 'sl', 'hr', 'bn', 'ta', 'te', 'ml', 'mr', 'gu',
    'ur', 'pa', 'kn', 'sw', 'am', 'my', 'ne', 'si', 'km', 'lo', 'mn',
    'ka', 'hy', 'az', 'be', 'bs', 'gl', 'eu', 'is', 'mt', 'ga', 'cy'
}

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

def input_validation(Q):
    while True:
        if Q == 1:
            from_lang = input("Please give a language to translate from: ").strip().lower()
            to_lang = input("Please give a language to translate to: ").strip().lower()
            if all(lang in VALID_LANGUAGE_CODES for lang in (from_lang,to_lang)):
                return from_lang, to_lang
            print(f"please input correct language codes from the list: {VALID_LANGUAGE_CODES} ")
        else:
            to_lang = input("Please give a language to translate to: ").strip().lower()
            return to_lang
         
    
while True:
    Q=input('Which method do you wish to use? (type 1 for Offline Translator or 2 for Online Translator): ')
    try:
        Q=int(Q)
        if Q == 1: 
            from_lang, to_lang = input_validation(Q)
            break
        elif Q == 2:
            to_lang = input_validation(Q)
            break
        else:
            print("Please give the right value")
    except Exception as e:
        print(e)
        continue

if Q==1:                #Offline Translator
    while True:
        try:
            root = tk.Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            file_path = fd.askopenfilename()
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as my_file:
                    x = my_file.read()
                    if len(x)>500:
                        print(f"offline translator has a limit of up to 500 characters, current character number: {len(x)} \nThe app will now terminate.")
                        break
            translator = Translator(to_lang=f"{to_lang}", from_lang=f"{from_lang}")
            translation = translator.translate(x)                      #translate a text
            print(translation)
            save_function()
            break
        except AttributeError as e:
            print("No file was selected. The app will now terminate.")
            print(e)
            break
else:
    while True:
        try:                #Google Translator
            root = tk.Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            file_path = fd.askopenfilename()
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as my_file:
                    x = my_file.read()
            translation= GoogleTranslator(source='auto', target=f"{to_lang}").translate(x)
            print(translation)
            save_function()
            break
        except AttributeError:
            print("No file was selected. The app will now terminate.")
            break
        except LanguageNotSupportedException  as e:
            print(e)
            to_lang = input_validation(2)
            continue
    

    

