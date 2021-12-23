from hillclimbing import hillclimbing
from knapsack import knapsack
from diffTime import diff_time
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    max_repetitions = 31
    max_iterations = 1000
    directory = 'problems/'
    myProblem1 = knapsack(directory + 'Knapsack1.txt')
    myProblem2 = knapsack(directory + 'Knapsack2.txt')
    myProblem3 = knapsack(directory + 'Knapsack3.txt')
    myProblem4 = knapsack(directory + 'Knapsack4.txt')
    myProblem5 = knapsack(directory + 'Knapsack5.txt')
    myProblem6 = knapsack(directory + 'Knapsack6.txt')
    my_functions =[myProblem1,myProblem2,myProblem3,myProblem4,myProblem5, myProblem6]

    # algoritmos
    myHC = hillclimbing(max_iterations)
    myHC.hillClimbingClasic()
    myHC2 = hillclimbing(max_iterations)
    myHC2.hillClimbingModified(5)
    my_algorithms = [myHC, myHC2]

    for my_function in my_functions:
        x = np.arange(max_iterations)
        curve = []
        pos = 0
        print("{0:30}".format(str(my_function)), end=" ")
        for my_algorithm in my_algorithms:
            curve.append(np.zeros(max_iterations, float))
            best = np.zeros(max_iterations, dtype=float)
            my_time = diff_time()
            for this_repetition in range(max_repetitions):
                np.random.seed(this_repetition)
                curve[pos] = curve[pos] + my_algorithm.evolve(my_function)
                best[this_repetition] = my_algorithm.best.fitness

            print(
                "{0:20}".format(str(my_algorithm))
                + " {0:12.6f}".format(best.mean())
                + " {0:12.6f}".format(best.std())
                + " {0:12.6f}".format(best.max())
                + " {0:12.6f}".format(best.min())
                + " {0:10.5f}".format(my_time.end() / max_repetitions),
                end=" ",
            )
            curve[pos] = curve[pos] / max_repetitions
            pos = pos + 1

        print("")

        #plotting
        plt.title("Convergence curve" + str(my_function))
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        leg=[]
        for i in range(len(my_algorithms)):
            plt.plot(x, curve[i])
            leg.append(str(my_algorithms[i]))
        plt.legend(leg)
        plt.show()




