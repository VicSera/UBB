x = [0 10 20 30 40 60 80 100];
y = [0.0061 0.0123 0.0234 0.0424 0.0738 0.1992 0.4736 1.0133];

p1 = polyfit(x, y, 5);
p2 = polyfit(x, y, 3);

pred1 = polyval(p1, 45)
pred2 = polyval(p2, 45)
actual = 0.095848;

error1 = abs(actual - pred1)
error2 = abs(actual - pred2)

xplot = 0:0.1:100;
yplot1 = polyval(p1, xplot);
yplot2 = polyval(p2, xplot);

plot(x, y, 'r+')
hold on
plot(xplot, yplot1, 'b-')
plot(xplot, yplot2, 'g-')
hold off