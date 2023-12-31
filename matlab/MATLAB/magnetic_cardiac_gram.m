% 处理大鼠心磁-Quspin 探头的程序。
% version: 0.1.0
% 进行的操作：
%   读取数据、滤波、寻峰、按周期叠加、作图并保存

% 获取文件列表。
files = dir("rat\*.tdms");

Fs = 200;

% 设置滤波器。大鼠心率为480次/min，呼吸频率为80次/min
filters = getFilters(Fs, 4, [48 52], [2 2 1.5], [20 20]);

% 遍历每个文件
for i=1:numel(files)
    file = files(i);
    filename = file.name;
    file = convertTDMS(true,filename)
    fprintf("%d/%d: %s\n",i,numel(files),filename)

    % 读取 lvm 文件。
    data = readmatrix([file.folder,'\',file.name],"FileType","text","NumHeaderLines",7);
    data = data(:,2);
    % 滤波。
    data = filterTwice(data,filters);
    % 删去振荡部分。
    data = data(3*Fs:end-1*Fs);
    % 时间序列。
    time = (1:numel(data))/Fs;

    % 获取包络线。up, lo 分别是上、下包络。
    [up,lo] = envelope(data,500,'rms');
    % 寻峰。用包络线的幅度来代表峰的幅度
    meanProminence = mean(up-lo);
    [peaks,locs] = findpeaks(data,"MinPeakDistance",0.1*Fs,"MinPeakProminence",meanProminence);

    fig = figure;
    fig.Visible = "off";
    fig.Position = get(0,"ScreenSize");
    hold on;
      % 绘制信号及寻峰结果
    plot(time,data,"Color","black");
    plot(locs/Fs,peaks,"v")
    xlim([10 30])

    % 对信号按周期叠加。
    avgData = periodicAverage(data,locs,0.5*Fs,0.5*Fs);
    avgTime = (1:numel(avgData))/Fs;
    plot(avgTime,avgData,"Color","black");
    
    xlabel("time(s)")
    ylabel("magnetic filed (pT)");
    title(file.name,"Interpreter","none")

    % 将图打印到文件。
    print("-dpng","-r300",strjoin(["figs/rats/average/",strrep(file.name,".lvm",".png")]))
    close all;
end