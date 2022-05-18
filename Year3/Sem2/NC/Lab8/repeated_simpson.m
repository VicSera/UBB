function res = repeated_simpson(n, f, a, b)
  points = linspace(a, b, n);
  s1 = 0;
  s2 = 0;
  for i = 2:n
    s1 += f((points(i - 1) + points(i)) / 2);
  endfor
  for i = 1:n-1
    s2 += f(points(i));
  endfor
  
  res = (b - a) * (f(a) + f(b) + 4*s1 + 2*s2) / (6 * n);
endfunction