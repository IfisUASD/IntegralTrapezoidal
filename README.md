Python algorithm that uses the Trapezoidal rule for aproximating integrals
from a data set.
We know that:

$$\int_a^b f(x) dx \approx \sum_{k=1}^N \frac{f(x_{k-1}) + f(x_k)}{2}\Delta x_k$$
And using this method we can import a data set of the form:
| x | f(x) |
|---|------|
| $$x_1$$ | $f(x_1)$$|
| $$x_2$$ | $f(x_2)$$|
| $$x_3$$ | $f(x_3)$$|
| ... | ...|
| $$x_n$$ | $$f(x_n)$$|


Which should be saved in an external file and will later be parsed onto the main file.
The program will take two arguments:


| Arguments | Description |
|---|---|
| -f | Mandatory, precedes the path for the dataset |
| -g | Optional, if the argument is y then it graphs the dataset |

Finally, the program is to be used as follows on the console:
```console
foo@bar:~$ python3 main.py -f filePath 
```
Or, in case that the graph of the function is needed:
```console
foo@bar:~$ python3 main.py -f filePath -g y
```

Please let me know if there are any questions.


