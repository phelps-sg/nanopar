
# nanopar

A lightweight parallel map implementation that can be used for parallel processing on multiple cores without
requiring pickling of data.

This code is taken almost verbatim from
<https://stackoverflow.com/questions/3288595/multiprocessing-how-to-use-pool-map-on-a-function-defined-in-a-class#16071616>.

## Installation

~~~bash
cd src/main/python
python setup.py install
~~~

## Usage

~~~python
from nanopar.map import parmap
import numpy as np

results = parmap(lambda x: x*x, np.arange(0., 10e8))
~~~
