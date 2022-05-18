f = @(x) exp(-(x .^ 2));
a = 1;
b = 1.5;

function res = repeated_rect(f, a, b, n)
  values = linspace(a, b, n);
  res = ((b - a) / n) * sum(f(values));
endfunction

# a)
rect_height = f((a + b) / 2);
rect_area = (b - a) * rect_height

# b)
x = 0:0.001:3;
y = f(x);
x_rect = [1, 1, 1.5, 1.5, 1];
y_rect = [0, rect_height, rect_height, 0, 0];

plot(x, y);
hold on;
plot(x_rect, y_rect);
hold off;

# c)
rect_150 = repeated_rect(f, a, b, 150)
rect_500 = repeated_rect(f, a, b, 500)