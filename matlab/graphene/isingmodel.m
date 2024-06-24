%matlab code
clear;clc;
n=10000;                       %马尔可夫链长度1万
ns=20;                          %20*20的格点 
beta_mc=(0.1:0.01:0.4);         %温度从10到2.5,链长1万，样品长5万
%T_mc=(2.1:0.01:2.4);          %第三批模拟温度设定，临界温度附近取点更密集，还要调整n=50000
%beta_mc=1./T_mc;
tic;                               %计时用，n=10000时，通常需要跑一分多钟
for jj=1:1:size(beta_mc,2)
X=sign(rand(ns,ns));        %所有格点方向一致，相当于从0度开始升温
%马尔可夫链长度为5万次
for j=1:1:n
    %随机选取一个格点，行列存储在index[1,2]
    index=unidrnd(ns,1,2);      
    % 利用周期性边界条件，分别计算格点上下左右四个点行列坐标
    tmp1=rem(index(1),ns)+1;tmp2=rem(index(1)+1,ns)+1;tmp3=rem(index(1)-1,ns)+1;
    tmp4=rem(index(2),ns)+1;tmp5=rem(index(2)+1,ns)+1;tmp6=rem(index(2)-1,ns)+1;
    % 计算改变格点方向后的能量变化
    cen=X(tmp1,tmp4);right=X(tmp1,tmp5);left=X(tmp1,tmp6);
    up= X(tmp2,tmp4);down= X(tmp3,tmp4);
    deE=2*cen*(right+left+up+down);
    % 判断是否改变格点
    if rand<exp(-deE*beta_mc(jj))
        X(tmp1,tmp4)=-X(tmp1,tmp4);
    end
end    

% 取样5万次，平衡时同样需要判断是否改变格点
for j=1:1:5*n
    index=unidrnd(ns,1,2);
    % 利用周期性边界条件，分别计算格点上下左右四个点行列坐标
    tmp1=rem(index(1),ns)+1;tmp2=rem(index(1)+1,ns)+1;tmp3=rem(index(1)-1,ns)+1;
    tmp4=rem(index(2),ns)+1;tmp5=rem(index(2)+1,ns)+1;tmp6=rem(index(2)-1,ns)+1;
    % 计算改变格点方向后的能量变化
    cen=X(tmp1,tmp4);right=X(tmp1,tmp5);left=X(tmp1,tmp6);
    up= X(tmp2,tmp4);down= X(tmp3,tmp4);
    deE=2*cen*(right+left+up+down);
    % 判断是否改变格点
    if rand<exp(-deE*beta_mc(jj))
        X(tmp1,tmp4)=-X(tmp1,tmp4);
    end
    %计算一种特定分布时的平均磁化率
    m(j)=abs(mean(mean(X)));  
	%计算一种特定分布时的平均能量
    Xt1=X;Xt1(1,:)=[];Xt1=[Xt1; X(1,:)];
    Xt2=X;Xt2(:,1)=[];Xt2=[Xt2, X(:,1)];
    e(j)=-mean(mean(X.*Xt1+X.*Xt2));
end
% 特定温度下的统计量
m_bar(jj)=mean(m);   
e_bar(jj)=mean(e);
cv_bar(jj)=beta_mc(jj)^2*ns^2*std(e)^2;
end
toc;
% 作图观察
figure(1);
plot(1./beta_mc,m_bar,'ko');
figure(2);
plot(1./beta_mc,e_bar,'ko');
figure(3);
plot(1./beta_mc,cv_bar,'ro');
