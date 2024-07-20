import difflib

# Dua urutan yang akan dibandingkan
a = "qabxcd"
b = "abycdf"

# Membuat objek SequenceMatcher
s = difflib.SequenceMatcher(None, a, b)

# Mendapatkan opcode
opcodes = s.get_opcodes()

# Menampilkan dan membenarkan hasil opcode
c = []
for tag, i1, i2, j1, j2 in opcodes:
    print(f"{tag:7} a[{i1}:{i2}] --> b[{j1}:{j2}] {a[i1:i2]!r:>8} --> {b[j1:j2]!r}")
    if tag == 'equal':
        c.extend(a[i1:i2])
    elif tag == 'replace':
        c.extend(b[j1:j2])
    elif tag == 'insert':
        c.extend(b[j1:j2])
    elif tag == 'delete':
        continue

print(a, '<->', b, '==', ''.join(c))