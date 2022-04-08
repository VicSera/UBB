x = [1 2 3 4 5 6 7];
y = [13 15 20 14 15 13 10];

m = length(x);
sx = sum(x);
denominator = (m + 1) * sum(x .* x) - sx * sx;
a = ((m + 1) * sum(x .* y) - sx * sum(y)) / denominator
b = (sum(x .* x) * sum(y) - sum(x .* y) * sx) / denominator 

pred = a * 8 + b

E = sum((y - (a * x + b)) .^ 2)

xplot = 1:10;
yplot = a * xplot + b;

plot(x, y, 'r+')
hold on
plot(xplot, yplot, 'b-')
hold off