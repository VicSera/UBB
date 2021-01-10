function out = my_first_function(in)
  out = NaN;
  if in ~= 1
    return
  else
    printf("Hello world!");
    out = 1;
  endif
endfunction
