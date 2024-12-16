# Write a Python program to check if one string contains another

A = str("something at my car")
b = str("something")

print(b in A)  # True
print(A in b)  # False

sdf = str("Assalomu alaykum mening qadrdon dostlarim, uchrashganimiz juda yaxshi boldi")
sdg = str("uchrashganimiz juda yaxshi boldi")
sdh = str("juda yaxshi bolmadi")

print(sdf in sdg) # false
print(sdg in sdf) # true
print(sdh in sdf) # false