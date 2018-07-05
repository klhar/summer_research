import matplotlib.pyplot as plt
import numpy as np
a = [1.07]*7+[1]*93+[0.99]*300
zero=[0]*len(a)
Freq = []
def F(t):
    if len(Freq) > t:
        return Freq[t]
    
    return a[t] * F(t-1)

Dep = []
def D(t, gamma):
    D_t = 0
    if t == 0:
        return gamma**1 * (1 - gamma) * Freq[0]

    for i in range (0, t):
        D_t += gamma**(t-i-1) * (1 - gamma)/(1-gamma**t) * F(i)
    
    return D_t

Withdrawal = []
def W(t, gamma_1, gamma_2):
    return D(t, gamma_1) - D(t, gamma_2)


#constants
gamma_1 = 0.95
gamma_2 = 0.1

#initial values
    #let initial frequency value be 10
Freq.append(10)
Dep.append(D(0, gamma_1))
Withdrawal.append(W(0, gamma_1, gamma_2))

for timestep in range(1, len(a)):
    currF = F(timestep)
    Freq.append(currF)

    currD = D(timestep, gamma_1)
    Dep.append(currD)

    currW = W(timestep, gamma_1, gamma_2)
    Withdrawal.append(currW)

print(Freq)
print("\n")
print(Dep)
print("\n")
print(Withdrawal)
axisT = np.linspace(0, len(a)-1, len(a))
plt.plot(axisT, Freq, 'green')
plt.plot(axisT, Dep, 'red')
plt.plot(axisT, Withdrawal, 'orange')
plt.plot(axisT, zero, 'black')
plt.xlabel("Time (days)")
plt.show()

