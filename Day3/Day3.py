def get_input():
    db = []
    with open(r"D:\Coding\AdventofCode2022\Day3\31.in", "r") as f:
        for line in f.readlines():
            db.append([c for c in line.strip().split()])
    return db


x = get_input()
print(x)
