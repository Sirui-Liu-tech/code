% 注释时间 2023/6/17 21:00
% 本文件读取 main.m 保存的 one_period_map.mat 文件
% 通过插值画出 map, 保存到 anime 文件夹下。

% clear
clc
Fs = 20000;
top_dir = 'raw\yx80000nT';
mkdir([top_dir,'\anime'])
% % one_period_map = load([top_dir,'\one_period_map.mat']).one_period_map;

fig = figure;
% fig.Visible = "off";
fig.Position = [100 200 600 500];
% 划分几个阶段及相应的磁场范围
% P波 0.01s-0.26s [-1.1 6.6]
% QRS波 0.27s-0.32s [-8.7 3.3]
% ST间期 0.33-0.54s
% T波 0.55-0.64s
% T波后 0.65-0.99

% 三列表示 起始 终点 间隔
ranges = [...
          0.01 0.22 0.01;...
          0.23 0.28 0.01;...
          0.285 0.31 0.001;...
          0.32 0.35 0.01;...
          0.36 0.52 0.01;...
          0.53 0.635 0.001;
          0.64 0.99 0.01;...
    ];
for i=1:size(ranges,1)
    the_range = ranges(i,1)*Fs:ranges(i,2)*Fs;
    the_range = round(the_range);
    max_value = max(one_period_map(:,:,the_range),[],"all");
    min_value = min(one_period_map(:,:,the_range),[],"all");
%     fprintf("%.1f %.1f\n",min_value,max_value)
    ranges(i,4:5) = [min_value,max_value];
end

for k=1:size(ranges,1)
    fprintf("k=%d\n",k)
    the_range = ranges(k,1)*Fs:ranges(k,3)*Fs:ranges(k,2)*Fs;
    for i=the_range
        instant_map = one_period_map(:,:,floor(i));
        instant_map = reshape(instant_map,7,7);
    
        interpData = interp2(instant_map, 3,"spline");
    
        h = heatmap(interpData,"GridVisible","off","Colormap",parula);
        caxis(ranges(k,4:5))
        XDisplayLabels = repmat("",49,1);
        for ij=0:6
            XDisplayLabels(45-7*ij) = num2str(ij);
        end
        YDisplayLabels = repmat("",49,1);
        for ij=1:7
            YDisplayLabels(7*ij-4) = char(ij+64);
        end
        h.XDisplayLabels = XDisplayLabels;
        h.YDisplayLabels = YDisplayLabels;
    
        title(sprintf("yx 80000nT %.3fs",i/Fs))
        pngname = strjoin([top_dir,'\anime\',sprintf("%.3f",i/Fs),'s.png'],"");
        fprintf("%s\n",pngname)
        print(pngname,'-dpng', '-r300')
    end
end
