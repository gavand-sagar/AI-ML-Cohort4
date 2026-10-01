# # ============================================
# # Lab 3: Numbers, Built-in Types & Conversion   (NEW)
# # ============================================
# # Goal: the core scalar types and how to convert between them.

# # ---- The main built-in types ----
# an_int = 10            # int   -> whole numbers (unlimited size in Python!)
# a_float = 3.14         # float -> decimal numbers
# a_bool = True          # bool  -> True / False (a subclass of int)
# a_str = "hello"       # str   -> text
# nothing = None # null         # NoneType -> "no value"

# # for value in (an_int, a_float, a_bool, a_str, nothing):
# #     print(f"{str(value):>6}  ->  {type(value).__name__}")


# # ---- Arithmetic operators ----
# print("add      :", 7 + 2)     # 9
# print("subtract :", 7 - 2)     # 5
# print("multiply :", 7 * 2)     # 14
# print("divide   :", 7 / 2)     # 3.5   (always returns float)
# print("floor div:", 7 // 2)    # 3     (drops the remainder)
# print("modulo   :", 7 % 2)     # 1     (the remainder)
# print("power    :", 7 ** 2)    # 49    (7 squared)


# # ---- Type conversion (casting) ----
# print(int("42") + 1)       # str -> int  => 43
# print(float("3.5") * 2)    # str -> float => 7.0
# print(str(100) + " apples")# int -> str  => "100 apples"
# print(int(3.99))           # float -> int => 3 (truncates, not rounds)
# print(round(3.99))         # round properly => 4
# print(bool(0), bool(""), bool(-5))   # False False True


# # ---- Booleans are integers under the hood ----
# print(True + True)        
# print(True + True + True)
# print(True - True)
# print(True - False)
# print(False + False)


# print(bool(1))
# print(bool(-1))
# print(bool(1.5))
# print(bool(0.5))
# print(bool(0))

# # ---- Useful number helpers ----
# print(abs(-9))             # 9
# print(max(3, 7, 1))        # 7
# print(min(3, 7, 1))        # 1
# print(round(3.14159, 2))   # 3.14
# print(divmod(17, 5))       # (3, 2) -> (quotient, remainder)


# # ---- TRY THIS (uncomment to explore) ----
# # Big integers just work, no overflow:
# print(2 ** 200)

# # Floats are not always exact (binary representation):
# print(0.1 + 0.2)          # 0.30000000000000004

# using System

# import math
# print(math.sqrt(16), math.pi, math.floor(3.7), math.ceil(3.2))