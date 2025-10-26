S = "AHSHSHHSJDJD"
q = ["D", "A", "S", "H"]
hash_list = [0] * 123
for ch in S:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])
    

