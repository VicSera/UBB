x = linspace(0, 10, 21);
y = (1 + cos(pi * x)) ./ (x .+ 1);

x_plot = 0:0.01:10;
y_plot = lagrange(x_plot, x, y);

plot(x_plot, y_plot);