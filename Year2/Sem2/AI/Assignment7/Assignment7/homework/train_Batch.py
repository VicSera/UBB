import torch
from torch.utils.data import DataLoader, TensorDataset
import math

import models

if __name__ == '__main__':
    print('Running training on: ' + torch.cuda.get_device_name(0))

    x = torch.combinations(torch.linspace(-10, 10, 100), with_replacement=True).cuda()
    y = torch.unsqueeze(torch.sin(x[:, 0] + torch.div(x[:, 1], math.pi)), dim=1).cuda()

    dataset = TensorDataset(x, y)
    with open('dataset.dat', 'wb') as file:
        torch.save(dataset, file)

    dataLoader = DataLoader(dataset, batch_size=16)

    lossFunction = torch.nn.MSELoss()

    model = models.MathNet(n_feature=2, n_hidden=15, n_output=1).cuda()

    optimizer_batch = torch.optim.SGD(model.parameters(), lr=0.001)

    loss_list = []
    avg_loss_list = []

    n_epochs = 2000

    for epoch in range(n_epochs):
        for batch_x, batch_y in dataLoader:
            prediction = model(batch_x)

            loss = lossFunction(prediction, batch_y)
            loss_list.append(loss)
            loss.backward()

            optimizer_batch.step()
            optimizer_batch.zero_grad()

        if epoch % 100 == 0:
            y_pred = model(x)
            loss = lossFunction(y_pred, y)
            print('\repoch: {}\tLoss =  {:.5f}'.format(epoch, loss))

    filepath = "MathNet_3hidden.pt"
    torch.save(model.state_dict(), filepath)
