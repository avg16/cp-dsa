
# def can_craft_artifact(n, current, target):
#     if all(current[i] >= target[i] for i in range(n)):
#         return True
#     total_current = sum(current)
#     total_needed = sum(target)
#     if total_current < total_needed:
#         return False

#     for i in range(n):
#         if current[i] >= target[i]:
#             continue
#         can_transform = True
#         for j in range(n):
#             if j != i and current[j] < 1:
#                 can_transform = False
#                 break
                
#         if can_transform:
#             new_state = current.copy()
#             new_state[i] += 1
#             for j in range(n):
#                 if j != i:
#                     new_state[j] -= 1
#             if can_craft_artifact(n, new_state, target):
#                 return True
    
#     return False

# def process_test_cases():
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         current = list(map(int, input().split()))
#         target = list(map(int, input().split()))
#         result = can_craft_artifact(n, current, target)
#         print("YES" if result else "NO")
# if __name__ == "__main__":
#     process_test_cases()
# def can_craft_artifact(n, current, target):
#     # Check if current resources satisfy target directly
#     if all(current[i] >= target[i] for i in range(n)):
#         return True

#     total_deficit = 0
#     for i in range(n):
#         if current[i] < target[i]:
#             total_deficit += target[i] - current[i]

#     total_surplus = sum(current) - sum(target)
#     if total_surplus < total_deficit or total_surplus == 0:
#         return False

#     for i in range(n):
#         if current[i] < target[i]:
#             needed = target[i] - current[i]
#             can_transfer = sum(max(0, current[j] - target[j]) for j in range(n) if j != i)
#             if needed > can_transfer:
#                 return False

#     return True


# def process_test_cases():
#     t = int(input())
#     results = []
#     for _ in range(t):
#         n = int(input())
#         current = list(map(int, input().split()))
#         target = list(map(int, input().split()))
#         if can_craft_artifact(n, current, target):
#             results.append("YES")
#         else:
#             results.append("NO")
#     print("\n".join(results))

# if __name__ == "__main__":
#     process_test_cases()


def solve():
    n = int(input())
    current = list(map(int, input().split()))
    target = list(map(int, input().split()))
    neg_val_count = 0
    diff_arr = []
    for i in range(n):
        diff = current[i] - target[i]
        diff_arr.append(diff)
        if diff < 0:
            neg_val_count += 1
    if neg_val_count >= 2:
        return print("NO")
    elif neg_val_count == 0:
        return print("YES")
    else:
        for i in range(n):
            if diff_arr[i] < 0:
                for j in range(n):
                    if diff_arr[j]>= diff_arr[i]:
                        return print("YES")
                return print("NO")

res = []
for i in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)