# Disney movie networks
## Summary
This repository provides the network datasets that represent the characters' relationships in Disney movies. 
In networks, the nodes are the characters appeared in movies and the edges are the co-appearance of node pairs in the same scene who communicated with each other at least one time. The edges have weights that represent the positive or negative relationships between nodes. Two nodes with a positive edge (weight=1) have supportive relationships in the movie, whereas two nodes with a negative edge (weight=-1) have opposing relationships. 

The script `generate_network.py` plots the networks based on the input adjacency matrix of characters and provides some network statistics. To run the code, adjacency matrix saved as `.csv` format should be located in `datasets/` folder. The code generates network plot and saves in `plots/` folder.
The following is the example of running the script.
```
python generate_network.py -filename jungle_book_adj.csv -title jungle_book
```

## Requirements
Some Python packages are needed to plot networks:
* pandas
* numpy
* igraph
* pycairo

## Example networks
1. *Jungle Book*
* Network visualization

![image](https://user-images.githubusercontent.com/12605926/125357772-b1be3c00-e32d-11eb-81f7-e936d8926c20.png)

* Network statistics

|Statistics|Value|
|---------------|--|
|Number of nodes|14|
|Number of edges|30|
|Number of positive edges|21|
|Number of negative edges|9|
|Node with highest degree|Mowgli|
|Node with the greatest relationship|Mowgli|
|Node with the poorest relationship|Shere Khan|

2. *UP*
* Network visualization

![image](https://user-images.githubusercontent.com/12605926/125362252-34e29080-e334-11eb-8f21-98ab7770d4ec.png)

* Network statistics

|Statistics|Value|
|---------------|--|
|Number of nodes|11|
|Number of edges|38|
|Number of positive edges|17|
|Number of negative edges|21|
|Node with highest degree|Carl Fredricksen|
|Node with the greatest relationship|Ellie Fredricksen|
|Node with the poorest relationship|Russell|
