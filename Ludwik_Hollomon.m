clear all
close all
clc

%% unit Mpa For Abaqus input
epsilong_ln_pl = linspace(0,0.3,50);
abaqus_input=[];
for d = 0.3:0.05:0.5
    for sigma_y= 200:25:450
        for K = 600:150:1650
            for n = 0.1:0.05:0.5
                sigma_true = sigma_y + K*epsilong_ln_pl.^(n);
                abaqus = [sigma_true',epsilong_ln_pl'];
                abaqus_input = [abaqus_input,abaqus];
            end
        end
    end
end
%%
a = length(abaqus_input);
non = linspace(0,0,a);
abaqus_input = [non;abaqus_input];
writematrix(abaqus_input,'e:/ABAQUS/double hole/Abaqussnew.csv')

%% For ANN output              

ANN_output=[];
for d = 0.3:0.05:0.5
    for sigma_y= 200:25:450
        for K = 600:150:1650
            for n = 0.1:0.05:0.5
                temp_ANN = [sigma_y K n];
                ANN_output = [ANN_output;temp_ANN];
            end
        end
    end
end

%%

save('ANN_output.mat','ANN_output')




