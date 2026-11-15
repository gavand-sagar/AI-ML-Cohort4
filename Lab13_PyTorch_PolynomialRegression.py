# =====================================================================
# Lab13 - Polynomial Regression in PyTorch: Fuel Efficiency vs Speed
# =====================================================================
# Every demo below is independent.
# Keep the imports, then comment / uncomment one demo at a time.
#
# Main example: predict a car's fuel efficiency (km per litre) from speed
#   speed (km/h)    : 20    40    65    90    120
#   efficiency km/L : 12    16    18    16    9      -> goes UP, peaks, comes DOWN
#
# True formula (hidden from the model): efficiency = 18 - 0.003 * (speed - 65)^2
# =====================================================================

import torch
import torch.nn as nn


# # =====================================================================
# # DEMO 1 - The data: a hill, not a line
# # =====================================================================
# print("\n========== DEMO 1: The data ==========")

# torch.manual_seed(0)
# speed = torch.linspace(20, 120, 100).reshape(-1, 1)        # shape (100, 1)
# eff = 18 - 0.003 * (speed - 65) ** 2 + torch.randn(100, 1) * 0.6

# print("speed shape:", speed.shape, "| eff shape:", eff.shape)
# print("\nspeed | efficiency")
# for i in range(0, 100, 11):
#     bar = "#" * int(eff[i].item())
#     print(f"{speed[i].item():5.0f} | {eff[i].item():5.2f}  {bar}")

# print("\nTakeaway:")
# print("  - Slow: low gears -> poor mileage. ~65 km/h: best. Fast: air drag -> poor again.")
# print("  - Efficiency goes UP, peaks, then comes DOWN -> a HILL.")


# =====================================================================
# DEMO 2 - A straight line fails
# # =====================================================================
# print("\n========== DEMO 2: Straight line fails ==========")

# torch.manual_seed(0)
# speed = torch.tensor([[20.0],[40.0],[65.0],[91.0],[120.0]])
# eff = torch.tensor([[11.25],[16.51],[19.38],[15.73],[9.06]])

# x = (speed - speed.mean()) / speed.std()      # scaling (Lab12)

# model = nn.Linear(1, 1)                       # efficiency = w * x + b
# loss_fn = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.05)

# for epoch in range(2000):
#     loss = loss_fn(model(x), eff)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()


# with torch.no_grad():
#     pred = model(x)


# output = model(torch.tensor([130.0]))
# print (output)
# print("\nTakeaway:")
# print("  - A line can go up or down, but it can NEVER turn around.")
# print("  - Too high at both ends, too low at the peak.")
# print("  - Errors: - at ends, + in middle -> a PATTERN = wrong model shape.")
# print("  - This is UNDERFITTING. More epochs will not fix it.")


# # =====================================================================
# # DEMO 3 - The fix: add speed^2 as a new column
# # =====================================================================
# print("\n========== DEMO 3: Polynomial features ==========")

# speed = torch.tensor([[20.0], [65.0], [120.0]])

# x = (speed - 70) / 30                          # 1. scale first (70 ~ mean, 30 ~ std of our speeds)
# X_poly = torch.cat([x, x ** 2], dim=1)         # 2. then add x^2 as a new column

# print("x shape     :", x.shape)
# print("X_poly shape:", X_poly.shape)
# print("X_poly (columns: x, x^2):\n", X_poly)

# print("\nwithout scaling speed^2 would be:", (speed ** 2).squeeze().tolist())

# print("\nTakeaway:")
# print("  - New model: efficiency = w1 * x + w2 * x^2 + b  ->  nn.Linear(2, 1)")
# print("  - Same nn.Linear, same loop. We only added a COLUMN.")
# print("  - Polynomial regression = linear regression on [x, x^2].")
# print("  - Scale BEFORE squaring, else speed^2 = 14400 and training struggles (SGD -> nan).")


# =====================================================================
# # DEMO 4 - Train: linear vs polynomial
# # =====================================================================
# print("\n========== DEMO 4: Linear vs polynomial ==========")

# torch.manual_seed(0)
# speed = torch.linspace(20, 120, 100).reshape(-1, 1)
# eff = 18 - 0.003 * (speed - 65) ** 2 + torch.randn(100, 1) * 0.6

# x = (speed - speed.mean()) / speed.std()
# inputs = {
#     "linear     [x]     ": x,                               # [[20],[40],[60],[80]]
#     "polynomial [x, x^2]": torch.cat([x, x ** 2], dim=1),   # [[20,400],[40,1600],[60,3600],[80,6400]]
# }

# for name, X in inputs.items():
#     model = nn.Linear(X.shape[1], 1)
#     loss_fn = nn.MSELoss()
#     optimizer = torch.optim.Adam(model.parameters(), lr=0.05)

#     for epoch in range(2000):
#         loss = loss_fn(model(X), eff)
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     with torch.no_grad():
#         at_65 = model(X[45:46]).item()          # row 45 is speed ~65
#     print(f"{name} -> MSE {loss.item():5.2f} | at 65 km/h predicts {at_65:5.2f} (actual ~18)")

# print("\nTakeaway:")
# print("  - Only the INPUT changed: x  ->  [x, x^2].")
# print("  - Polynomial MSE ~0.36 = just the noise we added (0.6 ^ 2).")
# print("  - The curve now rises, peaks and falls, like the data.")


# =====================================================================
# DEMO 5 - Use the model: best speed + predictions
# =====================================================================
print("\n========== DEMO 5: Best speed and prediction ==========")

torch.manual_seed(0)
speed = torch.linspace(20, 120, 100).reshape(-1, 1)
eff = 18 - 0.003 * (speed - 65) ** 2 + torch.randn(100, 1) * 0.6

mean, std = speed.mean(), speed.std()
x = (speed - mean) / std
X = torch.cat([x, x ** 2], dim=1)

model = nn.Linear(2, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.05)
for epoch in range(2000):
    loss = loss_fn(model(X), eff)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# best speed = top of the hill: x = -w1 / (2 * w2)
w1, w2 = model.weight[0].tolist()
best_x = -w1 / (2 * w2)
best_speed = best_x * std.item() + mean.item()     # undo scaling
print(f"w2 = {w2:.2f} (negative -> hill)")
print(f"most efficient speed: {best_speed:.0f} km/h   (true: 65)")

# predict new speeds: SAME scaling + SAME [x, x^2]
new_speed = torch.tensor([[30.0], [65.0], [110.0]])
new_x = (new_speed - mean) / std
new_X = torch.cat([new_x, new_x ** 2], dim=1)

with torch.no_grad():
    predicted = model(new_X)

print("\nspeed | predicted km/L")
for s, p in zip(new_speed.squeeze().tolist(), predicted.squeeze().tolist()):
    print(f"{s:5.0f} | {p:6.2f}")

# print("\nTakeaway:")
# print("  - Top of a parabola: x = -w1 / (2 * w2). Unscale: x * std + mean.")
# print("  - New data must use the SAME mean/std and the SAME [x, x^2].")
# print("  - Don't overdo it: x^10 would chase the noise -> OVERFITTING.")
