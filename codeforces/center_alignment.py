lines = [input() for _ in iter(lambda: input(), '')]

max_len = max(len(line) for line in lines)

print("*"*(max_len+2))

for line in lines:
    print("* " + line.ljust(max_len) + " *")

print("*"*(max_len+2))