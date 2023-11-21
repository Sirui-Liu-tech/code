
function data = loadfile(path,cols)
    % ????????????
    data = zeros(12,1220000);
    oriData = load(path);
    for i=3:size(oriData,2)
        data(i) = oriData.ConvertedData.Data.MeasuredData(i).Data;
    end
    data = data(cols,:);
    %     ECG = data.ConvertedData.Data.MeasuredData(12).Data;

%     MCG= data.ConvertedData.Data.MeasuredData(8).Data;
%     ECG = data.ConvertedData.Data.MeasuredData(12).Data;
%     ECG = ECG-mean(ECG);
end


