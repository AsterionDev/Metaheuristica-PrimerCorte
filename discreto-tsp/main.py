from hillclimbing import hillclimbing
from tsp import tsp
import numpy as np
import matplotlib.pyplot as plt
from diffTime import diff_time

if __name__ == '__main__':
    max_repetitions = 31
    max_iterations = 1000
    directory = 'problems/'
    myProblem1 = tsp(directory + 'ulysses16..txt')
    myProblem2 = tsp(directory + 'ulysses22.txt')
    myProblem3 = tsp(directory + 'att48.txt')
    myProblem4 = tsp(directory + 'berlin52.txt')
    myProblem5 = tsp(directory + 'pr76.txt')
    my_functions =[myProblem1,myProblem2,myProblem3,myProblem4,myProblem5]

    # algoritmos
    myHC = hillclimbing(max_iterations)
    myHC.hillClimbingClasic()
    myHC2 = hillclimbing(max_iterations)
    myHC2.hillClimbingModified(2)
    my_algorithms = [myHC, myHC2]

    for my_function in my_functions:
        x = np.arange(max_iterations)
        curve = []
        pos = 0
        print("{0:30}".format(str(my_function)), end=" ")
        for my_algorithm in my_algorithms:
            curve.append(np.zeros(max_iterations, float))
            best = np.zeros(max_repetitions, dtype=float)
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



