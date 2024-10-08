# Split and join in the strings
# Split = Split a string and join une 

phrase = "i' m going to get the lob"
phrase_splited = phrase.split("'")

for i, phrase in enumerate(phrase_splited):
    print(phrase_splited[i].strip())
print(phrase_splited)


phrasestogether = "".join("abc")
print(phrasestogether)