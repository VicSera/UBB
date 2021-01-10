% Lab #6, problem 1. 
% Problem 1.
% In a study of the size of various computer systems, the random variable
% $X$, the number of files stored (in hundreds of thousands), is considered. If they cannot store at 
% least 9, on average, they don't meet the efficiency standard
% and they have to be replaced. Past experience 
% indicates that sigma = 5. These data are obtained:
%  7  7  4  5  9  9
%  4 12  8  1  8  7
%  3 13  2  1 17  7
% 12  5  6  2  1 13
% 14 10  2  4  9 11
%  3  5 12  6 10  7
% a. Assuming that past experience indicates that sigma = 5, at the 5%
% significance level, does the data suggest that the standard is met? What about at 1%?
% b. Without the assumption on sigma, does the data suggest that on average, the nr
% of files exceeds 5.5? (same sign. level) 

alpha = input(' significance level alpha = ');

x = [7, 7, 4, 5, 9, 9, 4, 12, 8, 1, 8, 7, 3, 13, 2, 1, 17, 7,...
   12, 5, 6, 2, 1, 13, 14, 10, 2, 4, 9, 11, 3, 5, 12, 6, 10, 7];
n = length(x);

% a)
% The null hypothesis H0: mu = 9
% the alt. hypothesis H1: mu < 9. This is a left-tailed test for mu.

fprintf(' Part a: ')
fprintf('\n Left-tailed test for the mean (sigma known)\n')
sigma = 5;


% a)
m0 = input(' test value m0 = '); % m0=theta0
% m0 is in this case 9.

[H, P, CI, zstat] = ztest(x, m0, sigma,"alpha",alpha,"tail","left"); % -1 is for left-tailed, 1 for right,
                                                    % 0 for two-tailed (default)
% z1=norminv(1-alpha); for right-tailed test
z2 = norminv(alpha);
RR = [-inf, z2]; % rejection region for left-tailed test
fprintf('\n H is %d', H)
if H == 1 % result of the test, h = 0, if H0 is NOT rejected, h = 1, if H0 IS rejected
    fprintf('\n So the null hypothesis is rejected,\n') 
    fprintf('i.e. the data suggests that the standard IS NOT met.\n')
else
    fprintf('\n So the null hypothesis is not rejected,\n')
    fprintf('i.e. the data suggests that the standard IS met.\n')
end    
fprintf(' the confidence interval for mu is (%4.4f,%4.4f)\n', CI)
fprintf('the rejection region is (%4.4f, %4.4f)\n', RR)
fprintf('the value of the test statistic z is %4.4f\n', zstat)
fprintf('the P-value of the test is %4.4f\n\n', P)

% b)
% The null hypothesis H0: mu = 5.5
% the alternative hypothesis H1: mu > 5.5. This is a right-tailed test for mu.

fprintf('\n Part b: ')
fprintf('\n Right-tailed test for the mean (sigma unknown)\n')

m0b = input(' test value m0 = ');
% m0 is in this case 5.5.
[H, P, CI, stats] = ttest(x,m0b,"alpha",alpha,"tail","right"); % 1, for right-tailed

t1 = tinv(1 - alpha, n-1); % quantile for right-tailed test
RR = [t1, Inf]; % rejection region for right-tailed test
fprintf('\n H is %d', H)
if H==1
    fprintf('\n So the null hypothesis is rejected,\n') 
    fprintf('i.e. the data suggests that the average exceeds 5.5.\n')
else
    fprintf('\n So the null hypothesis is not rejected,\n')
    fprintf('i.e. the data suggests that the average DOES NOT exceed 5.5.\n')
end    
fprintf(' the confidence interval for mu is (%4.4f,%4.4f)\n', CI)
fprintf('the rejection region is (%4.4f,%4.4f)\n', RR)
fprintf('the value of the test statistic t is %4.4f\n', stats.tstat)
fprintf('the P-value of the test is %4.4f\n\n', P)

