premium = [22.4, 24.5, 21.6, 22.4, 24.8, 21.7, 23.4, 23.3, 21.6, 20.0];
regular = [17.7, 19.6, 12.1, 15.4, 14.0, 14.8, 19.6, 14.8, 12.6, 12.2];

meanP = mean(premium);
meanR = mean(regular);

varP = var(premium);
varR = var(regular);

lengthP = length(premium);
lengthR = length(regular);

oneMinusAlpha = input('Confidence: ');
alpha = 1 - oneMinusAlpha;
conf = 100 * oneMinusAlpha;

... a)
quantile = tinv(1 - alpha / 2, lengthP + lengthR - 2);
sp2 = ((lengthP - 1) * varP + (lengthR - 1) * varR) / (lengthP + lengthR - 2);
sp = sqrt(sp2);
halfIntervalLength = quantile * sp * sqrt(1 / lengthP + 1 / lengthR);

limitLeft = meanP - meanR - halfIntervalLength;
limitRight = meanP - meanR + halfIntervalLength;

fprintf('a) CI for difference of means with confidence %6.1f percent: [%6.3f, %6.3f ]\n', conf, limitLeft, limitRight);

... b)
c = (varP / lengthP) / (varP / lengthP + varR / lengthR);
oneOverN = (c ^ 2) / (lengthP - 1) + ((1 - c) ^ 2) / (lengthR - 1);
quantile = tinv(1 - alpha / 2, 1 / oneOverN);
halfIntervalLength = quantile * sqrt(varP / lengthP + varR / lengthR);

limitLeft = meanP - meanR - halfIntervalLength;
limitRight = meanP - meanR + halfIntervalLength;

fprintf('b) CI for difference of means with confidence %6.1f percent: [%6.3f, %6.3f ]\n', conf, limitLeft, limitRight);

... c)
leftQuantile = finv(1 - alpha / 2, lengthP - 1, lengthR - 1);
rightQuantile = finv(alpha / 2, lengthP - 1, lengthR - 1);
varianceRatio = varP / varR;

limitLeft = varianceRatio / leftQuantile;
limitRight = varianceRatio / rightQuantile;

fprintf('a) CI for ratio of variances with confidence %6.1f percent: [%6.3f, %6.3f ]\n', conf, limitLeft, limitRight);