import numpy as np

best = np.random.uniform(low=-5, high=5,
                                    size=(2,))

        randCells = np.random.uniform(low=-5, high=5,
                                    size=(2,))
        if self.function.evaluate(best) > self.function.evaluate(randCells):
            best = randCells

    self.cells = best
    self.fitness = self.function.evaluate(self.cells)
