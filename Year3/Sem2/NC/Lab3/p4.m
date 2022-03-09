9999
function [max_error] = interpolation_error(n)
  n
  x = zeros(1, n + 1);
  y = zeros(1, n + 1);
  
  f = @(x) 1 ./ (1 + x .^ 2);
  
  for i = 1:n + 1
    x(i) = (i - 1) * 10 / n - 5;
  endfor
  y = f(x);
  
  max_error = 0;
  for i = 0:100
    yi = i / 10 - 5;
    error = abs(f(yi) - lagrange(yi, x, y));
    
    if error > max_error
      max_error = error;
    endif
  endfor
endfunction

for n = 2:2:8
  interpolation_error(n)
endfor