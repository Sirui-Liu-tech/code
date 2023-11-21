function showNormMap(one_period_map)
norm_map = zeros(size(one_period_map,1),size(one_period_map,2));
for i=1:size(one_period_map,1)
    for j=1:size(one_period_map,2)
        norm_map(i,j) = norm(reshape(one_period_map(i,j,:),[size(one_period_map,3),1]));
    end
end
heatmap(norm_map)
end

