from global_normal import*
from global_root import*

def pom(s):
    print("error 0.0 - помилка збережених налаштувань.")
    print("error 0.1 - помилка при перестворені налаштувань.")
    print("error 0.2 - помилка при перестворені налаштувань.")
    print("error 0.3 - помилка при створен/читанні нотаток.")
    print("error 1 - введено не коректні данні.")
    print("eroor 2 - невірна команда.")
    print("error 3 - зміна налаштувань не вдалася.")




    

def seting(s):
    a=0
    while True:

        print("1. відображати назву модулю")
        text=input()
        print("вводити тільки англійські 'T' та 'F'.")
        print("T - так.")
        print("F - ні.")
        if text==1:
            sot=input()
            if sot=="T":
                sat="True"
            elif sot=="F":
                sat="False"
            while True:
                try:
                    n1=open(f"{adres[a]}n1.txt", "w")
                    a=0
                    break
                except:
                    a+=1
            try:
                n1.write(sat)
                n1.close()
            except:
                print("error 3")

        elif text in ["hom", "/hom"]:
            break
        
def reset():
    a=0
    while True:
        try:
            n1=open(f"{adres[a]}n1.txt", "w")
            a=0
            break
        except:
            a+=1

    try:
        n1.write("True")
        n1.close()
    except:
        error=input("введіть адресу до файлів налаштування: ")
        try:
            n1=open(f"{error}/n1.txt", "w")
            n1.write("True")
            n1.close()
        except:
            print("error 0.2")
    
    while True:
        try:
            root=open(f"{adres[a]}/root.txt", "w")
            a=0
            break
        except:
            a+=1

    try:
        root.write("False")
        root.close()
    except:
        try:
            root=open(f"{error}/root.txt", "w")
            root.write("False")
            root.close()
        except:
            print("error 0.1")

def go():
    a=0
    while True:
        try:
            root=open(f"{adres[a]}root.txt", "r")
            a=0
            break
        except:
            a+=1

    try:
        Root=root.read()
        root.close()
    except:
        reset()

    while True:
        try:
            n1=open(f"{adres[a]}n1.txt", "r")
            a=0
            break
        except:
            a+=1

    try:
        nn1=n1.read()
        n1.close()
    except:
        reset()
        
    if nn1=="True":
        s=1
    elif nn1=="False":
        s=0
    else:
        reset()
    if Root=="True":
        r=1
        global_root(s, r)
    elif Root=="False":
        r=0
        while True:
            try:
                global_root(s, r)
                break
            except:
                print("error 1")
    else:
        print("error: 0.0")
        print("будьласка перезапустіть код.")
        reset()
        return()

adres=["/storage/emulated/0/addition/data/", "E:/Pyton/addition/data/", "C:/addition/data/", "D:/addition/data/", "F:/Pyton/addition/data/"]
