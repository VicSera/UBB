x = [7, 7, 4, 5, 9, 9,...
     4, 12, 8, 1, 8, 7,...
     3, 13, 2, 1, 17, 7,...
     12, 5, 6, 2, 1, 13,...
     14, 10, 2, 4, 9, 11,...
     3, 5, 12, 6, 10, 7];

oneMinusAlpha = input('1 - Alpha is: ');
alpha = 1 - oneMinusAlpha;
conf = 100 * oneMinusAlpha;
meanX = mean(x);
lengthX = length(x);
sqrtLengthX = sqrt(lengthX);
        
... a)
sigma = 5;
normalQuantile = norminv(1 - alpha / 2);

limitLeft = meanX - sigma * normalQuantile / sqrtLengthX;
limitRight = meanX + sigma * normalQuantile / sqrtLengthX;

fprintf('a) CI for mean with confidence %6.3f percent is [%6.3f, %6.3f ]\n', conf, limitLeft, limitRight)

... b)
sigma = std(x);
studentQuantile = tinv(1 - alpha / 2, lengthX - 1);

limitLeft = meanX - sigma * studentQuantile / sqrtLengthX;
limitRight = meanX + sigma * studentQuantile / sqrtLengthX;

fprintf('B) CI for mean with confidence %6.3f percent is [%6.3f, %6.3f ]\n', conf, limitLeft, limitRight)

... c)
varianceX = var(x);
leftChiSqQuantile = chi2inv(1 - alpha / 2, lengthX - 1);
rightChiSqQuantile = chi2inv(alpha / 2, lengthX - 1);

limitLeft = (lengthX - 1) * varianceX / leftChiSqQuantile;
limitRight = (lengthX - 1) * varianceX / rightChiSqQuantile;

fprintf('C) CI for variance with confidence %6.3f percent is [%6.3f, %6.3f ]\n', conf, limitLeft, limitRight)