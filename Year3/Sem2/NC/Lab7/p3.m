[x, y] = ginput(10);
x
y

p = polyfit(x, y, 2);

x_plot = min(x):0.01:max(x);
y_plot = polyval(p, x_plot);

plot(x, y, 'r+');
hold on
plot(x_plot, y_plot, 'b-');
hold off