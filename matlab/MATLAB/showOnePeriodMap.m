function showOnePeriodMap(one_period_map)
fig = figure;
fig.Position = [1 49 1536 742];
for j=1:8
    t = j*2500;
    this_period = reshape(one_period_map(:,:,t),[7,7]);
    subplot(2,4,j)
    heatmap(this_period)
    title(num2str(t));
    pause(0.05)
end
end
