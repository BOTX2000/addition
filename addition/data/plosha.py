from perevod import*
def plosha_geron(s):
    if s==1:
        print("периметр трикутника за формолою герона.")
    while True:
        text=input()
        if text in ["hom", "/hom"]:
            break
        chi=perevodk(text)
        a=int(chi[0])
        b=int(chi[1])
        c=int(chi[2])
        p=(a+b+c)/2
        print(sqrt(p*(p-a)*(p-b)*(p-c)))

def plosha_op(s):
    if s==1:
        print("площа описаного навколо трикутника кола.")
    while True:
        text=input()
        if text in ["hom", "/hom"]:
            break
        chi=perevodk(text)
        a=int(chi[0])
        b=int(chi[1])
        c=int(chi[2])
        R=int(chi[3])
        print((a*b*c)/(4*R))

def plosha_vp(s):
    if s==1:
        print("площа вписаного в трикутник кола.")
    while True:
        text=input()
        if text in ["hom", "/hom"]:
            break
        chi=perevodk(text)
        a=int(chi[0])
        b=int(chi[1])
        c=int(chi[2])
        r=int(chi[3])
        print(((a+b+c)/2)*r)

def plosha(s):
    while True:
        if s==1:
            print("формула герона(/ger).")
            print("описане коло(/op).")
            print("вписане коло(/vp).")
        text=input()
        if text in ["ger", "/ger"]:
            plosha_geron(s)
        elif text in ["op", "/op"]:
            plosha_op(s)
        elif text in ["vp", "/vp"]:
            plosha_vp(s)
        elif text in ["hom", "/hom"]:
            break
        else:
            print("команди не існує.")
