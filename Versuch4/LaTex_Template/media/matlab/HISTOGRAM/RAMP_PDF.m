%% Time specifications:
Fs = 5000;                   % samples per second
dt = 1/Fs;                   % seconds per sample
StopTime = 1;             % seconds
t = (0:dt:StopTime-dt)';     % seconds
%% Sine wave:
Fc = 1;                     % hertz
A= 3.5/2;
Vfs=3.3;
C=Vfs/2;
x = A*sawtooth(2*pi*Fc*t+1.6,0.5)+C;
% Plot the signal versus time:
figure1=figure;
plot(t,x,'Color',[0 0 0.6], 'LineWidth', 1.25);
hold on;
plot(t,Vfs,'--');
plot(t,0,'--');
xlabel('time (in s)');
ylabel('Amplitude A (in V)');
xlabel('time (in s)');
ylabel('Amplitude A (in V)');
%x,y limits
xlim([0 1]);
ylim([-0.2 3.5]);


% Create textbox
annotation(figure1,'textbox',...
    [0.810119047619048 0.51915796386249 0.0577380952380974 0.0333796940194715],...
    'String',{'ADC Vfs 3.3V'},...
    'HorizontalAlignment','right',...
    'FitBoxToText','off',...
    'LineStyle','none');
% Create doublearrow
annotation(figure1,'doublearrow',[0.869642857142857 0.870238095238095],...
    [0.878014989293362 0.154175588865096]);

filename='ramp_fkt_samples_5000';
print(figure1, '-depsc', filename);

%calc overdrive samples
for i=1:length(x);
    if x(i)>=Vfs
        x(i)=3.3;
    end
    if x(i) <= 0
        x(i)=0;
    end
end

filename='ramp_hist_samples_5000';
figure1=figure;

hist(x,64,figure1);
xlabel('dx');
ylabel('ni');
xlim([0 Vfs]);
%xlim([-0.1 3.4]);
%zoom xon;
%xlim([0 1]);
%ylim([-0.2 3.5]);

print(figure1, '-depsc', filename);
