h = 0.25;
i = 0:6;
x = 1 + h*i;
f = @(x) sqrt(5 * x.^2 + 1);

res = zeros(length(i), length(i) + 1)
for row = 1:length(i)
  res(row, 1) = i(row);
endfor
for row = 1:length(i)
  res(row, 2) = f(x(row));
endfor

for col = 3:(length(i) + 1)
  for row = 1:(length(i) - col + 2)
    res(row, col) = (res(row + 1, col - 1) - res(row, col - 1)) / (res(row + col - 2, 1) - res(row, 1));
  endfor
endfor

res