import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('valoresobtidos.csv')

coltempo = df.tempo.values
coltempo2 = []

for x in range(0, 48):
    coltempo[x] = round(coltempo[x], 1)
    coltempo2.append(x)

x = coltempo[::1]
y = coltempo2[::1]

fig, ax = plt.subplots()

ax.plot(coltempo, color='red', zorder=0)

ax.scatter(y, x, zorder=5)
plt.xlabel("Número de fibonacci (N)")
plt.ylabel("Tempo necessário em segundos")

for i, txt in enumerate(x):
    ax.annotate(txt, (y[i], x[i] + i))
plt.show()
