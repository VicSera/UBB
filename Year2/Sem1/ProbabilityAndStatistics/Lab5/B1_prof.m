% Lab #5, part B, problem 1.
% Problem 1.
% In a study of the size of various computer systems, the random variable
% $X$, the number of files stored, is considered. Past experience 
% indicates that sigma = 5. These data are obtained:
%  7  7  4  5  9  9
%  4 12  8  1  8  7
%  3 13  2  1 17  7
% 12  5  6  2  1 13
% 14 10  2  4  9 11
%  3  5 12  6 10  7
% Find a 100(1-alpha)% confidence interval for the average number of 
% files stored.

x = [7, 7, 4, 5, 9, 9, 4, 12, 8, 1, 8, 7, 3, 13, 2, 1, 17, 7,...
   12, 5, 6, 2, 1, 13, 14, 10, 2, 4, 9, 11, 3, 5, 12, 6, 10, 7];
% sample size 
n = length(x);
% confidence level
oneminusalpha = input('conf. level = ');
% significance level
alpha = 1 - oneminusalpha;
% population standard deviation
sigma = 5;
% sample mean
samp_m = mean(x);
fprintf('\n Problem 1.\n')
% fprintf('the sample mean is: %4.3f\n',samp_m)
% fprintf('the standard error is: %4.3f\n',stand_er)
% limits of the confidence interval

% a) Sigma known
m1 = mean(x) + norminv(alpha/2) * sigma/sqrt(n); %or m1=mean(x)-norminv(1-alpha/2)*sigma/sqrt(n); 
m2 = mean(x) - norminv(alpha/2) * sigma/sqrt(n);

fprintf('a) the confidence interval for the mean  (sigma known) is: (m1, m2) = (%4.3f, %4.3f)\n',m1, m2)

% b) Sigma not known
samp_std = std(x); % we use the sample std. dev.

% limits of the confidence interval
m1b = mean(x) + tinv(alpha/2, n - 1) * samp_std/sqrt(n);
m2b = mean(x) - tinv(alpha/2, n - 1) * samp_std/sqrt(n);

fprintf('b) the confidence interval for the mean (sigma unknown) is: (m1b, m2b) = (%4.3f ,%4.3f)\n',m1b, m2b)

% c)
v = var(x)
q1 = chi2inv(1 - alpha/2, n - 1)
q2 = chi2inv(alpha/2, n - 1) % here we need BOTH quantiles, there's no more symmetry
v1 = (n - 1) * v/q1
v2 = (n - 1) * v/q2
s1 = sqrt(v1); s2 = sqrt(v2);

fprintf('c) conf. interval for variance (v1, v2) = (%4.3f, %4.3f)\n', v1, v2)
fprintf('c) conf. interval for st. deviation (s1, s2) = (%4.3f, %4.3f)\n\n', s1, s2)