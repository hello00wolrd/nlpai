import torch

Y = torch.randn(4, 5)
before = id(Y)
X = torch.arange(20).reshape(4, 5)
# Y = X + Y
ans = (id(Y) == before)
# False
Y[:] = X + Y
ans = (id(Y) == before)
# True
print("0")
