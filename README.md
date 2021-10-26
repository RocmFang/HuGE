# HuGE

This repository provides a reference implementation of *HuGE* as described in the paper:<br>

HuGE: An Entropy-driven Approach to Efficient and Scalable Graph Embeddings.<br>
Peng Fang, Fang Wang, Zhan Shi, Hong Jiang, Dan Feng, and Lei Yang <br>
Accepted to [37th IEEE International Conference on Data Engineering, 2021.](https://icde2021.gr) pdf <br>


## Prerequisites

- Linux
- Python 2 or 3
- networkx
- gensim
- multiprocessing

## Basic Usage

### Example
To run *HuGE* on the example graphs, execute the following command from the project home directory:<br/>

#### Preprocessing
Executing the preprocessing operation to compute the common neighbors for each pair-node in the graph.<br/>
    ``python src/common_neighbor_preprocess.py --input ./graph/CA-AstroPh.txt --output ./pre_data/CA-AstroPh_comneig.txt`` 
	
#### Trainging    
Training on the existing graphs and generating the embeddings. <br/>
- Single thread version<br/>
    ``python src/main.py --input ./graph/CA-AstroPh.txt --comnb ./pre_data/CA-AstroPh_comneig.txt --output ./emb/CA-AstroPh.emb``
- Parallel version<br/>
     ``python src-p/main_pel.py --input ./graph/CA-AstroPh.txt --comnb ./pre_data/CA-AstroPh_comneig.txt --output ./emb/CA-AstroPh.emb``
     
### Options
You can check out the other options available to use with *HuGE* using:<br/>
	``python src/main.py --help``

### Input
The supported input format is an edgelist:
		
The graph is assumed to be undirected and unweighted by default. These options can be changed by setting the appropriate flags.


### Output
The output file has *n+1* lines for a graph with *n* vertices. 
The first line has the following format:

	number of nodes   dimensions of representation

The next *n* lines are as follows:
	
	node_id dim1 dim2 ... dimd

where dim1, ... , dimd is the *d*-dimensional representation learned by *HuGE*.

## Citing
If you find *HuGE* useful for your research, please consider citing the following paper:

	@inproceedings{HuGE-ICDE2021,
	author = {Peng Fang, Fang Wang, Zhan Shi, Hong Jiang, Dan Feng, and Lei Yang},
	 title = {HuGE: An Entropy-driven Approach to Efficient and Scalable Graph Embeddings},
	 booktitle = {Proceedings of the 37th IEEE International Conference on Data Engineering, {ICDE 2021}},
	 year = {2021}
	}


## Miscellaneous

Please send any questions you might have about the code and/or the algorithm to <fangpeng@hust.edu.cn> or feel free to open an issue.

*Note:* This is only a reference implementation of the *HuGE* algorithm and could benefit from several performance enhancement schemes, some of which are discussed in the paper.
