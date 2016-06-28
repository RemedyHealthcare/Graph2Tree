import json
import numpy

graph_file = open('graph.json', 'rb')
graph = json.loads(graph_file.read())


id2condition = {}
id_is_root = {}
id2node = {}
condition2roots = {}


for i in range(len(graph['nodes'])):
    node = graph['nodes'][i]
    id2node[node['id']] = node
    id_is_root[node['id']] = False
    if 'onditions/' in node['text']:
        id = node['id']
        id2condition[id] = node['text'].lower()

num_roots = 0

for edge in graph['edges']:
    if edge['sourceId'] in id2condition.keys():
        id_is_root[edge['targetId']] = True
        if id2condition[edge['sourceId']] not in condition2roots:
            condition2roots[id2condition[edge['sourceId']]] = [edge['targetId']]
        else:
            condition_roots = condition2roots[id2condition[edge['sourceId']]]
            condition_roots += [edge['targetId']]
            condition2roots[id2condition[edge['sourceId']]] = condition_roots
        num_roots += 1


num_conditions = len(id2condition.keys())

print(str(num_conditions) + ' conditions found in graph.')
print(str(num_roots) + ' roots found in graph.')
print(str(len(graph['nodes'])) + ' nodes found in graph.')

        

