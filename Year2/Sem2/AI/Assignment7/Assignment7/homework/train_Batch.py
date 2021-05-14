import torch

import models

if __name__ == '__main__':
    print('Running training on: ' + str(torch.cuda.current_device()))

    x = torch.combinations(torch.linspace(-10, 10, 100), with_replacement=True)
    x = x.cuda()

    y = torch.unsqueeze(torch.sin(x[:, 0] + torch.div(1, x[:, 1])), dim=1)
    y = y.cuda()

    lossFunction = torch.nn.MSELoss()

    model = models.MathNet(n_feature=2, n_hidden=10, n_output=1)
    model.cuda()

    optimizer_batch = torch.optim.SGD(model.parameters(), lr=0.2)

    loss_list = []
    avg_loss_list = []

    batch_size = 16
    n_batches = int(len(x) / batch_size)

    n_epochs = 2000

    for epoch in range(n_epochs):
        for batch in range(n_batches):
            batch_x, batch_y = x[batch * batch_size: (batch + 1) * batch_size], \
                               y[batch * batch_size: (batch + 1) * batch_size]

            # we compute the output for this batch
            prediction = model(batch_x)

            # we compute the loss for this batch
            loss = lossFunction(prediction, batch_y)

            # we save it for graphics
            loss_list.append(loss)

            # we set up the gradients for the weights to zero (important in pytorch)
            optimizer_batch.zero_grad()

            # we compute automatically the variation for each weight (and bias) of the network
            loss.backward()

            # we compute the new values for the weights
            optimizer_batch.step()

        # we print the loss for all the dataset for each 10th epoch
        if epoch % 100 == 99:
            y_pred = model(x)
            loss = lossFunction(y_pred, y)
            print('\repoch: {}\tLoss =  {:.5f}'.format(epoch, loss))

    # Specify a path
    filepath = "MathNet.pt"

    # save the model to file
    torch.save(model.state_dict(), filepath)

# visualise the parameters for the ann (aka weights and biases)
# for name, param in ann.named_parameters():
#     if param.requires_grad:
#         print (name, param.data)
