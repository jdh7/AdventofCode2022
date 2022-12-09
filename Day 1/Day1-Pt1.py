def get_input(input_file, day=0):
    db = []
    entry = []
    with open(r"D:\Coding\AdventofCode2022\Day 1\11.in", "r") as f:
        for line in f.readlines():
            line = line.strip()  # .split()
            if line:
                entry.append(line)
            else:
                db.append(entry)
                entry = []
    return db


db = get_input("11.in", day=0)


# part one JEEZ and crackers how to code. oh god this worked lol.
# big_honcho = 0
# for i in db:
#     x = 0
#     for c in i:
#         x += int(c)
#     if x > big_honcho:
#         big_honcho = x
#     x = 0
# print(big_honcho)


total_cals = list()
for elf in db:
    x = 0
    for food in elf:
        x += int(food)
    total_cals.append(x)
    x = 0
print(sum(sorted(total_cals, reverse=True)[:3]))
