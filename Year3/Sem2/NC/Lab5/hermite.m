function res = hermite(p,x,y,df)
  res = y(1);
  x = [x;x](:)';
  y = [y;y](:)';
  df = [df;df](:)';
  
  n = length(x);
  
  
  
  for i = 2 : n
    partial_res = div_diff(x(1:i), y(1:i), df(1:i));
    for j = 1 : i - 1
      partial_res *= (p - x(j));
    endfor
    res += partial_res;
  endfor
endfunction




