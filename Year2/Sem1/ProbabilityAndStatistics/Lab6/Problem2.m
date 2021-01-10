premium = [22.4, 24.5, 21.6, 22.4, 24.8, 21.7, 23.4, 23.3, 21.6, 20.0];
regular = [17.7, 19.6, 12.1, 15.4, 14.0, 14.8, 19.6, 14.8, 12.6, 12.2];

lengthP = length(premium);
lengthR = length(regular);

alpha = 0.05;

fprintf('a)\n');

f1 = finv(alpha / 2, lengthP - 1, lengthR - 1);
f2 = finv(1 - alpha / 2, lengthP - 1, lengthR - 1);

# H0: variances are equal
# H1: variances are different
[H, P, CI, stats] = vartest2(premium, regular, "alpha", alpha);

if H == 0
    fprintf('The null hypothesis is accepted because the variances seem to be equal\n')
else
    fprintf('The null hypothesis is rejected because the variances seem to differ\n')
end
fprintf('RR: (%6.4f, %6.4f) U (%6.4f, %6.4f)\n', -inf, f1, f2, inf)
fprintf('the test statistic: %6.4f\n', stats.fstat)
fprintf('P-value: %6.4f\n', P)

fprintf('b)\n');

# H0: mP = mR
# H1: mP > mR -> right tailed test

t = tinv(1 - alpha, lengthP + lengthR - 2);

[H, P, CI, stats] = ttest2(premium, regular, "alpha", alpha, "tail", "right");

if H == 0
    fprintf('The null hypothesis is accepted because the average mileages seem to be equal\n')
else
    fprintf('The alternate hypothesis is accepted because the average mileage for premium is higher than for regular gas\n')
end
fprintf('RR: (%6.4f, %6.4f)\n', t, inf)
fprintf('the test statistic: %6.4f\n', stats.tstat)
fprintf('P-value: %6.4f\n', P)