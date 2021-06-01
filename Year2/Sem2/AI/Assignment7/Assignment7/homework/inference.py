import torch

import models
import math
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filepath = "MathNet_3hidden.pt"
    ann = models.MathNet(2, 15, 1).cuda()

    x = torch.cartesian_prod(torch.tensor([1.]), torch.linspace(-10, 10, 100)).cuda()
    y = torch.unsqueeze(torch.sin(x[:, 0] + torch.div(x[:, 1], math.pi)), dim=1).cuda()

    ann.load_state_dict(torch.load(filepath))
    ann.eval()

    pred = ann(x)
    plt.plot(x[:, 1].tolist(), y.tolist())
    plt.plot(x[:, 1].tolist(), pred.tolist())
    plt.show()
