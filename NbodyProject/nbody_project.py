import numpy as np
import matplotlib.pyplot as plt
import sys

class particles:
	def __init__(self, m=1.0, npart=1000, soft=0.01, G=1.0, dt=0.1, scale=1.0):
		self.opts = {}
		self.opts['n'] = npart
		self.opts['soft'] = soft
		self.opts['G'] = G
		self.opts['dt'] = dt

		# Generate n particles in 3 dimensions (gaussian distribution)
		self.x = np.random.randn(self.opts['n'])*scale
		self.y = np.random.randn(self.opts['n'])*scale
		self.z = np.random.randn(self.opts['n'])*scale
		# Each particles has some mass m
		self.m = m*np.ones(self.opts['n'])
		# Each particle starts at rest
		self.vx = 0*self.x
		self.vy = self.vx.copy()
		self.vz = self.vx.copy()

	def get_potential2D(self, grid=[-10,10,-10,10,1001]):
		self.xmin, self.xmax, self.ymin, self.ymax, self.npts = grid
		xx = np.linspace(self.xmin, self.xmax, self.npts)
		yy = np.linspace(self.ymin, self.ymax, self.npts)
		self.X, self.Y = np.meshgrid(xx, yy)
		pot = np.zeros([self.npts, self.npts])

		for i in range(0, self.opts['n']):
			r2 = (self.X-self.x[i])**2 + (self.Y-self.y[i])**2
			pot = pot - 0.5*self.opts['G']*self.m[i]/(r2+self.opts['soft']**2)**0.5
			sys.stdout.write('\r')
			j = (i+1)/self.opts['n']
			sys.stdout.write('[%-20s] %d%%' % ('|'*int(20*j), (j)*100))
			sys.stdout.flush()
		sys.stdout.write('\n')
		return pot

plt.ion()
test = particles(npart=1000, scale=10)
pot2d = test.get_potential2D(grid=[-100,100,-100,100,1001])

plt.contourf(test.X,test.Y,np.log10(-pot2d),100, cmap='cividis_r')
plt.colorbar()

