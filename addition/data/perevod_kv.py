def ybrat_x_1 (t):
    t1=t.replace("x^", "#")
    
    t2=t1.replace("x", "#")
    t3=t2.split("#")
    dii= [x for x in t3 if x !='']
    return dii

def ybrat_x (text):
    chi=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    a=0
    for i in chi:
        text=text.replace(chi[a], "#")
    return text

def perevod_par(text):
    text1=text.replace("x^2", "*")
    text3=text1.replace("x", "*")
    text4=text3.split('*')
    chi=[x for x in text4 if x !='']
    return chi
