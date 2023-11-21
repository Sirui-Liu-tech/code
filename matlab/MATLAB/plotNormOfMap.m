function plotNormOfMap(one_period_map)
norms = zeros(size(one_period_map,3),1);
for j=1:size(one_period_map,3)
    this_period = one_period_map(:,:,j);
    norms(j) = norm(this_period);
end
plot(norms)
end

