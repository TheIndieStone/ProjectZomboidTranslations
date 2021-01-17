"""
This file is a script I'm trying to make to make my work a bit faster. Still work in progress, I'm not sure if I'll improve it.
Produces a new file from which you can copy and append to the translation file you want to improve
"""
import pprint

pp = pprint.PrettyPrinter(indent=4)
file_to_translate = 'IT/ItemName_IT.txt'
english_file = file_to_translate.replace('IT', 'EN')

def make_translation_dict(path):
    file = open(path, 'r+', encoding='utf8')
    lines = [line.strip() for line in file.readlines()]
    finaldict = {line.split('=')[0].strip(' '): line.split('=')[1].strip(' ') for line in lines[1:] if '= ' in line}
    return finaldict

english = make_translation_dict(english_file)


def subtraction(t1, t2):
    finaldict = {k: "" for k in t1 if not k in t2}
    return finaldict


def translate(m):
    n = {}
    for key in m:
        eng = english[key]
        stop = False
        while True:
            print(f'Traduci: {eng.strip()} - ({key})')
            i = input()
            if i.lower() == '/stop':
                print("Smettere?")
                r = input()
                if r.lower() == "y":
                    stop = True
                    break
                elif r.lower() == "n":
                    pass
            print(f'Tradurre "{eng.replace(",", "")}" con "{i}" ({key})?')
            r = input()
            if r.lower() == "":
                n[key] = i
                print('Salvato')
                break
            elif r.lower() == "n":
                continue
            if i.lower() == '/stop':
                print("Smettere?")
                r = input()
                if r.lower() == "y":
                    stop = True
                    break
                elif r.lower() == "n":
                    pass
            else:
                pass
        if stop == True:
            break
    return n


def review(t):
    for k in t:
        print(f'La traduzione di {english[k]} è {t[k]}?')
        r = input().lower()
        if r == 'y':
            pass
        if r == 'n':
            print('Inserisci la traduzione giusta')
            n = input()
            t[k] = n


if __name__ == '__main__':
    translated = make_translation_dict(file_to_translate)
    missing = subtraction(english, translated)
    new = translate(missing)
    pp.pprint(new)
    file = open('new_for_' + file_to_translate.split('/')[1], 'w+')
    for k in new:
        file.write(f'{k} = "{new[k]}",\n')
    file.close()
