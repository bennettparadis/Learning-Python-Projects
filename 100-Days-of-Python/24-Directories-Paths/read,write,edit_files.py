
# can work with a file in same folder --> must remember to use both open and close methods...otherwise file may
# remain open and take up CPU
# open method --> default mode is read only
file = open("../my_file.txt")
contents = file.read()
print(contents)
file.close()

# alternatively, can use keywords to open/close automatically
with open("../my_file.txt") as file:
    contents = file.read()
    print(contents)

# Can also write to a file
with open("../my_file.txt", mode='w') as file:
    file.write("New text.")
    #this would remove and replace previous text with new text

# Can also edit a file
with open("../my_file.txt", mode='a') as file:
    file.write("\nNew text again.")
    #this would append
# if in write mode and the file does not exist, it will create a new file and add the text


# File paths
# Root drive is the base, everything branches out from here - in mac it's MacIntosh HD; in windows it's C
# Absolute file paths always start off relative to the root (begins with '/') -- begins at origin
# Relative file path -- working directory that is currently being used, can use relative file path (basically abbreviated pathway)
# ex/ starts with a '.' --> ./Project/talk.ppt

# Move between directories
# go to parent folder --> ../report.doc

# Access file in the same folder, can just refer to it by it's name

# Challenge to access a new text file; slashes need to be forward
with open("/Users/bparadis/Documents/Social Media/challenge.txt") as file:
    contents = file.read()
    print(contents)

# each '../' indicates to go back one folder
with open("../../../SR vid/challenge.txt") as file:
    contents = file.read()
    print(contents)
