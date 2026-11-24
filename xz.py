import os


def create_file(path, content=""):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return f"file {path} created!"


def getfile(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def playfile(path):
    with open(path, "r", encoding="utf-8") as file:
        exec(file.read())


def delete_file(path):
    os.remove(path)
    return f"file {path} deleted!"


def getfile_aslist(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()

def moverename_file(path, new_path):
      os.rename(path, new_path)
      print("file renamed!")
      return "file moved!"


def open_fileeditor(path):
    if not os.path.exists(path):
        create_file(path, "")

    fileaslist = getfile_aslist(path)
    input_filed = ""

    while input_filed != "/save":
        os.system("cls" if os.name == "nt" else "clear")
        print("███████████████████████████████████████████████████████FILE EDITOR█████████████████████████████████████████████████████")
        print("/save - save")
        print("/remove - delete last string")
        for loadvisual in fileaslist:
            print(loadvisual.rstrip("\r\n"))
        input_filed = input("")
        if input_filed == "/remove":
            if fileaslist:
                fileaslist.pop()
        elif input_filed != "/save":
            fileaslist.append(input_filed + "\n")

    with open(path, "w", encoding="utf-8") as file:
        file.writelines(fileaslist)

    print(f"file {path} saved!")
    return "file saved!"
