# # ============================================
# # Lab 2: Variables & Dynamic Typing
# # ============================================
# # Goal: how Python variables work, and how they differ from C#/Java.

# # ---- No type declaration needed ----
# # You don't write 'int x = 10'. Python infers the type at runtime.
# x = 56
# print(type(x).__name__)   # int
# x = "Sagar"
# print(type(x).__name__)   # str

# # ---- Dynamic typing: same name can later hold a different type ----
# x = "now I am a string"
# print("x =", x, "| type:", type(x).__name__)   # str


# # ---- PEP 8 naming convention: snake_case for variables ----
# user_name = "Alice"
# item_count = 42
# is_active = True
# print(user_name, item_count, is_active)


# # ---- Multiple assignment ----
# a, b, c = 1, 2, 3            # unpack in one line
# print(a, b, c)

# p = q = r = 0               # chain assignment: all point to the same 0
# print(p, q, r)


# # ---- Variables are REFERENCES to objects (important!) ----
# # Immutable types (int, str, tuple) behave like copies because they can't change.
# n1 = 5
# n2 = n1
# n1 = 99
# print("n1:", n1, "n2:", n2)        # n2 stays 5

# # Mutable types (list, dict, set) are SHARED when assigned.
# list_a = [1, 2]
# list_b = list_a                    # both names point to the SAME list
# list_a.append(3)
# print("list_a:", list_a, "list_b:", list_b)   # both show [1, 2, 3]!

# # # To get an independent copy, copy explicitly:
# list_c = list_a.copy() # diff reference
# list_a.append(4)
# print("list_a:", list_a, "list_c:", list_c)   # list_c is unaffected


# # ---- 'is' vs '==' ----
# # '=='  compares VALUES.   'is' compares IDENTITY (same object in memory).

list_a = [1,2,3] # memory location a
list_b = [1,2,3] # memory location b



print(list_a == list_b)   # True  -> equal values

print(list_a is list_b)   # False -> two different objects


# # ---- Constants: Python has no real 'const'; convention is UPPER_CASE ----
# PI = 3.14159
# MAX_USERS = 100

# print(PI)


# # ---- TRY THIS (uncomment to explore) ----
# print(type(3.0))          # <class 'float'>
# # print(type(True))         # <class 'bool'>
# # del x                     # delete a variable; using x after this raises NameError
# # print(x)
