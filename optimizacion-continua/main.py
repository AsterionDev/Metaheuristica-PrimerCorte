import numpy as np
from hillclimbing import hillclimbing
from sphere import sphere
from step import step
from Ackley import Ackley
from Griewank import Griewank
from Rastrigin import Rastrigin
from Schwefel import Schwefel
from diffTime import diff_time
import matplotlib.pyplot as plt

if __name__ == "__main__":
    my_step = step(-5.0, 5.0)
    my_shpere = sphere(-5.0, 5.0)
    my_schwefel = Schwefel(-100, 100)
    my_rastrigin = Rastrigin(-5.12, 5.12)
    my_griewank = Griewank(-600, 600)
    my_ackley = Ackley(-32, 32)
    my_functions = [
        my_shpere,
        my_step,
        my_schwefel,
        my_rastrigin,
        my_griewank,
        my_ackley,
    ]

    max_iterations = 1000
    dimensions = 10
    max_repetitions = 31

    # algoritmos
    myHC = hillclimbing(max_iterations)
    myHC.hillcilmbingClasico(0.5)
    myHC2 = hillclimbing(max_iterations)
    myHC2.hillcilmbingModified(10, 5)
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
                curve[pos] = curve[pos] + my_algorithm.evolve(my_function, 2)
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


