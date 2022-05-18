f = @(x) 100 / (x .^ 2) * sin(10./x);
a = 1;
b = 3;
eps = 10 ^ -4;

function res = adaptive_simpson(f, a, b, eps)
  m = (a + b) / 2;
  i1 = simpson(f, a, b);
  i2 = simpson(f, a, m) + simpson(f, m, b);
  
  if abs(i1 - i2) < 15 * eps
    res = i2;
  else
    res = adaptive_simpson(f, a, m, eps / 2) + adaptive_simpson(f, m, b, eps / 2);
  endif
endfunction

obtained = adaptive_simpson(f, a, b, eps)
s50 = repeated_simpson(50, f, a, b)
s100 = repeated_simpson(100, f, a, b)
