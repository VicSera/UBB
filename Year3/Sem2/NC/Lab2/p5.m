x = [2 4 6 8]
f = [4 8 14 16]

res = zeros(length(x), length(x) + 1)
for row = 1:length(x)
  res(row, 1) = x(row);
endfor
for row = 1:length(x)
  res(row, 2) = f(row);
endfor

for col = 3:(length(x) + 1)
  for row = 1:(length(x) - col + 2)
    res(row, col) = (res(row + 1, col - 1) - res(row, col - 1)) / (res(row + col - 2, 1) - res(row, 1));
  endfor
endfor

res