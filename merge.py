import os

path = 'E:\\md'

md_list = os.listdir(path)

contents = []
for md in md_list:
    md_file = path + '\\' + md
    with open(md_file, 'r', encoding='utf-8') as file:
        contents.append(file.read() + '\n')

with open('merged.md','w', encoding='utf-8') as file:
    file.writelines(contents)