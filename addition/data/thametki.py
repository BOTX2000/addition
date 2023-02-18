def thp (s):
    a=0
    if s==1:
        print('нотатки.')
    while True:
        if s==1:
            text=input('нова нотатка: ')
        else:
            text=input()
        if text in ['/hom']:
            file.close()
            break

        while True:
            try:
                file=open(f"{adres[a]}thametki.txt", "a", encoding="utf-8")
                a=0
                break
            except:
                a+=1
                
        try: 
            file.write(text)
            file.write("\n")
        except:
            print("error 0.3")


def thr (s):
    a=0
    while True:
        try:
            file=open(f"{adres[a]}thametki.txt", "r", encoding="utf-8")
            a=0
            break
        except:
            a+=1

    try:
        text=file.read()
        print(text)
        file.close()
    except:
        print("error 0.3")

def th (s):
    if s==1:
        print('нотатки')
        print('+ додати нотатку.')
        print('read побачити усі нотатки.')
    while True:
        text=input()
        if text in ['hom', '/hom']:
            break
        elif text in ['+']:
            thp(s)
            print('нотатки')
        elif text in ['read', '/read']:
            thr(s)
            print('нотатки')

adres=["/storage/emulated/0/addition/cache/", "E:/Pyton/addition/cache/", "F:/Pyton/addition/cache/", "D:/addition/cache/", "C:/addition/cache/"]
