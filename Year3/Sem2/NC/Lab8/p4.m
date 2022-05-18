a = 1;
b = 2;
f = @(x) x.*log(x);
err = inf;
expected = 0.63629;
n = 1;


while err >= 0.001
  aprox = repeated_trapezium(n, f, a, b);
  n += 1;
  err = abs(expected - aprox);
endwhile
n
aprox