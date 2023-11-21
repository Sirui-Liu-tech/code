% 将所有channel的信号绘制到子图中，以助确认各通道信号的含义。
% 输入：
%   data: 二维数组，各列视为一个信号。
%   Fs: 采样率。
%   filters: 滤波器列表。默认值：[]
%   xLim: 1x2数组，整数。x 轴范围，单位：秒。
%       默认值：[1 floor(size(data,1)/Fs)-1], 即前后各删去 1s。
%   figAttr: 要更改的图窗属性，名称-值对的形式。
%       默认值：{"Position",get(0, 'ScreenSize')}
% 输出：
%   fig: 打印出的图窗。
% 注意：
%   get(0,"ScreenSize") 没有减去任务栏的部分，所以图窗会被部分挡住。
% 依赖函数：
%   filterTwice

function fig = plotAllChannels(data,Fs,filters,xLim,figAttr)
    arguments
        data;
        Fs;
        filters = [];
        xLim = [1 floor(size(data,1)/Fs)-1];
        figAttr = {"Position",get(0, 'ScreenSize')};
    end

    fig = figure;
    setFig(fig,figAttr)

    time = (1:size(data,1))/Fs;
    [r,c] = factorize(size(data,2));
    for i=1:size(data,2)
        channel = data(:,i);
        channel = filterTwice(channel,filters);
        subplot(r,c,i)
        plot(time,channel)
        xlabel("time (s)")
        xlim(xLim)
        title(sprintf("channel %d",i))
    end
end


function setFig(fig,varargin)
% 解析 varargin 参数并设置图窗。
% 输入：
%   fig: 要设置的图窗对象。
%   varargin: 名称-值对的形式。
% 无输出

    p = inputParser;
    
    % 添加参数名称-值对，其中值需要通过 eval 函数来计算
    for i = 1:2:length(varargin)
        paramName = varargin{i};
        paramValue = varargin{i + 1};
        % 使用 eval 函数计算参数值
        paramValueEval = eval(paramValue);
        % 添加参数到 inputParser
        addParameter(p, paramName, paramValueEval);
    end
    
    % 解析参数
    parse(p, varargin{:});
    % 获取解析后的参数
    parsedParams = p.Results;
    
    % 使用 set 函数设置 figure 对象属性
    fields = fieldnames(parsedParams);
    for i = 1:length(fields)
        paramName = fields{i};
        paramValue = parsedParams.(paramName);
        
        % 设置 figure 对象属性
        set(fig, paramName, paramValue);
    end
end


function [r,c] = factorize(n)
% 给定 n， 求因子 r x c >= n, 使得 r, c 尽量接近。
% n/r <= c <= n/r +1, 所以 r·c >= n
    r = ceil(sqrt(n));
    c = ceil(n/r);
end

