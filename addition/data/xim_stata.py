def xim(s):
    if s==1:
        print("хімічна статистика елемента.")
    while True:
        art=["H", "He", "Li", "Be","B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Ti", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Uut", "Fl", "Uup", "Lv", "Uus", "Uuo"]
        name=["Гідроген", "Гелій", "Літій", "Берилій", "Бор", "Карбон", "Нітроген", "Оксиген", "Флуор", "Неон", "Натрій", "Магній", "Алюміній", "Силіцій", "Фосфор", "Сульфур", "Хлор", "Аргон", "Калій", "Кальцій", "Скандій", "Титан", "Ванадій", "Хром", "Манган", "Ферум", "Кобальт", "Нікол", "Купрум", "Цинк", "Галій", "Германій", "Арсен", "Селен", "Бром", "Криптон", "Рубідій", "Стронцій", "Ітрій", "Цирконій", "Ніобій", "Молібден", "Технецій", "Рутеній", "Родій", "Паладій", "Аргентум", "Кадмій", "Індій", "Станум", "Стибій", "Телур", "Йод", "Ксенон", "Цезій", "Барій", "Лантан", "Церій", "Празеодим", "Неодим", "Прометій", "Самарій", "Європій", "Гадоліній", "Тербій", "Диспрозій", "Гольмій", "Ербій", "Тулій", "Ітербій", "Лютецій", "Гафній", "Тантал", "Вольфрам", "Реній", "Осмій", "Іридій", "Платина", "Аурум", "Меркурій", "Талій", "Плюмбум", "Бісмут", "Полоній", "Астат", "Радон", "Францій", "Радій", "Актиній", "Торій", "Проактиній", "Уран", "Нептуній", "Плутоній", "Америцій", "Кюрій", "Берклій", "Каліфорній", "Ейнштейній", "Фермій", "Менделевій", "Нобелій", "Лоуренсій", "Резерфордій", "Дубній", "Сиборгій", "Борій", "Гасій", "Майтнерій", "Дармштадтій", "Ренгеній", "Коперницій", "Унунтрій", "флеровій", "Унунгентій", "Лівермерій", "Унунсептій", "Унуноктій"]
        mas=["1.0079", "4.0026", "6.941", "9.012", "10.81", "12.011", "14.0067", "15.999", "18.998", "20.180", "22.990", "24.305", "26.982", "28.086", "30.974", "32.06", "35.453", "39.948", "39.098", "40.08", "44.956", "47.87", "50.941", "51.996", "54.938", "55.845", "58.933", "58.69", "63.546", "65.38", "69.72", "72.64", "74.922", "78.96", "79.904", "83.80", "85.468", "87.62", "88.906", "91.22", "92.906", "95.94", "[98]", "101.07", "102.905", "106.4", "107.868", "112.41", "114.82", "118.71", "121.76", "127.60", "126.904", "131.29", "132.91", "137.33", "138.905", "140.12", "140.908", "144.24", "[147]", "150.4", "151.96", "157.25", "158.925", "162.50", "164.93", "167.26", "168.93", "173.04", "174.97", "178.49", "180.948", "193.84", "186.207", "190.2", "192.22", "195.08", "196.967", "200.59", "204.38", "207.2", "208.980", "[209]", "[210]", "[222]", "[223]", "226.03", "[227]", "232.038", "231.036", "238.029", "[237]", "[244]", "[243]", "[247]", "[247]", "[249]", "[252]", "[257]", "[258]", "[259]", "[260]", "[261]", "[262]", "[263]", "[262]", "[265]", "[266]", "[281]", "[280]", "[285]", "[284]", "[289]", "[288]", "[293]", "[294]", "[294]"]


        text=input()
        if text in ["hom", "/hom"]:
            break
        try:
            artn=art.index(text)
            print("порядковий номер елемента: ", artn+1)
            print("назва елемента: ", name[artn])
            print("маса елемента: ", mas[artn])
            print("число протонів у ядрі: ", artn+1)
            print("число електронів у атоні: ", artn+1)
            print("число нейтронів у ядрі визначається за формолою: маса-число протонів. програмою я невзмозі це порахувати.")
        except:
            try:
                artn=name.index(text)
                print("порядковий номер елемента:", artn+1)
                print("позначення елемента:", art[artn])
                print("маса елемента:", mas[artn])
                print("число протонів у ядрі: ", artn+1)
                print("число електронів у атоні: ", artn+1)
                print("число нейтронів у ядрі визначається за формолою: маса-число протонів. програмою я невзмозі це порахувати.")
            except:
                if s==1:
                    print("невиходить(")