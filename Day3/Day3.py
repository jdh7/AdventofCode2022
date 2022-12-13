def get_input():
    db = []
    with open(r"D:\Coding\AdventofCode2022\Day3\31.in", "r") as f:
        for line in f.readlines():
            db.append(line.strip().split())
    return db


x = get_input()


# split contents into first and second compartment

i = x[0][0]
first_half = i[: int(len(i) / 2)]
second_half = i[int(len(i) / 2) :]

# assign priorities
items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in items:
    print(i)
