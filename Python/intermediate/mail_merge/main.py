NAME = "[name]"

with open("./names.txt") as name:
    names = name.readlines()

with open("./letter.txt") as letter_template :
    letter = letter_template.read()

for name in names:
    striped_name = name.strip()
    new_letter = letter.replace(NAME, striped_name)
    with open(f"./ready_to_send/letter_for_{striped_name}.txt", mode = "w" ) as completed_letter:
        completed_letter.write(new_letter)
