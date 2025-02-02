import numpy as np

def solver(I, a, T, dt, theta):
    """Solve u'=-a*u, u(0)=I, for t in (0,T] with steps of dt."""
    Nt = int(T/dt)            # no of time intervals
    T = Nt*dt                 # adjust T to fit time step dt
    u = np.zeros(Nt+1)           # array of u[n] values
    t = np.linspace(0, T, Nt+1)  # time mesh

    u[0] = I                  # assign initial condition
    for n in range(0, Nt):    # n=0,1,...,Nt-1
        u[n+1] = (1 - (1-theta)*a*dt)/(1 + theta*dt*a)*u[n]
    return u, t

def u_exact(t, I, a):
    return I*np.exp(-a*t)

import matplotlib.pyplot as plt

def plot_numerical_and_exact(theta, I, a, T, dt):
    """Compare the numerical and exact solution in a plot."""
    u, t = solver(I=I, a=a, T=T, dt=dt, theta=theta)

    t_e = np.linspace(0, T, 1001)        # fine mesh for u_e
    u_e = u_exact(t_e, I, a)

    plt.plot(t,   u,   'r--o',            # red dashes w/circles
         t_e, u_e, 'b-')              # blue line for exact sol.
    plt.legend(['numerical', 'exact'])
    plt.xlabel('t')
    plt.ylabel('u')
    plt.title('theta=%g, dt=%g' % (theta, dt))
    #plt.savefig('plot_%s_%g.png' % (theta, dt))

def test_solver_three_steps():
    """Compare three steps with known manual computations."""
    theta = 0.8; a = 2; I = 0.1; dt = 0.8
    u_by_hand = np.array([I,
                       0.0298245614035,
                       0.00889504462912,
                       0.00265290804728])

    Nt = 3  # number of time steps
    u, t = solver(I=I, a=a, T=Nt*dt, dt=dt, theta=theta)

    tol = 1E-12  # tolerance for comparing floats
    diff = abs(u - u_by_hand).max()
    success = diff < tol
    assert success

if __name__ == "__main__":
    a = -1
    N = 10
    dts = [0.6, 0.9, 1.1, 1.5]
   
    for dt in dts:
        plot_numerical_and_exact(0, 1, a, N*dt, dt)
        plot_numerical_and_exact(0.5, 1, a, N*dt, dt)
        plot_numerical_and_exact(1, 1, a, N*dt, dt)
        plt.show()
    

    def amp(theta, a, dt, c):
        g = (1-(1-theta)*a*dt)/(1+theta*a*dt)
        plt.axhline(g, label = f'theta = {theta}', color = c)

    thetas = [0, 0.5, 1]
    colours = ["r", "b", "g"]
    index = 0
    for theta in thetas:
        amp(theta, a, 0.1, colours[index])
        index += 1
    plt.axhline(a, label = f'a = {a}', color = "k")
    plt.legend()
    plt.show()
    