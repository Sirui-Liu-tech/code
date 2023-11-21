% 生成滤波器列表，包括带阻、高通和低通滤波器。
% 使用 butter 滤波器，取同一阶数。
% 输入：
%   Fs: 整数。采样率。默认值: 20000
%   N: 整数。滤波器的阶数，应为2的倍数。默认值：4
%   bsFcs: 二维数组，列数应为2。每行两个元素表示带阻滤波器的左、右截止频率。
%       默认值：[48 52;98 102;148 152]
%   hpFcs: 一维数组。每个元素表示高通滤波器的截止频率。默认值：0.1
%   lpFcs: 一维数组。每个元素表示低通滤波器的截止频率。默认值：30
% 输出：
%   filters: 一维元胞数组，每个元素是一个 Filter Object，可以通过调用函数 filter 来对数据进行滤波。
% 注意：
%   1. 需要安装 Signal Processing Toolbox 以使用 design 函数。
%   2. butter 滤波器会使滤波后数据产生相移。
%      可以对滤波后的数据倒序后进行同样的滤波后再倒序以抵消这种相移。
%   3. 所有截止频率应小于Fs/2。
%      若截止频率大于Fs/2, design 函数会报错；
%      若截止频率等于Fs/2, 滤波后会得到 NaN.
%   4. 信号通过低通滤波器会产生 Gibbs 现象，即信号发生指数衰减的振荡。
%      未来需要针对此问题对低通滤波器进行改进。

function filters = getFilters(Fs,N,bsFcs,hpFcs,lpFcs)
    arguments % 默认参数
        Fs = 20000;
        N = 4;
        bsFcs = [48 52;98 102;148 152];
        hpFcs = 0.1;
        lpFcs = 30;
    end

    filters = cell(0);

    for i=1:size(bsFcs,1)
        Fc1 = bsFcs(i,1);
        Fc2 = bsFcs(i,2);
        bsFilter = design(fdesign.bandstop('N,F3dB1,F3dB2', N, Fc1, Fc2, Fs), 'butter');
        filters{end+1} = bsFilter;
    end

    for hpFc = hpFcs
        hpFilter = design(fdesign.highpass('N,F3dB', N, hpFc, Fs), 'butter');
        filters{end+1} = hpFilter;
    end

    for lpFc = lpFcs
        lpFilter = design(fdesign.lowpass('N,F3dB', N, lpFc, Fs), 'butter');
        filters{end+1} = lpFilter;
    end

end
