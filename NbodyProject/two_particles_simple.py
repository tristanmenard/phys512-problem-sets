import numpy as np
import matplotlib.pyplot as plt
plt.ion()

# Start with 2 particles in a circular orbit
x0 = 0; y0 = 0; vx0 = 0; vy0 = 0.5
x1 = 1; y1 = 0; vx1 = 0; vy1 = -0.5

# Take G and m equal to 1
# Give time steps
dt = 0.01
tmax = 5

for t in np.arange(0, tmax, dt):
	dx = x0 - x1
	dy = y0 - y1
	rsquare = dx**2 + dy**2
	r = np.sqrt(rsquare)
	r3 = r**3
	# Calculate the x and y force components
	fx0 = -dx/r3 # r/r^3
	fy0 = -dy/r3
	# Forces on particle 1 must be opposite of particle 0
	fx1 = -fx0
	fy1 = -fy0
	# Update particle positions
	x0 = x0 + dt*vx0
	y0 = y0 + dt*vy0
	vx0 = vx0 + dt*fx0
	vy0 = vy0 + dt*fy0

	x1 = x1 + dt*vx1
	y1 = y1 + dt*vy1
	vx1 = vx1 + dt*fx1
	vy1 = vy1 + dt*fy1

	plt.plot(x0, y0, 'rx')
	plt.plot(x1, y1, 'b*')
	plt.ylim(-1.5,1.5)
	plt.xlim(-1,2)
	plt.pause(0.01)
	pot = -1.0/r # potential
	kin = 0.5*(vx0**2 + vy0**2 + vx1**2 + vy1**2) # kinetic energy
	print('kin and pot are ', kin, pot, pot + kin)