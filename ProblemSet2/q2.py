import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np

# Import the data
data = np.loadtxt('229614158_PDCSAP_SC6.txt', delimiter=',', skiprows=1)
time = data[:,0]
flux = data[:,1]

# Cut down the data to the interesting region
idx1 = np.argmax(flux)
idx2 = sum(time<1707)
new_time = time[idx1:idx2]
new_flux = flux[idx1:idx2]

def model_derivs(pars, x):
    A = pars[0]
    B = pars[1]
    C = pars[2]
    D = pars[3]
    expvec = np.exp(-B*(x-C))
    fun = A*expvec + D
    dA = expvec
    dB = (C-x)*A*expvec
    dC = B*A*expvec
    dD = 1.0
    derivs = np.zeros([len(x), len(pars)])
    derivs[:,0] = dA
    derivs[:,1] = dB
    derivs[:,2] = dC
    derivs[:,3] = dD
    return fun, derivs

x = new_time
y = new_flux
n = 5
pars = np.asarray([1.5, 80, 1706.5, 1])
chi_old = 0

all_fun = np.zeros([len(x), n+1])

# plt.plot(x,y,'*')
# plt.pause(1)
for i in range(1,n+1):
    fun, derivs = model_derivs(pars, x)
    all_fun[:,i] = fun
    resid = y-fun
    chi_new = np.sum(resid**2)
    grad = 2*np.dot(derivs.transpose(), resid)
    curve = 2*np.dot(derivs.transpose(), derivs)
    pars = pars + np.dot(np.linalg.inv(curve), grad)
    print('Change in chi-squared is '+repr(chi_new-chi_old))
#     plt.plot(x, fun)
#     plt.pause(1)
# plt.show()


xdata = new_time
ydata = all_fun[:,0]

fig, ax = plt.subplots()
ax.plot(xdata, ydata, '*')
line, = ax.plot([], [])

def update(i):        
    ydata = all_fun[:,i]
    line.set_ydata(ydata)

ani= matplotlib.animation.FuncAnimation(plt.gcf(), update, frames=len(fun),
                                       interval=10, repeat=False)

plt.show()



# np.random.seed(19680801)
# data = np.random.random((50, 50, 50))

# fig, ax = plt.subplots()

# for i in range(len(data)):
#     ax.cla()
#     ax.imshow(data[i])
#     ax.set_title("frame {}".format(i))
#     # Note that using time.sleep does *not* work here!
#     plt.pause(0.1)