x = [0 3 5 8 13];
y = [0 225 383 623 993];
df = [75 77 80 74 72];

pos = hermite(10, x, y, df)
speed = pos / 10
