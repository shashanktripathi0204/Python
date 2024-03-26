#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



# List of names
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)

# Read the contents of the file
with open('./Input/Letters/starting_letter.txt', 'r') as file:
    content = file.read()

# Replace the placeholder with each name and write to the file

for name in names:
    name = name.strip() # strping the \n from names
    with open(f'./Output/ReadyToSend/Letter_for_{name}.txt', 'w') as file:
        modified_content = content.replace('[name]', name)
        file.write(modified_content + '\n')