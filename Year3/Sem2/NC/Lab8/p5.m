f = @(x) 1 / (4 + sin(20 * x));

repeated_simpson(10, f, 0, pi)
repeated_simpson(30, f, 0, pi)