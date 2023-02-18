def el (s):
    if s==1:
        print('конвентатор КВт в грн.')
        print('останнє оновлення: 03.11.2022')
    while True:
        text=input()
        if text in ['hom', '/hom']:
            break
        a=int(text)

        if a>250.00:
            b=a*1.68
        else:
            b=a*1.44
        print(b, 'грн')

def vod (s):
    if s==1:
        print('конвертатор води в грн.')
        print('останнє оновлення: 03.11.2022')
    while True:
        text=input()
        if text in ['/hom', 'hom']:
            break
        a=int(text)

        b=a*33.12
        print (b, 'грн')

def gaz (s):
    if s==1:
        print('конвентатор газу в грн.')
        print('останнє оновлення: 03.11.2022')
    while True:
        text=input()
        if text in ['hom', '/hom']:
            break
        a=int(text)

        b=a*9.60
        print(b, 'грн')
