[x, y] = ginput(5)
x_plot = min(x):0.01:max(x);
y_plot = spline(x, y, x_plot);

plot(x, y, 'b+')
hold on
plot(x_plot, y_plot, 'r-')
hold off