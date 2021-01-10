steel = [4.6, 0.7, 4.2, 1.9, 4.8, 6.1, 4.7, 5.5, 5.4];
glass = [2.5, 1.3, 2.0, 1.8, 2.7, 3.2, 3.0, 3.5, 3.4];

alpha = 0.05;
steelN = length(steel);
glassN = length(glass);

# a)
# H0: variances are equal
# H1: variances are different - two-tailed test

f1 = finv(alpha / 2, steelN - 1, glassN - 1);
f2 = finv(1 - alpha / 2, steelN - 1, glassN - 1);

[H, P, CI, stats] = vartest2(steel, glass, "alpha", alpha);

if H == 0
  fprintf('The null hypothesis is accepted - the variances seem to be equal\n');
else
  fprintf('The null hypothesis is rejected - the variances seem to differ\n');
endif

fprintf('RR: (%6.3f, %6.3f) U (%6.3f, %6.3f)\n', -inf, f1, f2, inf);
fprintf('CI: (%6.3f, %6.3f)\n', CI);
fprintf('P-value: %6.3f\n', P);
fprintf('Stats: %6.3f\n', stats.fstat);

# b)
# H0: heatLossSteel = heatLossGlass
# H1: heatLossSteel > heatLossGlass -> right tailed test

t = tinv(1 - alpha, steelN + glassN - 2);

[H, P, CI, stats] = ttest2(steel, glass, "alpha", alpha, "tail", "right");

if H == 0
  fprintf('The null hypothesis is accepted - the heat loss seems to be equal\n');
else
  fprintf('The null hypothesis is rejected - the heat loss seems to be higher for steel\n');
endif

fprintf('RR: (%6.3f, %6.3f)\n', t, inf);
fprintf('CI: (%6.3f, %6.3f)\n', CI);
fprintf('P-value: %6.3f\n', P);
fprintf('Stats: %6.3f\n', stats.tstat);