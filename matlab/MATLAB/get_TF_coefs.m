function TF_coefs = get_TF_coefs(one_period_map,Fs)
    ranges = [...
          0.01 0.99;...
    ];
    
    TF_coefs = zeros(size(ranges,1),9,320,320);

    for k=1:size(ranges,1)
        the_range = ranges(k,1)*Fs:ranges(k,2)*Fs;
        the_range = round(the_range);
        mcg = one_period_map(4:6,3:5,the_range);
        for i=1:3
            for j=1:3
                data = mcg(i,j,:);
                % 1 2 3 ?? D4-D2 
                % 4 5 6 ?? E4-E2 
                % 7 8 9 ?? F4-F2
                TF_coefs(k,3*(i-1)+j,:,:) = get_TFM(data);
            end
        end
    end
%     matname = [top_dir,'\TF_coefs.mat'];
%     save(matname,"TF_coefs");
end