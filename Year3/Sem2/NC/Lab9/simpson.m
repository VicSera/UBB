function res = simpson(f, a, b)
  res = (b - a) * (f(a) + 4*f((a+b)/2) + f(b)) / 6;
endfunction