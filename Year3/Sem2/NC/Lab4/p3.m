x = linspace(0, 6, 13);
y = exp(sin(x));

X = 0:0.1:6;
Y = zeros(length(X), 1);

for i = 1 : length(X)
  Y(i) = newton(X(i), x, y);
endfor

plot(X, Y, 'b-');
hold on;
plot(x, y, 'r+');
hold off;