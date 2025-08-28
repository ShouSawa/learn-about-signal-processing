import pyperclip
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 10000
    mu = 0 # 平均値
    sigma = 1 # 標準偏差
    X1 = np.random.normal(mu, sigma, size=N)

    X2 = np.random.rand(N)

    s = "No.\t正規乱数\t一様乱数\n"

    for i in range(10000):
        s += str(i) + "\t" + str(X1[i]) + "\t" + str(X2[i]) + "\n"

    #print(s)
    pyperclip.copy(s)

    fig, ax = plt.subplots(1, 2, figsize=(9, 4))
    ax[0].hist(X1, bins=100)
    ax[1].hist(X2, bins=100)
    ax[0].set_title("Normal Rand Histogram")
    ax[1].set_title("Uniform Rand Histogram")
    plt.show()