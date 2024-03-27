# # for the given names generate a dictionary
# import random
# names = ["alex", "dave","caroline", "Dave","freddie","eleanor"]
#
# dict_new = {name:random.randint(0,100) for name in names}
# print(dict_new)
#
# # from the dictionary above create a new dictionary of names with value greater than 40
#
# passed_dict = {key:value for (key, value) in dict_new.items() if value > 39}
# print(passed_dict)

# ----------------------------------------------------------------------------------------------------------------------

# sen = "What is the airspeed velo of an unladen swallow?"
#
# l = sen.split()
# dict = {word:len(word) for word in l}
# print(dict)

# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd

student_dict = {
    "student" : ["sha","tri", "shiv"],
    "score":[56,67,78]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

for (index, row) in student_df.iterrows():
    print(row.student)
