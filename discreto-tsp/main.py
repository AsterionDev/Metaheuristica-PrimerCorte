from hillclimbing import hillclimbing
from tsp import tsp
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    maxRepetitions = 31
    maxIterations = 1000
    directory = 'discreto-tsp/problems/'
    myProblem = tsp(directory + 'ulysses16..txt')

    best = np.zeros(maxRepetitions, dtype=float)
    avgX = np.arange(0, maxIterations)
    avgY = np.zeros(maxIterations, float)
    for i in range(maxRepetitions):
        np.random.seed(i)
        myHC = hillclimbing(myProblem, maxIterations)
        [x, y] = myHC.evolve()
        best[i] = myHC.best.fitness
        avgY = avgY + y

        # plotting
        '''
        plt.title("Convergence curve")
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        plt.plot(x, y, color="red")
        plt.show()
        '''

    print('AVG = ', best.mean(), ' +/- ', best.std(), ' MAX = ', best.max(), ' MIN =  ', best.min())

    # plotting
    avgY = avgY / maxRepetitions
    plt.title("Average convergence curve")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.plot(avgX, avgY, 'o', color="red")
    plt.show()

    fig1, ax1 = plt.subplots()
    ax1.set_title('Box Plot for best solutions')
    ax1.boxplot(best)
    plt.show()