x = [0, pi/2, pi, 3*pi/2, 2*pi];
y = sin(x)

spline(x, y, pi/4)
spline(x, [cos(0) y cos(2*pi)], pi/4)

x_plt = 0:0.1:2*pi;
y_plt = sin(x_plt);
y2_plt = spline(x, y, x_plt);
y3_plt = spline(x, [cos(0) y cos(2*pi)], x_plt);

plot(x_plt, y_plt);
hold on
plot(x_plt, y2_plt);
hold on
plot(x_plt, y3_plt);
hold off