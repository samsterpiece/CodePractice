acronyms = {"LOL" : "laugh out loud", 
"IDK": "I don't know", 
"TBH": "to be honest"} #key-value pair
del acronyms["LOL"]

# #Get a word in the dictionary, use get()
# definition = acronyms.get("BTW")
# print(definition)

# if definition: 
#     print(definition)
# else:
#         print("Key doesn't exist")

sentence = "IDK" + " what happened " + "TBH"
translation = acronyms.get("IDK") + " what happened " +  acronyms.get("TBH") #prints out acronyms of words

print("sentence: ", sentence)
print("translation: ", translation)