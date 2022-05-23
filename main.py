import matplotlib.pyplot as plt

b = 0.1
k = 0.05
n = 100

s = [0.99*n]
i = [0.01*n]
r = [0*n]

beta = b/n

def s_fun(t: int):
    return s[t] - beta * i[t] * s[t]

def i_fun(t: int):
    return i[t] + beta * i[t] * s[t] - k * i[t]

def r_fun(t: int):
    return r[t] + k * i[t]

def loop(limit_t: int):
    for t in range(limit_t-1):
        s.append(s_fun(t))
        i.append(i_fun(t))
        r.append(r_fun(t))

if __name__ == "__main__":
    t = int(input("Iterations:"))
    loop(t)
    print("s", s[-1])
    print("i", i[-1])
    print("r", r[-1])
    x_t = [i for i in range(t)]
    plt.plot(x_t, s)
    plt.plot(x_t, i)
    plt.plot(x_t, r)
    plt.show()