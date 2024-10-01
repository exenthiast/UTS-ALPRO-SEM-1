from collections import Counter

X = [13, 19, 12, 13, 190, 12, 13, 120001, 4, 23765876]

frekuensi = Counter(X)

modus = frekuensi.most_common(1)[0]  

print(f"Modusnya adalah {modus[0]} dengan frekuensi {modus[1]}")
