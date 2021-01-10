x = [7, 7, 4, 5, 9, 9,...
     4, 12, 8, 1, 8, 7,...
     3, 13, 2, 1, 17, 7,...
     12, 5, 6, 2, 1, 13,...
     14, 10, 2, 4, 9, 11,...
     3, 5, 12, 6, 10, 7];
     
meanX = mean(x);
lengthX = length(x)
     
sigma = 5;
significanceLevel = 0.05;

m0 = 9
# H0: x = 9, or, the average computer can store at least 9 hundreds of thousands of files (9 is good enough)
# H1: x < 9, or, the average computer cannot store 9 hundreds of thousands of files

# a)
fprintf('a) FOR ALPHA = 0.05\n');
[H, P, CI, zstat] = ztest(x, m0, sigma, "alpha", significanceLevel, "tail", "left");

z = norminv(significanceLevel);
RR = [-inf, z];
if H == 1
   fprintf('The alternate hypothesis was accepted\n');
else
   fprintf('The alternate hypothesis was rejected\n');
end   
fprintf('CI: (%4.4f,%4.4f)\n', CI)
fprintf('RR: (%4.4f, %4.4f)\n', RR)
fprintf('z: %4.4f\n', zstat)
fprintf('P-value: %4.4f\n\n', P)

fprintf('a) FOR ALPHA = 0.01\n');
significanceLevel = 0.01;
[H, P, CI, zstat] = ztest(x, m0, sigma, "alpha", significanceLevel, "tail", "left");

z = norminv(significanceLevel);
RR = [-inf, z];
if H == 1
   fprintf('The alternate hypothesis was accepted\n');
else
   fprintf('The alternate hypothesis was rejected\n');
end
fprintf('CI: (%4.4f,%4.4f)\n', CI)
fprintf('RR: (%4.4f, %4.4f)\n', RR)
fprintf('z: %4.4f\n', zstat)
fprintf('P-value: %4.4f\n\n', P)

# b)
fprintf('b) FOR ALPHA = 0.05\n');
significanceLevel = 0.05;
m0 = 5.5;

[H, P, CI, stats] = ttest(x, m0, "alpha", significanceLevel, "tail", "right");

t = tinv(1 - significanceLevel, lengthX - 1);
RR = [t, inf];
if H == 1
   fprintf('The alternate hypothesis was accepted\n');
else
   fprintf('The alternate hypothesis was rejected\n');
end   
fprintf('CI: (%4.4f,%4.4f)\n', CI)
fprintf('RR: (%4.4f, %4.4f)\n', RR)
fprintf('z: %4.4f\n', stats.tstat)
fprintf('P-value: %4.4f\n\n', P)