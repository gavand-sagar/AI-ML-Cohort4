# # ============================================
# # Lab 1: Comments, Indentation & Blocks
# # ============================================
# # Goal: understand how Python "structures" code WITHOUT { } braces.

# # ---- Single-line comment ----
# # Anything after a '#' is ignored by Python. Use it to explain WHY, not WHAT.

# print("Hello, Python")  # inline comment: runs the line, ignores this text


# # ---- Multi-line string / docstring ----
# """
# Triple quotes create a multi-line string.
# When placed at the top of a file/function/class, it becomes a 'docstring'
# (documentation that tools and help() can read).
# """


# # ---- Blocks are defined by INDENTATION (4 spaces), not braces ----
# # In C/Java:  if (day == 1) { print("mon"); }
# # In Python:  the indented lines below the ':' form the block.

# day = 1

# if day == 1:
#     print("mon")
# elif day == 2:
#     print("tue")
# elif day == 3:
#     print("wed")        # <- this block runs because day == 3
# else:
#     print("some other day")


# # ---- Indentation must be CONSISTENT ----
# # Mixing tabs and spaces, or wrong indent levels, raises IndentationError.
# def show():
#     print("line 1 in block")
#     print("line 2 in block")   # same indent = same block

# print("outside the function")  # dedented = back to top level

# show()


# # ---- 'pass' = an empty block placeholder ----
# # Python does not allow an empty block, so use 'pass' when you have nothing yet.
# def not_implemented_yet():
#     pass


# # ---- TRY THIS (uncomment to explore) ----
# # Wrong indentation -> IndentationError:
# day = 8
# if day == 3:
#     print("this will error")     # not indented under the if

# # A line that is too long can be continued with a backslash \ :
# # total = 1 + 2 + 3 + \
# #         4 + 5
# # print(total)
