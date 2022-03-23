function res = newton(p,x,y)
  res = y(1);
  n = length(x);
  for i = 2 : n
    partial_res = div_diff(x(1:i), y(1:i));
    for j = 1 : i - 1
      partial_res *= (p - x(j));
    endfor
    res += partial_res;
  endfor
endfunction




