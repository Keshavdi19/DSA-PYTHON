S = "azyuyyzaaaa"
q = ["d", "a", "y", "u"]
hash_dict = {}
for ch in S:
    hash_dict[ch] = hash_dict.get(ch, 0) + 1
for ch in q:
    print(hash_dict.get(ch, 0))
# for capital letters
S = "AHSHSSGGDG"
q = ["A", "H", "S", "G"]
hash_dict = {}
for ch in S:
    hash_dict[ch] = hash_dict.get(ch, 0) + 1
for ch in q:
    print(hash_dict.get(ch, 0))

