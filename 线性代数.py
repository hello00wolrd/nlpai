import torch

#
# # x = torch.tensor(3.0)
# # y = torch.tensor(2.0)
# # print(x+y)
# # print(x*y)
# # print(x-y)
# # print(x**y)
# # print(x//y)
#
# x = torch.arange(4)
# print(x[3])
# print(len(x))
# print(x.shape)  # torch.Size([4])
# # 形状（shape）是一个元素组，列出了张 量沿每个轴的长度（维数）。
# A = torch.arange(20).reshape(5, 4)
# print(A)
# print(A.T)
# # 转置
# B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
# print(B)
# print(B == B.T)
# X = torch.arange(24).reshape(2, 3, 4)
# print(X)
# A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
# B = A.clone()
# # 通过分配新内存，将A的一个副本分配给B
# print(A, '\n', B)
# print(A * B)  # 标量乘
#
# x = torch.arange(4, dtype=torch.float32)
# print(x.sum())
#
# A_sum_axis0 = A.sum(axis=0)  # 沿着轴0降维
# print(A_sum_axis0)
# A_sum_axis1 = A.sum(axis=1)  # 沿着轴1降维
# print(A_sum_axis1)
# print(A.mean(axis=0))
# print(A.shape[0])
# print(A.sum(axis=0) / A.shape[0])
#
# Sum_A = A.sum(axis=1, keepdims=True)  # 非降维求和
# print(Sum_A)
# print(A / Sum_A)
#
# print(A.cumsum(axis=0))  # 沿轴0求累计总和
#
# y = torch.ones(4, dtype=torch.float32)
# print(torch.dot(x, y))  # 向量点积
ax = torch.ones((4, 9))
print(ax)
