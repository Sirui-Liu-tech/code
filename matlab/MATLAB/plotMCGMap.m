function plotMCGMap(this_period)
for i=1:7
    for j=1:7
        subplot(7,7,7*(i-1)+j)
        plot(this_period)
        xticks([])
%         ylim([])
    end
end
end

