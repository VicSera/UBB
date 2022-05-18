p = 75;
r = 110;
f = @(x) (1 - ((p / r) ^ 2) * sin(x)) .^ 0.5;
int = repeated_trapezium(2, f, 0, 2*pi);
H = 60 * r * int / (r^2 - p^2)