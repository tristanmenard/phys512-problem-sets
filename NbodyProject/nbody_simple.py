import numpy as np
import matplotlib.pyplot as plt
import time

class particles:
	def __init__(self, m=1.0, npart=1000, soft=0.01, G=1.0, dt=0.1):
		self.opts = {}
		self.opts['soft'] = soft
		self.opts['n'] = npart
		self.opts['G'] = G
		self.opts['dt'] = dt

		# Generate npart particles in 2 dimensions (gaussian distribution)
		# Each particle has (x,y) coordinates, (vx, vy) velocities, and mass m
		# Particles start with zero velocity (vx = vy = 0)
		self.x = np.random.randn(self.opts['n'])
		self.y = np.random.randn(self.opts['n'])
		self.m = m*np.ones(self.opts.['n'])
		self.vx = 0*self.x
		self.vy = self.vx.copy()

	def get_forces(self):
		# Initialize forces
		self.fx = np.zeros(self.opts['n'])
		self.fy = 0*self.fx
		pot = 0

		for i in range(0,self.opts['n']):
			dx = self.x[i] - self.x
			dy = self.y[i] - self.y
			rsqr = dx**2 + dy**2
			soft = self.opts['soft']**2
			rsqr[rsqr < soft] = soft
			rsqr = rsqr + self.opts['soft']**2
			r = np.sqrt(rsqr)
			r3 = 1.0/(r*rsqr)
			self.fx[i] = -np.sum(self.m*dx*r3)*self.opts['G']





