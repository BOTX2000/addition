def perevod (text):
    thn=["+", "-", "/", ":", "÷", "*", "×", "•", "^", "**"]
    a=0
    for i in thn:
        text=text.replace(thn[a], "#")
        a=a+1
    text=text.split('#')
    chi=[x for x in text if x !='']
    return chi

def perevod1 (text):
    chi=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    a=0
    for i in chi:
        text=text.replace(chi[a], "#")
        a=a+1
    text=text.split("#")
    dii= [x for x in text if x !='']
    return dii

def perevodk (text):
    thr=["a=", " b=", " c=", " R=", " r="]
    a=0
    for i in thr:
        text=text.replace(thr[a], "#")
        a=a+1
    text=text.split('#')
    chi=[x for x in text if x !='']
    return chi
