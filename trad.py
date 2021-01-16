"""
This file is a script I'm trying to make to make my work a bit faster. Still work in progress, I'm not sure if I'll improve it.
Produces a new file from which you can copy and append to the translation file you want to improve
"""
import pprint
pp = pprint.PrettyPrinter(indent=4)

def make_translation_dict(path):
    file = open(path, 'r+', encoding='utf8')
    lines = [line.strip() for line in file.readlines()]
    finaldict = {line.split('=')[0].strip(' ') : line.split('=')[1].strip(' ') for line in lines[1:] if '= 'in line}
    return finaldict


def subtraction(t1, t2):
    finaldict = {k : "" for k in t1 if not k in t2}
    return finaldict


def translate(m, e):
    n = {}
    for key in m:
        eng = e[key]
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
            print(f'Tradurre "{eng.replace(",","")}" con "{i}" ({key})?')
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


if __name__ == '__main__':
    translated_file = 'IT/ItemName_IT.txt'
    english_file = 'EN/ItemName_EN.txt'
    translated = make_translation_dict(translated_file)
    english = make_translation_dict(english_file)
    missing = subtraction(english, translated)
    new = translate(missing, english)
    pp.pprint(new)
    file =  open('new_for_'+translated_file.split('/')[1], 'w+')
    for k in new:
        file.write(f'{k} = "{new[k]}",\n')
    file.close()