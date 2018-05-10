# -*- coding: utf-8 -*-
"""
Tue Apr 17 10:46:14 CST 2018
generate webcrawl graph with searching words and related words.
"""
import networkx as nx
# import random
# import uuid
import copy
import logging
from tqdm import tqdm
from web_crawl.google_search.magic_google import MagicGoogle as GoogleSearch
from web_crawl.scholar.scholar import Scholar
import time

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

depth = 10
graph = nx.DiGraph()
base_nodes = []
end_nodes = []
i = 0
new_kw = '创业板'

# gs = GoogleSearch()
# data = gs.gain_data(query=new_kw, language='en', nums=1)
scholar = Scholar()
data = scholar.gain_data('machine learning', language='en', nums=10, pause=2)

base_nodes = data['related_keywords']
logging.debug('base nodes %s' % base_nodes)

#related_keywords = data['RelatedKeywords']
#for kw in related_keywords:
#    base_nodes.append(kw)
#     graph.add_edge(new_kw, kw)
logging.debug(base_nodes)
while i < depth:
    for index, b in enumerate(base_nodes):
        if b not in graph:
            logging.debug('crawling %s' % b)
            data = scholar.gain_data(query=b, language='en', nums=1)
            nodes = data['related_keywords']
        else:
            nodes = []
        logging.debug("new nodes %s" % nodes)
        end_nodes.extend(nodes)
        if len(nodes) > 0:
            for n in nodes:
                graph.add_edge(b, n)
    base_nodes = copy.copy(end_nodes)
    logging.debug('level %s nodes: %s' % (i, end_nodes))
    end_nodes = []
    i += 1

ls_nodes = list(graph.nodes)
counter = 0
total_nodes_num = len(graph.nodes)
rm_counter = 0

# while True:
#     logging.debug('rm cycles loops number %s' % counter)

#     for node in tqdm(ls_nodes):
#         removed_counter = 0
#         # ylog.debug('rm cycles of node %s' % node)

#         while True:
#             try:
#                 ls_loop = nx.find_cycle(graph, node)
#                 removed_counter += 1
#                 # remove direct edge:
#                 #                    ylog.debug(ls_loop)
#                 if len(ls_loop) == 2:
#                     if ls_loop[0][0] == ls_loop[1][1] and ls_loop[0][1] == ls_loop[1][0]:
#                         graph.remove_edge(ls_loop[0][0], ls_loop[0][1])
#                 # remove big loop:
#                 elif len(ls_loop) == 1:
#                     break
#                 elif len(ls_loop) > 2:

#                     graph.remove_edge(ls_loop[-1][0], ls_loop[-1][1])
#                     # remove all edges in the loop, then next create edge first in.
#                     # for i in range(len(ls_loop) - 1):
#                     #     graph.remove_edge(ls_loop[i + 1][0],
#                     #                       ls_loop[i + 1][1])
#                 # counter = 0
#             except nx.NetworkXNoCycle:
#                 counter += 1
#                 if removed_counter != 0:
#                     logging.debug('rm cycles number %s' % removed_counter)
#                 break

nx.write_gexf(graph, "machine_learning.gexf")
