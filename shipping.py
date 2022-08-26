weight = 4.8
# ground shipping 
cost_ground = 20.00
cost_ground_premium = 125.00
if weight <= 2:
  print(cost_ground + (weight * 1.50))
if weight >= 2 and weight <= 6:
  print(cost_ground + (weight * 3.00))
if weight > 6 and weight <= 10:
  print(cost_ground + (weight * 4.00))
if weight > 10:
  print(cost_ground + (weight * 4.75))
if cost_ground_premium:
  print(weight * 0 + cost_ground_premium)
# drone shipping
cost_drone_shipping = 0.00
if weight < 2:
  print(weight * 4.50)
if weight > 2 and weight <= 6:
  print(weight * 9.00)
if weight > 6 and weight <= 10:
  print(weight * 12.00)
if weight > 10:
  print(weight * 14.25)
