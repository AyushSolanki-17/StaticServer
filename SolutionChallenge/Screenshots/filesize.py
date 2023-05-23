import os
size = os.path.getsize("D:\StaticServer\SolutionChallenge\Screenshots\demofile.txt")
print("Size before Alteration: ",size)
with open('demofile.txt', 'ab') as f:
    f.write(b'\0' * 1000)

size = os.path.getsize("D:\StaticServer\SolutionChallenge\Screenshots\demofile.txt")
print("Size after Alteration (1000 Bytes): ",size)