
function one_period_map = get_one_period_map(top_dir,Fs)
    % ?????
    N = 4; % ????Butter???
    HdBs50 = design(fdesign.bandstop('N,F3dB1,F3dB2', N, 48, 51, Fs), 'butter');
    HdBs100 = design(fdesign.bandstop('N,F3dB1,F3dB2', N, 96, 104, Fs), 'butter');
    HdH = design(fdesign.highpass('N,F3dB', N, 1, Fs), 'butter');
    HdL = design(fdesign.lowpass('N,F3dB', N, 30, Fs), 'butter');
    Hdlist = [HdBs100,HdBs50,HdH,HdL];
    
    % ????????????
    strip_left = 12*Fs;
    strip_right = 1*Fs;
    
    % ?????
    period_left = 0.3*Fs;
    period_right = 0.7*Fs;
    
    % ??? map ?????????????A0-G6
    one_period_map = zeros(7,7,period_right+period_left+1);
    
%     fig = figure;
    
    files = dir([top_dir,'/','*.mat']);
    for jj=1:12
        figs(jj) = figure;    
        sgtitle([top_dir,' channel ',char(num2str(jj))])
        figs(jj).Visible = "off";
        figs(jj).Position = [1 -156 1536 731];
    end

    mkdir([top_dir,'/channels'])

    for i=1:numel(files)
        file = files(i);
        path = [file.folder,'/',file.name];
        fprintf("%d/%d: %s\n",i,numel(files),path)
        oriData = loadfile(path,1:12);

        for jj=3:12
%             fprintf("channel=%d\n",jj)
            data = oriData(jj,:);
            data = myfilt(data,Hdlist);
            data = data(strip_left:end-strip_right);

    %         ECG = data(12,:);
    %         MCG = data(8,:);
    % 
    %         ECG = myfilt(ECG,Hdlist);
    % 
    %         ECG = ECG(strip_left:end-strip_right);
    %         
    %         [~,locs] = findpeaks(ECG,"MinPeakDistance",0.5*Fs,"MinPeakProminence",0.5*1e-4);
    %         filtered_data = myfilt(MCG,Hdlist);
    %         filtered_data = filtered_data(strip_left:end-strip_right,:);
    %         one_period = periodicAverage(filtered_data,locs,period_left,period_right);
            [r,c] = code2pos(file.name);
    % 
    %         one_period_map(r,c,:) = one_period;
    % %         showNormMap(one_period_map)
            figure(figs(jj))
            subplot(7,7,7*(r-1)+c)
            plot(data)
            xticks([])
            yticks([])
            pause(0.1)
        end
    end

%     matname = [top_dir,'/one_period_map.mat'];
%     save(matname,"one_period_map");
for jj=3:12
    figure(figs(jj))
    print([top_dir,'/channels/channel-',char(num2str(jj)),'.png'],'-dpng')
end
close all;
end

