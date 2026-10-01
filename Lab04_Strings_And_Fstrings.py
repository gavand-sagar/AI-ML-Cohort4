# ============================================
# Lab 4: Strings & f-strings   (NEW)
# ============================================
# Goal: create, format, slice and transform text.

name = "Sagar"
language = "Python"

# ---- f-strings: the modern way to build text (Python 3.6+) ----
# Put an 'f' before the quote, then drop variables inside { }.
print(f"Hi {name}, welcome to {language}!")

# # # You can run expressions inside the braces:
# print(f"2 + 3 = {2 + 3}")
# print(f"Upper: {name.upper()}")

# # # Number formatting inside f-strings:
# price = 1234.5678
# print(f"Price: {price:.2f}")     # 2 decimal places -> 1234.57
# print(f"Padded: {42:05d}")       # pad with zeros    -> 00042
# print(f"Percent: {0.873:.1%}")   # as a percentage   -> 87.3%


# # ---- Common string methods ----
# text = "  Hello, World  "
# print(text.strip())              # remove surrounding spaces
# print(text.strip().lower())      # "hello, world"
# print("hello".upper())           # "HELLO"
# print("Hello".replace("l", "L")) # "HeLLo"
# print("a,b,c".split(","))        # ['a', 'b', 'c']
# print("-".join(["2026", "06", "20"]))  # "2026-06-20"
# print("python".startswith("py")) # True
# print("python".find("th"))       # index 2 (-1 if not found)
# print(len("python"))             # 6


# # ---- Indexing & slicing (strings are sequences of characters) ----
s = "hello"
# print(s[0])        # 'h'   first char
# print(s[-3])       # 'o'   last char
# print(s[1:4])      # 'ell' chars 1,2,3
# print(s[-2])   
print(s[::-1])       # 'he'  start to index 2
# print(s[::-1])     # 'olleh' reversed


# # ---- Strings are IMMUTABLE ----
# You cannot do s[0] = "H". Instead, build a new string.
# fixed = "H" + s[1:]  # "ello"
# print(fixed)       # "Hello"


# # ---- Multi-line strings & escape characters ----
# poem = """Roses are red,
# Violets are blue."""
# print(poem)
# print("Tab\tseparated\nNew line")   # \t = tab, \n = newline
# print(r"C:\new\folder")             # r"..." = raw string, ignores escapes


# ---- TRY THIS (uncomment to explore) ----
# print("Python is fun".title())          # "Python Is Fun"
# print("123".isdigit(), "abc".isalpha()) # True True
# print("a".center(5, "*"))               # "**a**"
