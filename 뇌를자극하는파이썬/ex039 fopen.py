with open("basic.txt", "w", encoding="utf-8") as file: #utf-8 : unicode
    file.write("Hello python")
    file.write("안녕 파이썬")
    for i in range(0,6):
        file.write(str(i)+"\n")