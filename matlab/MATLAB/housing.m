%双摆
clear
clc
close all
%输入
N=2;%双摆
m=1;
l=1;
g=9.8;
Input=[N,m,l,g];
%初始条件和时间设置
y0=[pi/2;pi/2;0;0];%这里全部是弧度值。分别代表[摆1与垂面夹角，摆2与垂面夹角，摆1角动量，摆2角动量]
h=1e-2;
x0=0:h:20;
%代入到ODE求解器中
[y1,Output]=ODE_RK4_hyh(x0,h,y0,Input);

%提取出角度
tN=size(y1,2);
th1=y1(1,:);
th2=y1(2,:);

%计算出关节坐标
CX1_A=zeros(1,tN);
CX1_B=CX1_A+l*sin(th1);
CY1_A=zeros(1,tN);
CY1_B=CY1_A-l*cos(th1);

CX2_A=CX1_B;
CX2_B=CX2_A+l*sin(th2);
CY2_A=CY1_B;
CY2_B=CY2_A-l*cos(th2);

%绘图
n=1;
figure()
set(gcf,'position',[488   342   400   300])
for k=1:4:length(x0) %这里4步一显示时间帧
    clf
    xlim([-2,2])
    ylim([-2,2])
    hold on
    %绘制摆
    plot([CX1_A(k),CX1_B(k)],[CY1_A(k),CY1_B(k)],'color','k','LineWidth',1.5)
    plot([CX2_A(k),CX2_B(k)],[CY2_A(k),CY2_B(k)],'color','k','LineWidth',1.5)
    %绘制轨线
    if k>200
        n=n+1;
    end
    Nm=k-n+1;
    %轨迹1
    F_color=[1,0,0];
    F_color=F_color*0.6+[1,1,1]*0.4*0.999;
    cdata=[linspace(1,F_color(1),Nm+1)',linspace(1,F_color(2),Nm+1)',linspace(1,F_color(3),Nm+1)'];
    cdata=reshape(cdata,Nm+1,1,3);
    if k>3
        patch([CX1_B(n:k),NaN],[CY1_B(n:k),NaN],1:Nm+1,'EdgeColor','interp','Marker','none',...
          'MarkerFaceColor','flat','CData',cdata,'LineWidth',1.5);
    end
    %轨迹2
    F_color=[0,0,1];
    F_color=F_color*0.6+[1,1,1]*0.4*0.999;
    cdata=[linspace(1,F_color(1),Nm+1)',linspace(1,F_color(2),Nm+1)',linspace(1,F_color(3),Nm+1)'];
    cdata=reshape(cdata,Nm+1,1,3);
    if k>3
        patch([CX2_B(n:k),NaN],[CY2_B(n:k),NaN],1:Nm+1,'EdgeColor','interp','Marker','none',...
          'MarkerFaceColor','flat','CData',cdata,'LineWidth',1.5);
    end
    hold off
    pause(0.05)
    %可以在这里添加输出动图的程序
end

function [y,Output]=ODE_RK4_hyh(x,h,y0,Input)
%4阶RK方法
%h间隔为常数的算法
y=zeros(size(y0,1),size(x,2));
y(:,1)=y0;
for ii=1:length(x)-1
    yn=y(:,ii);
    xn=x(ii);
    K1=Fdydx(xn    ,yn       ,Input);
    K2=Fdydx(xn+h/2,yn+h/2*K1,Input);
    K3=Fdydx(xn+h/2,yn+h/2*K2,Input);
    K4=Fdydx(xn+h  ,yn+h*K3  ,Input);
    y(:,ii+1)=yn+h/6*(K1+2*K2+2*K3+K4);
end
Output=[];
end

function dydx=Fdydx(x,y,Input)
%将原方程整理为dy/dx=F(y,x)的形式
%输入Input整理
m=Input(2);
l=Input(3);
g=Input(4);
%输入
th1=y(1);%角度1
th2=y(2);%角度2
pth1=y(3);%角动量1
pth2=y(4);%角动量2
%利用拉格朗日法得到的方程
M=l^2*m*(-16 + 9*cos(th1 - th2)^2);
dth1 = -6*(2*pth1 - 3*pth2*cos(th1 - th2))/M; 
dth2 = -6*(8*pth2 - 3*pth1*cos(th1 - th2))/M;
dpth1=-0.5*l*m*(3*g*sin(th1)+dth1*dth2*l*sin(th1-th2));
dpth2=0.5*l*m*(dth1*dth2*l*sin(th1-th2)-g*sin(th2));
%整理输出
dydx=zeros(4,1);
dydx(1)=dth1;
dydx(2)=dth2;
dydx(3)=dpth1;
dydx(4)=dpth2;
end

