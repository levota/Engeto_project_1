TEXT = """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.
"""

def word_list(str) -> list:
    jednotliva_slova = str.split()
    list = [slovo.strip(".,!?") for slovo in jednotliva_slova]
    return list


def words_lenghts(list) -> str:
    word_count = len(list)
    print(f"There are {word_count} words in the selected text.")
    titled_words = []
    for slovo in list:
        if slovo.istitle():
            titled_words.append(slovo)
    print(f"There are {len(titled_words)} titlecase words.")
    uppercase_words = []
    for slovo in list:
        if slovo.isupper() and slovo.isalpha():
            uppercase_words.append(slovo)
    print(f"There are {len(uppercase_words)} uppercase words.")
    lowercase_words = []
    for slovo in list:
        if slovo.islower():
            lowercase_words.append(slovo)
    print(f"There are {len(lowercase_words)} lowercase words.")
    numeric_strings = []
    for slovo in list:
        if slovo.isnumeric():
            numeric_strings.append(int(slovo))
    print(f"There are {len(numeric_strings)} numeric strings.")
    print(f"The sum of all numbers {sum(numeric_strings)}")
