import matplotlib.pyplot as plt
import numpy as np
import unittest

def  true_function(x):
    y = np.sin(np.pi * x * 0.8) * 10
    return y

x = np.arange(-1,1,0.01)#　-1≦x≦1の定義域
y = true_function(x)

plt.plot(x,y)
plt.savefig("ex1.1.png")
plt.show()


class testfunction(unittest.TestCase):
    def test_true_function(self):
        result = true_function(0)
        self.assertEquals(result,0)


if __name__ == '__main__':
    unittest.main()
    


