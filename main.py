#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PATH_NAMES_FILE = "./Input/Names/invited_names.txt"
PATH_LETTER_FILE = "./Input/Letters/starting_letter.txt"

with open(PATH_NAMES_FILE, "r") as invited_names_file:
    raw_names = invited_names_file.readlines()

    # - - - Cleaning names - - -
    clean_names = []
    for line in raw_names:
        invited_name = line.strip()
        clean_names.append(invited_name)
    print(clean_names)

with open(PATH_LETTER_FILE, "r") as letter_file:
    letter_content = letter_file.read()
    print(letter_content)

    # - - - Replacing name in letter - - -
    personalized_letters = []
    for clean_name in clean_names:
        new_letter = letter_content.replace("[name]", f"{clean_name}")
        personalized_letters.append(new_letter)
    print(personalized_letters)

# - - - Creating new letters files - - -
all_new_letters = []
for index_letter, letter in enumerate(personalized_letters):
    name_in_letter = clean_names[index_letter]
    file_name = f"./Output/ReadyToSend/letter_for_{name_in_letter}.txt"
    with open(file_name, "w") as new_file:
        new_file.write(letter)




