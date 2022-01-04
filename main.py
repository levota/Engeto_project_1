import time
import pandas as pd
import matplotlib.pyplot as plt

from pomocne_funkce import word_list
from pomocne_funkce import words_lenghts
from Users import users
from task_template import TEXTS

def main():

    ODDELOVAC = "-"
    uzivatel = str(input("Plese enter your user name: ")).lower()
    heslo = str(input("Please insert your password: "))


    if users.get(uzivatel) == heslo:
        print(f"""Welcome to the app, {uzivatel}
    We have 3 texts to be analyzed""")
        print(ODDELOVAC * 40)
    else:
        print("User name or password is incorrect")
        time.sleep(3)
        quit()

    text_choice = int(input("Enter a number btw. 1 and 3 to select: "))

    if text_choice in range(1, 4):
        print(ODDELOVAC * 40)
    else:
        print("Use only numbers from 1 to 3 thx")
        time.sleep(3)
        quit()

    striped_word_list = word_list(TEXTS[text_choice - 1])
    words_lenghts(striped_word_list)

    print(ODDELOVAC*40)


    slovnik_delek_slov = {}
    for slovo in striped_word_list:
        if len(slovo) not in slovnik_delek_slov:
            slovnik_delek_slov[len(slovo)] = 1
        else:
            slovnik_delek_slov[len(slovo)] +=1

    list_delek_slov = []
    for delka in slovnik_delek_slov.keys():
        list_delek_slov.append(delka)

    list_vyskytu_slov = []
    for vyskyt in slovnik_delek_slov.values():
        list_vyskytu_slov.append(vyskyt)

    d = {"Lenght" :list_delek_slov, "Occurrence": list_vyskytu_slov}

    df = pd.DataFrame(d)
    print(df)
    df.plot(x ="Lenght", y = "Occurrence", kind = "bar" )
    plt.show()

if __name__ == "__main__":
    main()