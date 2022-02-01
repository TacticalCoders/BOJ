data = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}
s = list(input())
result = []
while len(s) != 0:
    if len(s) == 1:
        result.append(s[1])
        break
    word = s[0] + s[1]
    if word in data:
        result.append(word)
        del s[0:2]
    else:
        if len(s) < 3:
            result.append(s[0])
            result.append(s[1])
            del s[0:2]
        else:
            word = word + s[2]
            if word in data:
                result.append(word)
                del s[0:3]
            else:
                result.append(s[0])
                del s[0]

print(len(result))