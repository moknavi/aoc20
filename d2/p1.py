file = open("input.txt", "r")

valid_passwords = 0

for line in file:
    chars = 0
    line = line.strip()
    line = line.split(":")
    print(line)
    password = line[1]
    line = line[0].split()
    print(line)
    char = line[1]
    policy = line[0].split("-")
    print(policy)
    policy = [int(i) for i in policy]
    for i in password:
        if i == char:
            chars += 1
    if chars >= policy[0] and chars <= policy[1]:
        valid_passwords += 1
    
print(valid_passwords)
file.close()