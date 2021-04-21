import argparse
import networkx as nx
from multiprocessing import Process, Manager, cpu_count
import time
import os


def parse_args():
    "Preprocessing for the commoneighbor"

    parser = argparse.ArgumentParser(description='Preprocessing Commoneigbors')

    parser.add_argument('--input', nargs='?', default='../graph/CA-AstroPh.txt',
                        help='Input graph path')

    parser.add_argument('--output', nargs='?', default='../pre_data/CA-AstroPh_comneig.txt',
                        help='output the common neighbors')

    parser.add_argument('--workers', type=int, default=10,
                        help='Number pf parallel workers, default = 10')

    return parser.parse_args()

def read_graph():
    '''
    Reads the input network in networkx.
    '''

    G = nx.read_edgelist(args.input, nodetype=int, create_using=nx.Graph())

    return G


def common_neighbors_score_parallel(G, nodes, num_workers=cpu_count()):

    comneb_file = args.output

    if os.path.exists(comneb_file):
        os.remove(comneb_file)

    tt0 = time.time()

    with Manager() as manager:

        comm_neighbor = manager.dict()
        comm_nei_list = []

        node_len = len(nodes)

        tt1 = time.time()

        for i in range(num_workers):

            start = node_len * i // num_workers
            end = node_len * (i + 1) // num_workers

            ttt1 = time.time()

            comm_nei = Process(target=common_neighbor_process, args=(G, nodes[start:end], comm_neighbor))

            comm_nei.start()

            ttt2 = time.time()

            print i, 'time used:', (ttt2 - ttt1), 's'

            comm_nei_list.append(comm_nei)

        # print comm_nei_list

        tt2 = time.time()

        for res in comm_nei_list:
            # print res
            res.join()

        _comm_neighbor = comm_neighbor.copy()

        tt3 = time.time()

        f = open(comneb_file, 'a+')

        for edge in _comm_neighbor:
            f.write(u"{} {} {}\n".format(str(edge[0]), str(edge[1]), str(_comm_neighbor[edge])))

        f.close()



        print 'prepare:', (tt1 - tt0), 's'
        print "process parallel:", (tt2 - tt1), 's'
        print 'combine used:', (tt3 - tt2), 's'

    return _comm_neighbor

def common_neighbor_process(G, nodes, comm_neighbor):

    for cur in nodes:

        for w in G[cur]:
            v_nei = G[cur].keys()
            v_nei.remove(w)
            comm_neighbor[cur, w] = len(set(v_nei).intersection(set(G[w].keys())))
    #


    return comm_neighbor


def main(args):
    print("load graph")
    nx_G = read_graph()

    print("Common neighbor preparing:")

    time1 = time.time()
    nodes = list(nx_G.nodes())
    common_neighbors_score_parallel(nx_G, nodes, args.workers)
    time2 = time.time()

    print "Common neighbor time:", (time2-time1), 's'


if __name__ == "__main__":
    args = parse_args()
    main(args)