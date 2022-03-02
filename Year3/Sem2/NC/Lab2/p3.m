x = -1:0.001:3;
x0 = 0;

hold on;

for n = 1:6
  pn = zeros(size(x));
  for k = 0:n
    pn = pn + (x - x0).^k / factorial(k);
  endfor
  
  plot(x, pn);
endfor

hold off