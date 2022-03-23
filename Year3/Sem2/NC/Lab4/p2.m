x = [1 2 3 4 5];
y = [22 23 25 30 28];

prediction = newton(2.5, x, y)

X = 1:0.01:5;
Y = zeros(length(X), 1);
for i = 1 : length(X)
  Y(i) = newton(X(i), x, y);
endfor

plot(X, Y, 'b-');
hold on;
plot(x, y, 'r+');
hold off;