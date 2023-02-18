from perevod import*
def k(s):
    if s==1:
        print('калькулятор на 1 дію.')
    while True:
        text=input()
        if text in ['hom', '/hom']:
            break
        text1=perevod(text)
        di=text
        di1=perevod1(di)
        c=0
        a=int(text1[0])
        b=int(text1[1])
        dii=di1[0]
        if dii in [ '/', ':', '÷'] and b==0:
            print('Ділити на нуль не можна!')
        else :
            if  dii=='+':
                c=a+b
            elif dii=='-':
                c=a-b
            elif dii in ['/', ':', '÷']:
                c=a/b
            elif dii in ['*', '×', '•']:
                c=a*b
            elif dii in ['^', '**']:
                c=a**b
            elif dii=="+-":
                c=a-b
            elif dii=="--":
                c=a+b
            elif dii in ["/-", ":-", "÷-"]:
                c=a/(-b)
            elif dii in ['*-', '×-', '•-']:
                c=a*(-b)
            elif dii in ['^-', '**-']:
                c=a**(-b)
            print (text, '=', c)

def k1 (s):
    if s==1:
        print('калькулятор на 2 дії.')
        while True:
            text=input()
            if text in ['hom', '/hom']:
                break
            di=text
            text1=perevod(text)
            di1=perevod1(di)
            a=int(text1[0])
            b=int(text1[1])
            c=int(text1[2])
            dii=di1[0]
            dii1=di1[1]

            if b==0 and dii==['/', ':', '÷'] or c==0 and dii1==['/', ':', '÷']:
                print('Ділити на нуль не можна.')
            else:
                if dii=='+':
                    if dii1=='+':
                        d=a+b+c
                    if dii1=='-':
                        d=a+b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a+b/c
                    if dii1 in ['*', '×', '•']:
                        d=a+b*c
                    if dii1 in ["^", "**"]:
                        d=a+b**c
                elif dii=='-':
                    if dii1=='+':
                        d=a-b+c
                    if dii1=='-':
                        d=a-b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a-b/c
                    if dii1 in ['*', '×', '•']:
                        d=a-b*c
                    if dii1 in ['^', "**"]:
                        d=a-b**c
                elif dii in ['/', ':', '÷']:
                    if dii1=='+':
                        d=a/b+c
                    if dii1=='-':
                        d=a/b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a/b/c
                    if dii1 in ['*', '×', '•']:
                        d=a/b*c
                    if dii1 in ['^', "**"]:
                        d=a/b**c
                elif dii in ['*', '×', '•']:
                    if dii1=='+':
                        d=a*b+c
                    if dii1=='-':
                        d=a*b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a*b/c
                    if dii1 in ['*', '×', '•']:
                        d=a*b*c
                    if dii1 in ["**", "^"]:
                        d=a*b**c
                elif dii in ["^", "**"]:
                    if dii1=='+':
                        d=a**b+c
                    if dii1=='-':
                        d=a**b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a**b/c
                    if dii1 in ['*', '×', '•']:
                        d=a**b*c
                    if dii1 in ["**", "^"]:
                        d=a**b**c
#кольсь зробити закоментований уривок коду!!!!!!!!!!!!!! 
                        """
#- на 1-ом уровне 
                if dii=='+':
                    if dii1=='+':
                        d=a+b+c
                    if dii1=='-':
                        d=a+b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a+b/c
                    if dii1 in ['*', '×', '•']:
                        d=a+b*c
                    if dii1 in ["^", "**"]:
                        d=a+b**c
                elif dii=='-':
                    if dii1=='+':
                        d=a-b+c
                    if dii1=='-':
                        d=a-b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a-b/c
                    if dii1 in ['*', '×', '•']:
                        d=a-b*c
                    if dii1 in ['^', "**"]:
                        d=a-b**c
                elif dii in ['/', ':', '÷']:
                    if dii1=='+':
                        d=a/b+c
                    if dii1=='-':
                        d=a/b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a/b/c
                    if dii1 in ['*', '×', '•']:
                        d=a/b*c
                    if dii1 in ['^', "**"]:
                        d=a/b**c
                elif dii in ['*', '×', '•']:
                    if dii1=='+':
                        d=a*b+c
                    if dii1=='-':
                        d=a*b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a*b/c
                    if dii1 in ['*', '×', '•']:
                        d=a*b*c
                    if dii1 in ["**", "^"]:
                        d=a*b**c
                elif dii in ["^", "**"]:
                    if dii1=='+':
                        d=a**b+c
                    if dii1=='-':
                        d=a**b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a**b/c
                    if dii1 in ['*', '×', '•']:
                        d=a**b*c
                    if dii1 in ["**", "^"]:
                        d=a**b**c
#- на 2-ом уровне 
                if dii=='+':
                    if dii1=='+':
                        d=a+b+c
                    if dii1=='-':
                        d=a+b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a+b/c
                    if dii1 in ['*', '×', '•']:
                        d=a+b*c
                    if dii1 in ["^", "**"]:
                        d=a+b**c
                elif dii=='-':
                    if dii1=='+':
                        d=a-b+c
                    if dii1=='-':
                        d=a-b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a-b/c
                    if dii1 in ['*', '×', '•']:
                        d=a-b*c
                    if dii1 in ['^', "**"]:
                        d=a-b**c
                elif dii in ['/', ':', '÷']:
                    if dii1=='+':
                        d=a/b+c
                    if dii1=='-':
                        d=a/b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a/b/c
                    if dii1 in ['*', '×', '•']:
                        d=a/b*c
                    if dii1 in ['^', "**"]:
                        d=a/b**c
                elif dii in ['*', '×', '•']:
                    if dii1=='+':
                        d=a*b+c
                    if dii1=='-':
                        d=a*b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a*b/c
                    if dii1 in ['*', '×', '•']:
                        d=a*b*c
                    if dii1 in ["**", "^"]:
                        d=a*b**c
                elif dii in ["^", "**"]:
                    if dii1=='+':
                        d=a**b+c
                    if dii1=='-':
                        d=a**b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a**b/c
                    if dii1 in ['*', '×', '•']:
                        d=a**b*c
                    if dii1 in ["**", "^"]:
                        d=a**b**c
#- на обох рівнях
                if dii=='+':
                    if dii1=='+':
                        d=a+b+c
                    if dii1=='-':
                        d=a+b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a+b/c
                    if dii1 in ['*', '×', '•']:
                        d=a+b*c
                    if dii1 in ["^", "**"]:
                        d=a+b**c
                elif dii=='-':
                    if dii1=='+':
                        d=a-b+c
                    if dii1=='-':
                        d=a-b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a-b/c
                    if dii1 in ['*', '×', '•']:
                        d=a-b*c
                    if dii1 in ['^', "**"]:
                        d=a-b**c
                elif dii in ['/', ':', '÷']:
                    if dii1=='+':
                        d=a/b+c
                    if dii1=='-':
                        d=a/b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a/b/c
                    if dii1 in ['*', '×', '•']:
                        d=a/b*c
                    if dii1 in ['^', "**"]:
                        d=a/b**c
                elif dii in ['*', '×', '•']:
                    if dii1=='+':
                        d=a*b+c
                    if dii1=='-':
                        d=a*b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a*b/c
                    if dii1 in ['*', '×', '•']:
                        d=a*b*c
                    if dii1 in ["**", "^"]:
                        d=a*b**c
                elif dii in ["^", "**"]:
                    if dii1=='+':
                        d=a**b+c
                    if dii1=='-':
                        d=a**b-c
                    if dii1 in ['/', ':', '÷']:
                        d=a**b/c
                    if dii1 in ['*', '×', '•']:
                        d=a**b*c
                    if dii1 in ["**", "^"]:
                        d=a**b**c
"""
                        
                else:
                    print('такої дії не існує.')
                print (text, '=', d)
