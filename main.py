# Print on the same line in Python

my_list = ['bobby', 'hadz', 'com']

# ✅ print list items horizontally in for loop
for item in my_list:
    print(item, end=' ')  # 👉️ bobby hadz com

# -------------------------------------------

# ✅ print horizontally using iterable unpacking
print(*my_list)  # 👉️ bobby hadz com

# -------------------------------------------

# ✅ print horizontally using str.join()

result = ' '.join(my_list)
print(result)  # 👉️ bobby hadz com