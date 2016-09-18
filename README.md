spar.py – Spatial partitions in Python
======================================

A spar object represents an n-dimensional space that is partitioned into mutually disjoint, nonempty subsets.


Requirements
------------

- Python 2 or 3
- NumPy


Creating a spar
---------------

You can create a spar object by passing a list or array representing the space:

```python
>>> from spar import spar
>>> my_partition = spar([[0,0,1,1], [0,0,1,1], [2,2,3,3], [2,2,3,3]])
```

To view the spatial partition, use ```print()```:

```python
>>> print(my_partition)
[[0 0 1 1]
 [0 0 1 1]
 [2 2 3 3]
 [2 2 3 3]]
```

In this example, we have a 4×4 space partitioned into 4 equally-sized, square-shaped subsets, labeled 0 through 3. Any integer can be used to label each subset, so long as each subset uses a different integer.

To create a spatial partition consisting of a single subset (the trivial partition), just pass the dimensions of the space as a tuple:

```python
>>> my_trivial_partition = spar((5,3))
>>> print(my_trivial_partition)
[[0 0 0]
 [0 0 0]
 [0 0 0]
 [0 0 0]
 [0 0 0]]
```


Indexing a spar
---------------

A spar object can be indexed in two ways. First, you can index by subset label (an integer), which will return a list of points that belong to that subset:

```python
>>> my_partition[0]
[(0, 0), (0, 1), (1, 0), (1, 1)]
```

So, subset 0 consists of points (0, 0), (0, 1), (1, 0), and (1, 1). Second, you can index by point in the space (a tuple), which will return the label of the subset that the point belongs to:

```python
>>> my_partition[2,1]
2
```

So, point (2, 1) belongs to subset 2. If you're dealing with a one-dimensional space, be sure to index points with a trailing comma so that the index is treated as a tuple. Compare:

```python
>>> my_1D_partition = spar([0,0,1,2,2])
>>> my_1D_partition[2]
[(3,), (4,)]
>>> my_1D_partition[2,]
1
```

Spar objects are mutable. To assign a point to a different subset, use:

```python
>>> my_partition[3,3] = 4
>>> print(my_partition)
[[0 0 1 1]
 [0 0 1 1]
 [2 2 3 3]
 [2 2 3 4]]
```

Now point (3, 3) belongs to a new subset (subset 4).


Iterating over a spar
---------------------

Directly iterating over a spar object returns each point in the space and its subset label:

```python
>>> for point, subset_label in my_partition:
...   print(point, subset_label)
...
(0, 0) 0
(0, 1) 0
(0, 2) 1
(0, 3) 1
(1, 0) 0
(1, 1) 0
(1, 2) 1
(1, 3) 1
(2, 0) 2
(2, 1) 2
(2, 2) 3
(2, 3) 3
(3, 0) 2
(3, 1) 2
(3, 2) 3
(3, 3) 4
```

And, of course, if you know how many dimensions there are in advance, you can also unpack the point tuple:

```python
>>> for (x, y), subset_label in my_partition:
...   print(x, y, subset_label)
...
0 0 0
0 1 0
0 2 1
0 3 1
1 0 0
1 1 0
1 2 1
1 3 1
2 0 2
2 1 2
2 2 3
2 3 3
3 0 2
3 1 2
3 2 3
3 3 4
```

To iterate over subsets, use:

```python
>>> for subset in my_partition.subsets():
...   print(subset)
...
[(0, 0), (0, 1), (1, 0), (1, 1)]
[(0, 2), (0, 3), (1, 2), (1, 3)]
[(2, 0), (2, 1), (3, 0), (3, 1)]
[(2, 2), (2, 3), (3, 2)]
[(3, 3)]
```

To iterate over subset labels, use:

```python
>>> for label in my_partition.labels():
...   print(label)
...
0
1
2
3
4
```

To iterate over all points in the space, use:

```python
>>> for point in my_partition.points():
...   print(point)
...
(0, 0)
(0, 1)
(0, 2)
(0, 3)
(1, 0)
(1, 1)
(1, 2)
(1, 3)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
(3, 0)
(3, 1)
(3, 2)
(3, 3)
```


Querying a spar
---------------

To list the labels, points, or subsets of a spar, call ```list()``` on the relevant method call:

```python
>>> list(my_partition.labels())
[0, 1, 2, 3, 4]
>>> list(my_partition.points())
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
>>> list(my_partition.subsets())
[[(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 2), (0, 3), (1, 2), (1, 3)], [(2, 0), (2, 1), (3, 0), (3, 1)], [(2, 2), (2, 3), (3, 2)], [(3, 3)]]
```

Calling ```len()``` on a spar object returns the number of subsets:

```python
>>> len(my_partition)
5
```

To return the size of an individual subset, use:

```python
>>> len(my_partition[2])
4
```

To return the total number of points in the spar, use:

```python
>>> my_partition.size()
16
```

To return the shape (dimensions) of the spar, use:

```python
>>> my_partition.shape()
(4, 4)
```

Naturally, ```len(my_partition.shape())``` gives you the number of dimensions.


Usage examples
--------------

In this example, we'll determine the centroid of each subset:

```python
>>> for subset in my_partition.subsets():
...   x_vals = [subset[i][0] for i in range(len(subset))]
...   y_vals = [subset[i][1] for i in range(len(subset))]
...   x_mean = sum(x_vals) / len(x_vals)
...   y_mean = sum(y_vals) / len(y_vals)
...   print(x_mean, y_mean)
...
0.5 0.5
0.5 2.5
2.5 0.5
2.33333333333 2.33333333333
3.0 3.0
```

In this example, we'll find the smallest subset:

```python
>>> smallest_subset_size = my_partition.size()
>>> for label in my_partition.labels():
...   this_subset_size = len(my_partition[label])
...   if this_subset_size <= smallest_subset_size:
...     smallest_subset_label = label
...     smallest_subset_size = this_subset_size
...
>>> print(smallest_subset_label)
4
```

In this example, we'll iterate over all points in the space and measure how distant each point is, on average, to the members of its subset:

```python
>>> def euclidian_distance(i, j):
...  return sum([(i[dim] - j[dim])**2 for dim in range(len(i))])**0.5
...
>>> for point, label in my_partition:
...   dists = [euclidian_distance(point, member) for member in my_partition[label]]
...   mean_distance = sum(dists) / len(dists)
...   print(point, mean_distance)
... 
(0, 0) 0.853553390593
(0, 1) 0.853553390593
(0, 2) 0.853553390593
(0, 3) 0.853553390593
(1, 0) 0.853553390593
(1, 1) 0.853553390593
(1, 2) 0.853553390593
(1, 3) 0.853553390593
(2, 0) 0.853553390593
(2, 1) 0.853553390593
(2, 2) 0.666666666667
(2, 3) 0.804737854124
(3, 0) 0.853553390593
(3, 1) 0.853553390593
(3, 2) 0.804737854124
(3, 3) 0.0
```

In this example, we'll iterate over all points in the space and print the subset label of the point directly below it (or None if there is no point directly below):

```python
>>> height = my_partition.shape()[0] - 1
>>> for point in my_partition.points():
...   if point[0] < height:
...     point_below = (point[0]+1, point[1])
...     print(point, my_partition[point_below])
...   else:
...     print(point, None)
...
(0, 0) 0
(0, 1) 0
(0, 2) 1
(0, 3) 1
(1, 0) 2
(1, 1) 2
(1, 2) 3
(1, 3) 3
(2, 0) 2
(2, 1) 2
(2, 2) 3
(2, 3) 4
(3, 0) None
(3, 1) None
(3, 2) None
(3, 3) None
```


License
-------

spar.py is licensed under the terms of the MIT License.
