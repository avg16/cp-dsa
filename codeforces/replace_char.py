def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def calculate_permutations(string):
    n = len(string)
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    permutations = factorial(n)
    for freq in char_freq.values():
        permutations //= factorial(freq)

    return permutations

def solve(str):
    # dictionary to store strings and their permutations
    permutations_dict = {}
    for i in range(len(str)):
        for j in range(len(str)):  
            new_str = list(str)
            new_str[i] = str[j]  
            permutations = calculate_permutations(''.join(new_str))
            permutations_dict[''.join(new_str)] = permutations
    min_permutations = min(permutations_dict.values())
    result_strs = [s for s, p in permutations_dict.items() if p == min_permutations]
    return result_strs[0]

results= []
for i in range(int(input())):
    n= int(input())
    str = input()
    results.append(solve(str))
for i in results:
    print(i)