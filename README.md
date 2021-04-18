# HuGE

This repository provides a reference implementation of *HuGE* as described in the paper:<br>
> HuGE: An Entropy-driven Approach to Efficient and Scalable Graph Embeddings.<br>
> Peng Fang, Fang Wangy, Zhan Shi, Hong Jiang, Dan Feng, and Lei Yang <br>
> 37th IEEE International Conference on Data Engineering, 2021.<br>
> <Insert paper link>

The *HuGE* algorithm learns continuous representations for nodes in any (un)directed, (un)weighted graph. 

## Prerequisites

- Linux or macOS
- Python 2 or 3
- networkx
- gensim
- multiprocessing

### Basic Usage

#### Example
To run *HuGE* on the example graphs, execute the following command from the project home directory:<br/>
## preprocess
Executing the preprocessing operation for generating the common neighbors of the input graoph and then loading to the main function.<br/>
    ``python src/common_neighbor_preprocess.py --input ../graph/CA-AstroPh.txt --output ../pre_data/CA-AstroPh_comneig.txt``
Training on the existing graphs and generating the embeddings 
    ``python src/main.py --input ../graph/CA-AstroPh.txt --comnb ../pre_data/CA-AstroPh_comneig.txt --output ../emb/CA-AstroPh.emb``

#### Options
You can check out the other options available to use with *HuGE* using:<br/>
	``python src/main.py --help``

#### Input
The supported input format is an edgelist:
		
The graph is assumed to be undirected and unweighted by default. These options can be changed by setting the appropriate flags.

#### Output
The output file has *n+1* lines for a graph with *n* vertices. 
The first line has the following format:

	num_of_nodes dim_of_representation

The next *n* lines are as follows:
	
	node_id dim1 dim2 ... dimd

where dim1, ... , dimd is the *d*-dimensional representation learned by *HuGE*.

### Citing
If you find *HuGE* useful for your research, please consider citing the following paper:

	@inproceedings{HuGE-ICDE2021,
	author = {Peng Fang, Fang Wangy, Zhan Shi, Hong Jiang, Dan Feng, and Lei Yang},
	 title = {HuGE: An Entropy-driven Approach to Efficient and Scalable Graph Embeddings},
	 booktitle = {Proceedings of the 37th 37th IEEE International Conference on Data Engineering},
	 year = {2021}
	}


### Miscellaneous

Please send any questions you might have about the code and/or the algorithm to <fangpeng@hust.edu.cn>.

*Note:* This is only a reference implementation of the *HuGE* algorithm and could benefit from several performance enhancement schemes, some of which are discussed in the paper.
