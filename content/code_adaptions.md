# Code Adaptions

Even in an embarassingly parallel situation we will have to make a couple of adaptions to the code
in order to be able to run parallel executions of our code.

## Updating the code to obtain input parameters

First off, we will need to allow the programm to receive input parameters that define which element(s)
of the data have to be computed by this instance.

So from this:

```
data = load_and_preprocess_data

for i in 1,2,3,...,n do:
   res[i] = calculate(data[i])

save(res)

```

We need to create something like:

```
i = input_arg

data = load_and_preprocess_data(i)
res = calculate(data)

save res as res_i
```

## Collection script

Since we are now producing multiple individual results, we will have to collect them and put them together
into our actual result. This highly depends on your result data, but in general it will take the form of

```
res = [] of length n
for i in 1,2,3...n do:
   res[i] = load(res_i)

save(res)
```

## Exercise

````{exercise} Parallel-1: Make the script accept an input index
We will be working with a an example of a company that sells in
several markets. More precisely, they want to sell their products in several coutries.
They are quite specialised and their target audience are smaller businesses that are located
all over the countries they want to sell in. They have one representative per country and thus
that representative will have to visit many cities (a classical traveling salesman problem).
They want to optimise the travel time for these representatives and have a program to do so
for all of their representatives.

The code does use the `python_tsp` library as well as `numpy`, `scipy` and `pandas`.
We provide a conda environment file that will create an environment for you that can run this
For simplicity, we will just use the distances between the places instead of actual routes.
The locations of the cities that need to be visited along with their countries is provided
in {download}`cities.csv <code/cities.csv>`.
The code itself is provided {download}`here </code/python/traveling_salesman.py>`:
```{literalinclude} code/python/traveling_salesman.py
    :language: python
```

Adapt the code, such that it takes an integer input value for each calculation

````

````{solution} Solution: Parallel-1
The simplest solution is to use `sys.argv` taking in the first argument and converting
it to an integer. You can also use more elaborate input parsers (see for example
[this lecture about argument parsing](https://aaltoscicomp.github.io/python-for-scicomp/scripts/#parsing-command-line-arguments-with-argparse))

```{literalinclude} code/python/traveling_salesman_for_index.py
    :language: python
    :emphasize-lines: 5, 28-45
```

````
