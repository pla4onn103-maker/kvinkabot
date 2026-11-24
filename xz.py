import os


def create_file(path, content=""):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return f"file {path} created!"


def getfile(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def delete_file(path):
    os.remove(path)
    return f"file {path} deleted!"


def getfile_aslist(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def open_fileeditor(path):
    if not os.path.exists(path):
        create_file(path, "")

    fileaslist = getfile_aslist(path)
    input_filed = ""

    while input_filed != "/save":
        os.system("cls" if os.name == "nt" else "clear")
        print("█" * 40 + " FILE EDITOR " + "█" * 40)
        print("/save - сохранить и выйти")
        print("-" * 93)

        for idx, line in enumerate(fileaslist, start=1):
            print(f"{idx}: {line.rstrip(chr(10) + chr(13))}")

        print("-" * 93)
        input_filed = input("> ")

        if input_filed != "/save":
            fileaslist.append(input_filed + "\n")

    with open(path, "w", encoding="utf-8") as file:
        file.writelines(fileaslist)

    print(f"file {path} saved!")
    return "file saved!"
