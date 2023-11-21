% 进行两次滤波。在第一次滤波后将数据倒序，
% 进行同样的滤波处理，以消除滤波造成的相移。
% 第二次滤波结束后再对数据倒序以恢复原顺序。
% 输入：
%   data: 二维数组。每列视为一个信号序列。
%   filters: 一维元胞数组。元素为 Filter Object。该列表可以由函数 getFilters 得到。
% 输出：
%   data: 滤波后的数据。

function data = filterTwice(data,filters)
    for ft=filters
        data = filter(ft,data);
    end
    
    data = data(end:-1:1,:);

    for ft=filters
        data = filter(ft,data);
    end
    
    data = data(end:-1:1,:);
end

