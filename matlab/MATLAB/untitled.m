
digits(10)

m = 0
for i=1:10000
    m = ff(m)
end

disp(vpa(m))

function [f] = ff(x)
f = x - (x^3+x^2+15*x-10)/(3*x^2+2*x+15);
end
