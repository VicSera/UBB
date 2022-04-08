x = linspace(-5, 5, 5);
y = sin(2*x);
df = 2*cos(2*x);

x_plot = -5:0.1:5;
for i = 1 : length(x_plot)
  y_plot(i) = hermite(x_plot(i), x, y, df);
endfor

plot(x_plot, y_plot, 'b-');
hold on;
plot(x, y, 'r+');
hold off;