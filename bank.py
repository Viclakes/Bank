BANK_NAME = "[Bank]"

with open("bank.txt") as banks:
    bank = banks.readlines()

with open("/Users/User/Documents/Signatories 1.docx") as letters:
    letter = letters.read()
    for b in bank:
        stripped_letter = b.strip()
        new_letter = letter.replace(BANK_NAME, stripped_letter)
        with open(f"/Users/User/Documents/letter_to_{bank}.docx", 'w') as completed_letter:
            completed_letter.write(new_letter)
