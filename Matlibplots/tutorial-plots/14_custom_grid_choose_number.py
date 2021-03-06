import numpy
import pylab

t = numpy.arange(0.0, 1.0+0.1, 0.01)
s = numpy.cos(2*2*numpy.pi*t)

pylab.plot(t,s)
pylab.grid(True)
pylab.xticks([i/10.0 for i in range(0,22)])

pylab.show()