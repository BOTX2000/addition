def codec(s):
    if s==1:
        print('шифратор')
    while True:
        go=0
        texta=[" ", "#", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Ґ", "ґ", "Е", "е", "Є", "є", "Ж", "ж", "З", "з", "И", "и", "І", "і", "Ї", "ї", "Й", "й", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р", "С", "с", "Т", "т", "У", "у", "Ф", "ф", "Х", "х", "Ц", "ц", "Ч", "ч", "Ш", "ш", "Щ", "щ", "ь", "Ю", "ю", "Я", "я", ".", ",", "(", ")", "!"]
        textb=["✓ ", "✓# ", "✓## ", "✓### ", "✓#### ", "✓##### ", "✓###### ", "✓####### ", "######## ", "✓######### ", "✓########## ", "✓########### ", "j687 ", "q250 ", "a085 ", "d603 ", "k972 ", "g635 ", "b204 ", "v651 ", "o509 ", "w446 ", "h989 ", "l500 ", "z487 ", "x943 ", "p442 ", "c122 ", "i095 ", "d169 ", "f658 ", "r082 ", "s368 ", "m124 ", "a230 ", "w559 ", "t367 ", "d069 ", "h865 ", "n772 ", "z839 ", "d392 ", "g702 ", "w432 ", "h347 ", "k953 ", "x267 ", "o846 ", "q792 ", "c923 ", "i339 ", "r492 ", "z877 ", "q023 ", "f657 ", "b353 ", "y812 ", "m209 ", "t738 ", "n549 ", "h868 ", "p954 ", "g244 ", "o461 ", "a009 ", "w450 ", "k090 ", "c765 ", "d891 ", "s426 ", "x395 ", "u688 ", "o362 ", "b679 ", "k825 ", "h901 ", "d003 ", "f437 ", "y662 ", "r879 ", "u991 ", "x006 "]
        textc=["✓ ", "✓# ", "✓## ", "✓### ", "✓#### ", "✓##### ", "✓###### ", "✓####### ", "✓######## ", "✓######### ", "✓########## ", "✓########### "]
        textd=["a032 ", "u072 ", "p068 ", "a237 ", "v759 ", "m392 ", "c451 ", "w803 ", "s132 ", "q268 ", "n739 ", "z359 "]
        a=0
        text=input()
        if text in ["hom", "/hom"]:
            break
        elif text in ["decodec", "/decodec"]:
            decodec(s)
            go=1
        for i in texta :
            text=text.replace(texta[a], textb[a])
            a=a+1
        a=0
        for i in textc :
            text=text.replace(textc[a], textd[a])
            a=a+1
        if go==1:
            print("шифратор")
        else:
            print(text)

def decodec(s):
    if s==1:
        print('дешифратор')
    while True:
        go=0
        texta=[" ", "#", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Ґ", "ґ", "Е", "е", "Є", "є", "Ж", "ж", "З", "з", "И", "и", "І", "і", "Ї", "ї", "Й", "й", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р", "С", "с", "Т", "т", "У", "у", "Ф", "ф", "Х", "х", "Ц", "ц", "Ч", "ч", "Ш", "ш", "Щ", "щ", "ь", "Ю", "ю", "Я", "я", ".", ",", "(", ")", "!"]
        textb=["✓ ", "✓# ", "✓## ", "✓### ", "✓#### ", "✓##### ", "✓###### ", "✓####### ", "######## ", "✓######### ", "✓########## ", "✓########### ", "j687 ", "q250 ", "a085 ", "d603 ", "k972 ", "g635 ", "b204 ", "v651 ", "o509 ", "w446 ", "h989 ", "l500 ", "z487 ", "x943 ", "p442 ", "c122 ", "i095 ", "d169 ", "f658 ", "r082 ", "s368 ", "m124 ", "a230 ", "w559 ", "t367 ", "d069 ", "h865 ", "n772 ", "z839 ", "d392 ", "g702 ", "w432 ", "h347 ", "k953 ", "x267 ", "o846 ", "q792 ", "c923 ", "i339 ", "r492 ", "z877 ", "q023 ", "f657 ", "b353 ", "y812 ", "m209 ", "t738 ", "n549 ", "h868 ", "p954 ", "g244 ", "o461 ", "a009 ", "w450 ", "k090 ", "c765 ", "d891 ", "s426 ", "x395 ", "u688 ", "o362 ", "b679 ", "k825 ", "h901 ", "d003 ", "f437 ", "y662 ", "r879 ", "u991 ", "x006 "]
        textc=["✓ ", "✓# ", "✓## ", "✓### ", "✓#### ", "✓##### ", "✓###### ", "✓####### ", "✓######## ", "✓######### ", "✓########## ", "✓########### "]
        textd=["a032 ", "u072 ", "p068 ", "a237 ", "v759 ", "m392 ", "c451 ", "w803 ", "s132 ", "q268 ", "n739 ", "z359 "]
        a=0
        text=input()
        if text in ["hom", "/hom"]:
            break
        elif text in ["codec", "/codec"]:
            codec(s)
            go=1
        for i in textc :
            text=text.replace(textd[a], textc[a])
            a=a+1
        a=0
        for i in texta :
            text=text.replace(textb[a], texta[a])
            a=a+1
        if go==1:
            print("дешифратор")
        else:
            print(text)