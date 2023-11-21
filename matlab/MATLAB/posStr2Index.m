% 将形如 "A0","G1" 的字符转变为矩阵的行和列坐标。
% 其中 "A0" 转换为 (1,7), "G6" 转换为 (7,1).
% 输入：
%   positionString: 字符串或字符数组，长度为2，与正则表达式 "[A-G][0-6]" 匹配。
% 输出：
%   r. c: 转换的行和列。

function [r,c] = posStr2Index(positionString)
    positionString = char(positionString);
    r = double(positionString(1))-65+1;
    c = 7-str2double(positionString(2));
end
