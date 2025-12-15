import os
os.chdir(r"C:\Users\johnd\Documents\VIDEOGAMES\AULAS\FP1\Python_lab2025\AULA_07T")

file = open("dialogos.txt", "a+t")

line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)

file.write("blabla\n")

file.seek(0)  # move cursor to start

pagina = file.readlines()

for line in pagina:
    if line and ":" in line: 
        print(line.strip())

file.close()
