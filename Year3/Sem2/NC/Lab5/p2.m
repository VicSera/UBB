x = [1 2];
y = [0 0.6931];
df = [1 0.5];

res = hermite(1.5, x, y, df)
error = abs(res - log(1.5))