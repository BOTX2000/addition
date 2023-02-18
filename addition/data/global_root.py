from k import*
from kv import*
from codec import*
from convertatoru import*
from thametki import*
from xim_stata import*
from plosha import*
from seting import*
reset=0
def global_root(s,  r):
    while True:
        print("головне меню.")
        text=input()
        if text in ['help', '/help']:
            print('/k- викликає калькулятор на 1 дію.')
            print('/k1- викликає калькулятор на 2 дії.')
            print('/kv- викликає калькулятор квадратних рівнянь.')
            print('/bkv- викликає калькулятор біквадратних рівнянь.')
            print('/konv- викликає список конвентаторів.')
            print('/hom- повертає до цого меню, якщо використати тут то вимкне код.')
            print('/codec- викликає шифрувальну програму.')
            print('/decodec- викликає дешифрувальну програму.')
            print('/th- викликає нотатки.')
            print("/par- викликає калькулятор функції y=ax^2+bx+c.")
            print("/xim- можна дізнатися інформацію про хімічні елементи.")
            print("/er- підказка по помилкам в коді.")

        elif text in ['konv', '/konv']:
            print('/el- викликає конвентатор КВт в гривні.')
            print('/vod- викликає конвентатор води в гривні.')
            print('/gaz- викликає конвентатор газу в гривні.')

        elif text in ['hom', '/hom']:
            if s==1:
                print("Бувай!")
            reset=0
            break

        elif text in ['k', '/k']:
            k(s)

        elif text in ['k1', '/k1']:
            k1(s)

        elif text in ['kv', '/kv']:
            kv(s)

        elif text in ['bkv', '/bkv']:
            bkv(s)

        elif text in ['el', '/el']:
            el(s)

        elif text in ['vod', '/vod']:
            vod(s)

        elif text in ['gaz', '/gaz']:
            gaz(s)

        elif text in ['codec', "/cocodec"]:
            codec(s)

        elif text in ['decodec', "/decodec"]:
            decodec(s)

        elif text in ['th', '/th']:
            th(s)

        elif text in ['par', '/par']:
            parabola(s)

        elif text in ["xim", "/xim"]:
            xim(s)

        elif text in ["S", "/S"]:
            plosha(s)

        elif text in ["set", "/set"]:
            seting(s)
            reset=1
            break
        
        elif text in ["er", "/er"]:
            pom(s)

        else:
            if s==1:
                print('error 2')

    if reset==1:
        global_root(s, save, r)
