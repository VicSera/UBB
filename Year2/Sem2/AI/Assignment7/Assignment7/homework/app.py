import torch
import math
import models

if __name__ == '__main__':
    filepath = "MathNet_3hidden.pt"
    ann = models.MathNet(2, 15, 1).cuda()

    ann.load_state_dict(torch.load(filepath))
    ann.eval()

    while True:
        x1, x2 = float(input("x1 = ")), float(input("x2 = "))
        x = torch.tensor([x1, x2]).cuda()
        y = ann(x).tolist()
        print(str(ann(x).tolist()[0]) + ' (actual: ' + str(math.sin(x1 + x2 / math.pi)) + ')')

