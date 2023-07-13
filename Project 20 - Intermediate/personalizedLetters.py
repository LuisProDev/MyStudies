#TODO: Create a letter using starting_letter.txt

invited_names = open("Input/Names/invited_names.txt")
names = invited_names.readlines()
invited_names.close()

for name in names:
    with open("Input/Letters/starting_letter.txt", "r") as template:
        content = template.read().replace("[name]", name.strip())
        out_file_name = f"Output/ReadyToSend/letter_to_{name.strip()}.txt"
        with open(out_file_name, "w+") as out_file:
            out_file.write(content)

