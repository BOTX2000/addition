from perevod import*
from math import*
from perevod_kv import*
def kv (s) :
    if s==1:
        print('калькулятор квадратних рівнянь.')
    while True:
        text=input()
        if text in ['hom', '/hom']:
            break
        text1=perevodk(text)
        a=int(text1[0])
        b=int(text1[1])
        c=int(text1[2])

        D=b**2-4*a*c
        if D<0:
            print("коренів не існує.")
        else:
            k=sqrt(D)
            if D==0:
                h =-b/(2*a)
                print('х=', h)
            if D>0:
                p =(-b+k)/(2*a)
                o =(-b-k)/(2*a)
                print('х1=', p, 'х2=', o)

def bkv (s):
    if s==1:
        print('калькулятор біквадратних рівнянь.')
    while True:
        text=input()
        if text in ['hom', '/hom']:
            break
        text1=perevodk(text)
        a=int(text1[0])
        b=int(text1[1])
        c=int(text1[2])

        D=b**2-4*a*c
        if D<0:
            print("коренів не існує.")
        else:
            k=sqrt(D)
            if D==0:
                h =-b/(2*a)
                print('х1=√', h)
                print('x2=-√', h)
            if D>0:
                p =(-b+k)/(2*a)
                o =(-b-k)/(2*a)
                print('x1= √', p)
                print('x2= -√', p)
                print('x3= √', o)
                print('x4= -√', o)

def parabola(s):
    if s==1:
        print("функція y=ax^2+bx+c [непрацює до кінця]")
    while True:
        command=input()
        if command in ["hom"]:
            break
        text1=perevod_par(command)
        text3=ybrat_x(command)
        text4=ybrat_x_1(text3)
        di=len(text4)
        a=int(text1[0])
        b=int(text1[1])
        c=int(text1[2])
        if a<0:
            print("гілки спрямовано вниз.")
        elif a>0:
            print("гілки спрямовано вгору.")
        else:
            print("це не парабола.")
            break
        x=-(b/2*a)
        y=4*a*c-b**2/4*a
        print("точки вершини:")
        print("x=", x)
        print("y=", y)
        print("точка перетину з віссю х:")
        if di==2:
            print(text4[0])
            if "+"==text4[0]:
                if "+"==text4[1]:
                    print(a*0**2+b*0+c)
                if "-"==text4[1]:
                    print(a*0**2+b*0-c)
                else:
                    print("1/")
            if "-"==text4[0]:
                if "+"==text4[1]:
                    print(a*0**2-b*0+c)
                if "-"==text4[1]:
                    print(a*0**2-b*0-c)
                else:
                    print("2/")
            else:
                print("3/")
        else:
            if "+"==text4[0]:
                if "+"==text4[1]:
                    print(-a*0**2+b*0+c)
                if "-"==text4[1]:
                    print(-a*0**2+b*0-c)
                else:
                    print("4/")
            if "-"==text4[0]:
                if "+"==text4[1]:
                    print(-a*0**2-b*0+c)
                if "-"==text4[1]:
                    print(-a*0**2-b*0-c)
                else:
                    print("5/")
            else:
                print("6/")
