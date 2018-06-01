import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

rate, data = scipy.io.wavfile.read('./Test_audio.wav')

#Reducing ndarray to single list
cleaned = data[:,0]

#list is 268599 items long

trigger_range= []
counter = 0
flag = True

print(max(cleaned))
#Captures the instances that the clap is heard
for i in range(len(cleaned)):
    if abs(cleaned[i]) >= 31770 and flag is True:
        counter+=1
        trigger_range.append([i,cleaned[i]])
        flag=False
    elif abs(cleaned[i]) < 31770:
        flag=True
    
print (counter)
print (trigger_range)

plt.plot(cleaned)
plt.ylabel("Amplitude") 
plt.xlabel("Time (samples)")
plt.title("Clap Sample")
plt.show()