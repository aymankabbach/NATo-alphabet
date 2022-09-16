import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
##{"A": "Alfa", "B": "Bravo"}
new_dict={
    row.letter:row.code for (index,row) in data.iterrows()
}
def read_input():
    user_name=input("what is your name?\n")
    return user_name
def is_input_valid():
    user_input=read_input()
    try:
        user_input=int(user_input)
    except ValueError:
        return user_input
    else:
        return False
def get_user_input():
    wrong_input=True
    while wrong_input:
        user_name=is_input_valid()
        if user_name!=False:
            wrong_input=False
            return user_name
def start():
    user_name=get_user_input().upper()
    try:
        phonetic_list=[new_dict[letter] for letter in user_name]
    except:
        print("Invalid input, please enter only Latin alphabet")
        start()
    else:
        print(phonetic_list)
start()