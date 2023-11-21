% 将一个周期信号按给定峰位叠加并求平均，并跳过给定区间的信号。
% 若一段噪声较大的准周期信号（如MCG）无法直接确定每个周期的位置，
% 但已经通过其他方式（如对ECG寻峰）获得每个周期中同一标志点的位置（如QRS峰的位置），
% 则可以依靠这些标志点来对该信号叠加求平均。
% 若信号中的噪声包括持续时间较短、幅度较大的干扰（如忽然的抖动），
% 通过其他方式确定这些干扰持续的区间，在叠加求平均时可以跳过这些抖动的区间。

% 输入：
%   data: 二维数组，每一列视为一个信号。
%   anchorLocs: 一维数组，各元素应为整数且不超过data的长度，表示标志点的位置。
%   leftPoints: 整数，表示一个周期中标志点左侧的信号序列长度。
%   rightPoints: 整数，表示一个周期中标志点右侧的信号序列长度。
%   perturbIntervals: 二维数组，应为2列。每行的两个数表示一个异常信号持续的区间。默认值：[1 1]
% 输出：
%   若只有一个输出参数，则输出 avgData. 若有两个输出参数，则输出 avgData, numCycles.
%   avgData: 二维数组，列数与 data 的列数相同，行数等于 leftPoints + rightPoints + 1.
%       表示周期叠加后的信号。
%   numCycles: 整数，表示参与计算的周期数。
% 注意：
%   当标志点左侧、右侧距离边界或异常信号区间过近，不能完整截取一个周期时，这个标志点会被忽略。

function varargout = periodicAverage(data, anchorLocs, leftPoints, rightPoints,perturbIntervals)
    arguments
        data
        anchorLocs
        leftPoints
        rightPoints
        perturbIntervals = [ ];
    end

    anchorLocs = sort(anchorLocs);

    [n, m] = size(data);  
    numCycles = numel(anchorLocs); 
    
    avgData = zeros(leftPoints+rightPoints+1, m);

    for i = 1:numCycles
        left = anchorLocs(i)-leftPoints;
        right = anchorLocs(i)+rightPoints;
        if left<1 || right>n || isPerturb([left right],perturbIntervals)
            numCycles = numCycles - 1;
            continue
        end
            cycleData = data(left:right, :); 
            avgData = avgData + cycleData;
    end
    avgData = avgData / numCycles;

    if nargout==1
        varargout{1} = avgData;
    elseif nargout==2
        varargout{1} = avgData;
        varargout{2} = numCycles;
    end
end

function res = isPerturb(interval,perturbIntervals)
% 判断某个周期是否位于异常区间。
    res = false;
    for i=1:size(perturbIntervals,1)
        if perturbIntervals(i,1)<=interval(1) || interval(2)<=perturbIntervals(i,2)
            res = true;
            break
        end
    end
end
