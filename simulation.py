import random as rnd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

p_show = lambda x: rnd.uniform(0.907, 0.968)


def show_up(p):
    if rnd.random() <= p:
        return True
    return False


def flight(num_tix, tix_price, comp_cost, capacity):
    p = p_show(0)
    shows = sum([1 for x in range(num_tix) if show_up(p)])
    if shows <= capacity:
        return tix_price * shows
    else:
        denials = shows - capacity
        return tix_price * shows - comp_cost * denials


def run_sim(ticket_price, capacity):
    x_vals = []
    y_vals = []
    for i in ticket_price:
        comp_cost = 4 * i
        for j in capacity:
            num_tix = [j + k * 5 for k in range(8)]
            num_tix, res = sims_10000(i, comp_cost, j, num_tix)
            x_vals.append(num_tix + [i]), y_vals.append(res)
            # print(x_vals), print(j)
    print(x_vals)
    return x_vals, y_vals


def sims_10000(ticket_price, comp_cost, capacity, num_tix):
    res = [[], [], [], [], [], [], [], []]
    for i in range(len(num_tix)):
        for _ in range(10000):
            res[i].append(flight(num_tix[i], ticket_price, comp_cost, capacity))
    res = [sum(y) / len(y) for y in res]
    return num_tix, res


def plot_results(x_vals, y_vals):
    for i in range(len(x_vals)):
        x, y = x_vals[i], y_vals[i]
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x[:-1], y)
        ax.set(title="Simulation where capacity = %d and ticket price = %d" % (x[0], x[-1]),
               xlabel = 'Number of tickets sold',
               ylabel = 'Expected revenue in $')
        ax.fill_between(x[:-1], 10000, y, alpha=0.5)
        ax.set_ylim([min(y) - 2000, max(y) + 2000])
        ax.set_xlim([min(x[:-1]), max(x[:-1])])
        plt.setp(ax.get_xticklabels(), rotation=45)
        plt.grid()
        plt.show()
        fig.savefig('filename%d.eps'%i, format='eps')


t = [100, 500, 1000]
c = [200, 500]

x, y = run_sim(t, c)
plot_results(x, y)
