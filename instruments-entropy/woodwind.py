from cProfile import label
import audio2numpy as a2n
import matplotlib.pyplot as plt
import numpy as np
import math

def entropy(p, b):
    e=0
    for i in range(len(p)):
        if p[i]!=0 and p[i]<1:
            e-=(p[i]*math.log(p[i], b))
    return e

mp3 = []
mp3_1, sr1 = a2n.audio_from_file("bass-clarinetA3.mp3")
mp3_2, sr2 = a2n.audio_from_file("bassoonA3.mp3")
mp3_3, sr3 = a2n.audio_from_file("cor-anglaisA3.mp3")
mp3_4, sr4 = a2n.audio_from_file("saxophoneA3.mp3")
mp3.append(mp3_1)
mp3.append(mp3_2)
mp3.append(mp3_3)
mp3.append(mp3_4)

e = []
for i in range(len(mp3)):
    samples = len(mp3[i])

    hist, bin = np.histogram(mp3[i], bins=samples, density=0)
    p = np.zeros(samples)
    for i in range(samples):
        p[i] = hist[i]/samples
    e.append(entropy(p, samples))

fig, axs = plt.subplots(2, 2)
y = [0, 0, 1, 1]
x = [0, 1, 0, 1]
instrumento = ["Bass Clarinet", "Bassoon", "Cor Anglais", "Saxophone"]
for i in range(len(mp3)):
    t = np.linspace(0, 1, len(mp3[i]))
    axs[y[i], x[i]].plot(t, mp3[i])
    axs[y[i], x[i]].legend(["Entropia = {0:.6f}".format(e[i])], fontsize="25")
    axs[y[i], x[i]].set_title(instrumento[i])
plt.show()
