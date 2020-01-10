# Verändere den String: "heLLo World!" in:

s = "heLLo World!"

# 1) Hello world! (Stringmethode)
s1 = s.capitalize()
print(s1)

# 2) HeLLo World! (Konkatination + Slicing)
s2 = s[0].upper() + s[1:]
print(s2)

# 3) Hello World! (split() + Stringmethode)
s3_list = s.split()
s3 = s3_list[0].capitalize() + " " + s3_list[1]
s32= s[:6].capitalize() + s[6:]
print(s3)
print(s32)


# string in liste
s4 = list(s)
print(s4)
# liste in string
s4 = ''.join(s4)
print(s4)
