#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


invited_names = open("Input/Names/invited_names.txt")
names = invited_names.readlines()
invited_names.close()

for name in names:
    with open("Input/Letters/starting_letter.txt", "r") as template:
        content = template.read().replace("[name]", name.strip())
        out_file_name = f"Output/ReadyToSend/letter_to_{name.strip()}.txt"
        with open(out_file_name, "w+") as out_file:
            out_file.write(content)

