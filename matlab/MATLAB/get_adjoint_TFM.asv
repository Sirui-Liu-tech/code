function get_adjoint_TFM(TF_coefs,top_dir)
    for k=1:size(TF_coefs,1)
        for ul = [1 2 4 5] % ul ? upper left
            pos = [ul ul+1 ul+3 ul+4];
            coefs = TF_coefs(k,pos,:,:);
            coefs = reshape(coefs,[4,320,320]);
            TFM = permute(coefs,[2,3,1]);    
            matname = [top_dir,'\',char(sprintf("TFMs0/%.0f-%.0f.mat",k,ul))];
            save(matname,"TFM");
        end
    end
end




