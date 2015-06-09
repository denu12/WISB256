import numpy
from scipy.integrate import odeint

class Lorentz:
	def __init__(self, start, sigma = 10, rho = 28, beta = 8/3)
		self.start = start
		self.sigma = sigma
		self.rho = rho
		self.beta = beta
		
	def function(self, parameters, t0):
		x = parameters[0]
		y = parameters[1]
		z = parameters[2]
		
		x_dot = self.sigma * (y - x)
		y_dot = self.rho * x - y - x * z
		z_dot = x  y-self.beta*z
		return [x_dot, y_dot, z_dot]
	
	def solve(self, T, dt)
		time = numpy.linspace(0, T, T/dt)
		result = odeint(self.function, self.start, t)
		return result