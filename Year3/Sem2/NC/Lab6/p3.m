time = [0 3 5 8 13];
distance = [0 225 383 623 993];
speed = [75 77 80 74 72];

pos = spline(time, [speed(1) distance speed(length(speed))], 10)
speed = pos / 10