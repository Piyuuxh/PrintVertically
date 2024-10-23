def printVertically(s): #str
    words = s.split()
    max_len = max(map(len, words))
    result = []
    for i in range(max_len):
        vertical = ''.join([word[i] if i < len(word) else ' ' for word in words]).rstrip()
        result.append(vertical)
    return result

s = "HOW ARE YOU"
print(printVertically(s))
    