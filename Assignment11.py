import numpy as np
import pandas as pd

rng = np.random.default_rng()

random_series = pd.Series(rng.random(10))

print(random_series)
