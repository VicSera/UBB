# bank employees
BE = [3.1, 2.9, 3.8, 3.3, 2.7, 3.0, 2.8, 2.5, 2.6, 2.0, 3.2, 2.4, 2.3, 3.1, 2.1, 3.4];
# other employees
OE = [6.9, 6.4, 4.7, 4.3, 5.1, 6.3, 5.9, 5.4, 5.3, 5.2, 5.1, 5.9, 5.8, 4.9];

# compute useful values - length, mean and standard deviation
nBE = length(BE);
nOE = length(OE);

mBE = mean(BE);
mOE = mean(OE);

sBE = std(BE);
sOE = std(OE);

alpha = 0.05;

fprintf('a)\n');

# compute the quantiles
f1 = finv(alpha / 2, nBE - 1, nOE - 1);
f2 = finv(1 - alpha / 2, nBE - 1, nOE - 1);

# H0: variances are equal
# H1: variances are different
[H, P, CI, stats] = vartest2(BE, OE, "alpha", alpha);

# print test results
fprintf('H: %1.0f\n', H)
if H == 0
    fprintf('The null hypothesis is NOT rejected\nThe variances seem to be equal\n')
else
    fprintf('The null hypothesis is rejected\nThe variances seem to differ\n')
end
fprintf('RR: (%6.4f, %6.4f) U (%6.4f, %6.4f)\n', -inf, f1, f2, inf)
fprintf('The test value: %6.4f\n', stats.fstat)
fprintf('P-value: %6.4f\n', P)

fprintf('\nb)\n');

t = tinv(1 - alpha / 2, nBE + nOE - 2);
sp2 = ((nBE - 1) * sBE ^ 2 + (nOE - 1) * sOE ^ 2) / (nBE + nOE - 2);
sp = sqrt(sp2);

limitLeft = mBE - mOE - t * sp * sqrt(1 / nBE + 1 / nOE);
limitRight = mBE - mOE + t * sp * sqrt(1 / nBE + 1 / nOE);

fprintf('The %3.2f percent confidence interval for the difference of paper thrown out: (%6.3f, %6.3f)\n', 100 * (1 - alpha), limitLeft, limitRight);