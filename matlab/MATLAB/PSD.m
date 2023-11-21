% 计算功率谱密度。推导见 github@PKU-Biomagnetic-Group/MCG-data-process/documents/功率谱密度.md
% 输入：
%   X: 要计算功率谱密度的信号，每列视为一个信号。
%   Fs:采样率。
%   k: 滑动平均的阶数。
% 输出：
%   f: 频率，范围为 0~Fs/2.
%   P: 功率谱密度。

function [f,P] = PSD(X,Fs,k)

L = size(X,1);
right = ceil(L/2+1);
T = L/Fs;
P = zeros(right,size(X,2));

for i=1:size(X,2)
    x = X(:,i);
    y = fft(x);
    P(:,i) = abs(y(1:right))/sqrt(T);
    P(:,i) = movmean(P(:,i),k);
end
f = (0:right-1)/T;
