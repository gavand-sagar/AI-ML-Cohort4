# while True:
#     try:
#         v1 = input("Enter some value 1:")
#         v2 = input("Enter some value 2:")
#         result = int(v1) / int(v2)
#         print("v1/v2 = " + str(result))
#     except ValueError as e:
#         print(e)
#         print("Type valid number, please try again.")
#     except ZeroDivisionError as e:
#         print("Can't devide with zero")
#     except:
#         print("Can't devide with zero")
#     finally:
#         print("Done....")

# # v = "hello"
# # print(int(v))


# class InsufficientFundsError(Exception):
#     pass

# class Account:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientFundsError(f"Need {amount}, have {self.balance}")
#         self.balance -= amount
#         return self.balance

# acc = Account(1000)
# try:
#     acc.withdraw(500)
# except InsufficientFundsError as e:
#     print("Blocked:", e)
# except ValueError as e:
#     print(e)