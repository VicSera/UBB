function d_F = div_diff(x,f,df)
%x=[x_1,..,x_n]; f=[f_1,...,f_n]
n = length(x);
  d_F = 0;

  if n==2
    numerator = f(2) - f(1);
    denominator = x(2) - x(1);
    if denominator == 0
      d_F = df(1);
    else
      d_F=numerator / denominator;
    endif
  endif
  if n>2
    left = div_diff(x(2:n),f(2:n),df(2:n));
    right = div_diff(x(1:n-1),f(1:n-1),df(1:n-1));
    numerator = left - right;
    denominator = (x(n)-x(1));
    if denominator == 0
      d_F = df(1);
    else
      d_F=numerator / denominator;
    endif
  endif
endfunction