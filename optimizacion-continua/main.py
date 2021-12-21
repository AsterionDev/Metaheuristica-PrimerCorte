import numpy as np
from hillclimbing import hillclimbing
#from sphere import sphere
from step import step
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # myStep = step (-5.0, 5.0)
    # input = np.arrange(1,4);
    # result = myStep.evaluate(input)
    # print (result)

    np.random.seed(40)
    myStep = step(-5.0, 5.0)
    myHC = hillclimbing(myStep, 2, 30, 0.5)
    [x, y] = myHC.evolve()

    # plotting
    plt.title("Convergence curve")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.plot(x, y, color="red")
    plt.show()
