# Define AND Gate
def AND(x1, x2):
  
  # Params : weight & bias
  w1, w2, theta = 0.5, 0.5, 0.7
  
  # Linear combination
  lin_comb = w1 * x1 + w2 * x2
  
  # Gate implementation
  if lin_comb <= theta:
    return 0
  elif lin_comb > theta:
    return 1
  
  
# Give inputs
output1 = AND(0, 0)
output2 = AND(1, 0)
output3 = AND(0, 1)
output4 = AND(1, 1)

print(output1)
print(output2)
print(output3)
print(output4)
