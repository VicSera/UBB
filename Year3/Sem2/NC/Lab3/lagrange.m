function [res] = lagrange(x0, x, y)
  w = ones(1, length(x));

  for i = 1:length(x)
    for j = 1:length(x)
      if i != j
        w(i) = w(i) / (x(i) - x(j)); 
      endif
    endfor
  endfor

  numerator = zeros(1, length(x0));
  denominator = zeros(1, length(x0));

  for j = 1:length(x)
    numerator = numerator + (w(j) * y(j)) ./ (x0 - x(j));
    denominator = denominator + w(j) ./ (x0 - x(j));
  endfor

  res = numerator ./ denominator;
endfunction