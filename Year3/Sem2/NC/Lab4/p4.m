x = [64 81 100 121 144 169 196];
y = [8 9 10 11 12 13 14];

n = length(x);
table = zeros(n, n);
p = 115;
eps = 0.001;

for i = 1 : n
  table(i, 1) = y(i);
endfor

for i = 1 : n
  for j = 1 : i - 1
    table(i, j + 1) = ((table(j, j) * (x(i) - p)) - (table(i, j) * (x(j) - p))) / (x(i) - x(j));
  endfor
  
  if i > 1 && abs(table(i,i) - table(i-1,i-1)) <= eps
    table(i, i)
    break
  endif
endfor