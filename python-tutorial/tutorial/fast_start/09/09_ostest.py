import os
s1 = set()

for path, dirs, files in os.walk("//"): # в метод walk передаем текущую рабочую директорию
    for file in files:
        if (file.__contains__("Battle") or file.__contains__("battle")):
            s1.add(path)
            # print("path", path)
for path_files in s1:
    print(path_files)
