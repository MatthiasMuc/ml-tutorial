import torch

x = torch.rand(5,3)
print(x)
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)
