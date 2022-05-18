f = @(x) 2 ./ (1 + x .^ 2);
a = 0;
b = 1;

# a)
trapezium(f, a, b)

# b)
x = 0:0.01:1;
y = f(x);
x_trap = [0 0 1 1];
y_trap = [0 f(0) f(1) 0];
plot(x, y, 'b-')
hold on
plot(x_trap, y_trap, 'r+')
hold off

# c)
simpson(f, a, b)