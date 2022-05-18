f = @(x) 2 ./ (1 + x .^ 2);
a = 0;
b = 1;

eps = 10 ^ -4;

# a)
function res = romberg(f, a, b, n)
  h = b - a;
  if n == 0
    res = (h / 2) * (f(a) + f(b));
  else
    j = 1:(2^(n-1));
    res = (1/2) * romberg(f, a, b, n-1) + ((h / (2 ^ n)) * sum(f(a + h*(2*j - 1) / (2 ^ n))));
  endif
endfunction

previous = romberg(f, a, b, 0);
i = 1;
current = romberg(f, a, b, i);

err = abs(current - previous);
while err > eps
  previous = current;
  i += 1;
  current = romberg(f, a, b, i);
  err = abs(current - previous);
endwhile

err
current
i

# b)

function res = romberg_aitken(f, a, b, eps)
  matrix = [];
  matrix(1, 1) = repeated_trapezium(1, f, a, b);
  row = 0;
  err = eps + 1;
  while err > eps
    row += 1;
    matrix(row + 1, 1) = repeated_trapezium(row + 1, f, a, b);
    for column = 1:row
      matrix(row + 1, column + 1) = (4^(-column) * matrix(row, column) - matrix(row + 1, column)) / (4^(-column) - 1);
    endfor
    err = abs(matrix(row + 1, row + 1) - matrix(row, row));
  endwhile
  res = matrix(row + 1, row + 1);
endfunction

b = romberg_aitken(f, a, b, eps)
