PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() #이름을 리스트에 넣기

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
