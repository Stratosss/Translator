# Offline Translator
from translate import Translator
from deep_translator import GoogleTranslator

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
        with open("\\Users\\thand\\Desktop\\test.txt") as my_file:
            x = my_file.read()
            translator = Translator(to_lang="el")
            translation = translator.translate(x)                      #translate a text
            print(translation)
    except FileNotFoundError as err:
        print("File not found in that directory:", err)
else:
    try:
        with open("\\Users\\thand\\Desktop\\test.txt") as my_file:
            x = my_file.read()
            to_translate = x
            translated = GoogleTranslator(source='auto', target='el').translate(to_translate)
            print(translated)
    except FileNotFoundError as err:
        print("File not found in that directory:", err)

    

