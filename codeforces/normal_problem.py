t= int(input())
test_cases = []
for _ in range(t):
    str_input = input()
    test_cases.append(str_input)

def solve(str_input):
    str_list = list(str_input)
    for i in range(len(str_list)):
        if str_list[i] == 'p':
            str_list[i] = 'q'
        elif str_list[i] == 'q':
            str_list[i] = 'p'
        str_list = list(reversed(str_list))
    return "".join(str_list)

results = []
for str_input in test_cases:
    results.append(solve(str_input))

for res in results:
    print(res)