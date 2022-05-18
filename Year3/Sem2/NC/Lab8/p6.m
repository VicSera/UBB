f = @(t) exp(-(t ^ 2));
actual = 0.520499876
est1 = (2 / sqrt(pi)) * repeated_simpson(4, f, 0, 0.5)
est2 = (2 / sqrt(pi)) * repeated_simpson(10, f, 0, 0.5)

err1 = abs(actual - est1)
err2 = abs(actual - est2)