import pandas

p_reader = pandas.read_csv("Phonetics.csv")
DF = pandas.DataFrame(p_reader)
Dict = DF.to_dict()

Check = input("Please enter your name: ")
Check1 = Check.upper()


new_format = {values.letter:values.code for x, values in DF.iterrows()}

answer_list = [new_format[letter] for letter in Check1]
print(answer_list)