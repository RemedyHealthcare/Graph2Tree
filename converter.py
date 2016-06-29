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
tree = []
for id in id_is_root.keys():
    if id_is_root[id]:
        tree.append(build_from_root(id)) 



num_conditions = len(id2condition.keys())

print(str(num_conditions) + ' conditions found in graph.')
print(str(num_roots) + ' roots found in graph.')
print(str(len(graph['nodes'])) + ' nodes found in graph.')

func build_from_root(id):
    tree = []
    current_source = id
    current_fragment = [id]
    for edge in graph['edges']:
        if edge['sourceId'] == current_source:
            current_fragement += [edge['targetId']]

func get_target_index(source_id, edge):
    source_node = id2node[source_id]
    question_type = ''
    
    if '[mc]' in source_node['text'].lower():
        question_type = 'mc'
    if '[slider]' in source_node['text'].lower():
        question_type = 'slider'
    if '[ms]' in source_node['text'].lower():
        question_type = 'ms'
    if '[text]' in source_node['text'].lower():
        question_type = 'text'
    if '[test]' in source_node['text'].lower():
        question_type = 'test'
    for i in range(0, 2):   
        text = source_node['text']  
        crop_start = text.index('[')
        crop_end = text.index(']') + 1
        crop_text = text[crop_start:crop_end]
        text = text.replace(crop_text, '')
    

    answer_label = '0'
    if question_type == 'slider'    
        cutoffs = crop_text.replace(' ','').replace('[', '').replace(']','')
        cutoffs = cutoffs.split(',')
        all_edges = graph['edges']
        other_answers = []
        for other_edge in all_edges:
            if other_edge['source_id'] == source_id:
                other_answers.append(other_edge['label'])

        ###look through other answers to determine proper [min, max, cutoff], and cutoff idex for this question


    if question_type == ('mc' or 'ms'): #eventually change this to properly accoutn for ms
        answer_text = crop_text.replace('[', '').replace(']', '')
        answers = answer_text.split(',')
        if question_type == 'mc':
            for i in range(len(answers)):
                if edge['label'].lower().replace(' ', '') == answers[i].lower().replace(' ', ''):
                    answer_label = str(i)
        else: #is ms.... we ren't handling these yet
            answer_label = '0'

            
        
        

