X = [20 * ones(1, 2), 21, 22 * ones(1, 3), 23 * ones(1, 6),...
     24 * ones(1, 5), 25 * ones(1, 9), 26 * ones(1, 2), 27 * ones(1, 2)]
Y = [75 * ones(1, 3), 76 * ones(1, 2), 77 * ones(1, 2), 78 * ones(1, 5),...
     79 * ones(1, 8), 80 * ones(1, 8), 81, 82]
     
... a)
meanX = mean(X)
meanY = mean(Y)

... b)
varX = var(X, 1)
varY = var(Y, 1)

... c)
covXY = cov(X, Y, 1)

... d)
corrCoefXYMat = corrcoef(X, Y)
corrCoefXY = corrCoefXYMat(1, 2)
     
