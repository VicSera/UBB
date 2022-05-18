function res = repeated_trapezium(n, f, a, b)
  points = linspace(a, b, n - 1);
  
  res = (b - a) * (f(a) + f(b) + 2 * sum(f(points))) / (2 * n);
endfunction