# -*- coding: utf-8 -*-

# Python program to detect cycle
# in a graph

from collections import defaultdict
from ylib import ylog
import re
from lib.gftTools import gftIO
import os
import sys
import logging
from tqdm import tqdm
import time
import json
import networkx as nx

ylog.set_level(logging.DEBUG)
ylog.console_on()
ylog.filelog_on("cycles")
graph = nx.read_gexf('whole_edges.no_loops.gexf')
ls_nodes = list(graph.nodes)
counter = 0
total_nodes_num = 287966
rm_counter = 0
try:
    while True:
        ylog.debug('rm cycles loops number %s' % counter)

        for node in tqdm(ls_nodes):
            removed_counter = 0
            ylog.debug('rm cycles of node %s' % node)

            while True:
                try:
                    ls_loop = nx.find_cycle(graph, node)
                    # remove direct edge:
                    ylog.debug(ls_loop)
                    if len(ls_loop) == 2:
                        if ls_loop[0][0] == ls_loop[1][1] and ls_loop[0][1] == ls_loop[1][0]:
                            graph.remove_edge(ls_loop[0][0], ls_loop[0][1])
                    # remove big loop:
                    elif len(ls_loop) > 2:
                        graph.remove_edge(ls_loop[-1][0], ls_loop[-1][1])
                        # remove all edges in the loop, then next create edge first in.
                        # for i in range(len(ls_loop) - 1):
                        #     graph.remove_edge(ls_loop[i + 1][0],
                        #                       ls_loop[i + 1][1])
                    # counter = 0
                    removed_counter += 1
                except nx.NetworkXNoCycle:
                    counter += 1
                    if removed_counter != 0:
                        ylog.debug('rm cycles number %s' % removed_counter)
                    break

        if counter >= total_nodes_num - 1:
            break
except KeyboardInterrupt:
    nx.write_gexf(graph, 'whole_edges.no_loops.gexf')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
nx.write_gexf(graph, 'whole_edges.no_loops.gexf')
