# n = input().split()
# m = int(input())

# def minimum_possible_by_shuffling_n(n):
#     n.sort(key=int)
#     zero_count = 0
#     for i in range(len(n)):
#         if int(n[i]) == 0:
#             zero_count += 1
#     new_num = min(n[zero_count:], key=int) + '0' * zero_count + ''.join(n[zero_count:]) - min(n[zero_count:], key=int)
#     print(new_num)
#     return new_num

# new_num = minimum_possible_by_shuffling_n(n)
# if new_num == m:
#     print("OK")
# else:
#     print("WRONG_ANSWER")
n = int(input())
def minimum_possible_by_shuffling_n(n):
    n = str(n)
    n = list(n)
    n.sort()
    # now first digit should not be zero
    zero_count = 0
    for i in range(len(n)):
        if n[i] == '0':
            zero_count += 1
    non_zero = [x for x in n if x != '0']
    new_num = min(non_zero) + '0' * zero_count + ''.join([x for x in non_zero if x != min(non_zero)])

    return new_num

m = int(input())
new_num = minimum_possible_by_shuffling_n(n)
if n == m:
    print("OK")
elif int(new_num) == m:
    print("OK")
else:
    print("WRONG_ANSWER")