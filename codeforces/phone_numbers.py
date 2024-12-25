def divide_phone_number(n, phone_number):
    groups = []
    i = 0
    
    while i < n:
        remaining = n - i
        if remaining == 4:
            groups.append(phone_number[i:i + 2])
            groups.append(phone_number[i + 2:i + 4])
            break
        elif remaining >= 3:
            groups.append(phone_number[i:i + 3])
            i += 3
        else:
            groups.append(phone_number[i:i + 2])
            i += 2
    
    return "-".join(groups)

n = int(input())
phone_number = input()
print(divide_phone_number(n, phone_number))