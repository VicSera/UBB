x = [1 1.5 2 3 4];
y = [0 0.17609 0.30103 0.47712 0.60206];

lg_2_5= newton(2.5, x, y)
lg_3_25 = newton(3.25, x, y)

i = 10:35;
yi = i / 10;
fyi = log10(yi);
N4f = zeros(length(fyi), 1);

for k = 1 : length(yi)
  N4f(k) = newton(yi(k), x, y);
endfor

E = max(abs(fyi - N4f)(:))