import os

path = "D:\StaticServer\SolutionChallenge\Screenshots" # replace with the path to your folder

files = os.listdir(path)
files.sort() # sort the files alphabetically

i = 1
for file in files:
    if file.endswith(".jpeg") or file.endswith(".jpg"): # only rename image files
        os.rename(os.path.join(path, file), os.path.join(path, str(i) + ".jpeg"))
        i += 1
