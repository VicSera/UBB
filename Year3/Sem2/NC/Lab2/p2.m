T = @(n,x) cos(n * acos(x));

x = -1:0.001:1;

plot(x, T(1, x));
hold on
plot(x, T(2, x), 'r-');
plot(x, T(3, x), 'b+');
hold off