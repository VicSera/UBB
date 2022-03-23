x1 = [-2 -1 0 1 2];
y1 = [1/9 1/3 1 3 9];
p1 = 1/2;

x2 = [0 1 2 4 5];
y2 = [sqrt(0) sqrt(1) sqrt(2) sqrt(4) sqrt(5)];
p2 = 3;

function [res] = neville(p, x, y)
  n = length(x);
  table = zeros(n, n);

  for i = 1 : n
    table(i, 1) = y(i);
  endfor

  for i = 1 : n
    for j = 1 : i - 1
      table(i, j + 1) = ((table(j, j) * (x(i) - p)) - (table(i, j) * (x(j) - p))) / (x(i) - x(j));
    endfor
  endfor

  res = table(n, n);
endfunction

neville(p1, x1, y1)
neville(p2, x2, y2)

