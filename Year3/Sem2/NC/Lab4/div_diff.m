function d_F=div_diff(x,f)
%x=[x_1,..,x_n]; f=[f_1,...,f_n]



if length(x)==2
d_F=(f(2)-f(1))/(x(2)-x(1));
end
if length(x)>2
d_F=(div_diff(x(2:length(x)),f(2:length(x)))-div_diff(x(1:length(x)-1),f(1:length(x)-1)))/(x(length(x))-x(1));
end
end