S = "azyuyyzaaaa"
q = ["d", "a", "y", "u"]
hash_list = [0] * 26
for ch in S:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])

