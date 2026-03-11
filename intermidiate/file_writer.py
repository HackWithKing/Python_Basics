text = input("Enter text to save: ")

file = open("output.txt", "w")

file.write(text)

file.close()

print("Text saved to file.")
