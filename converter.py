import json
import numpy

graph_file = open('graph.json', 'rb')
graph = json.loads(graph_file.read())


id2condition = {}
id_is_root = {}
id2node = {}
condition2roots = {}
root2condition = {}
trees = {}


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

for condition in condition2roots.keys():
    roots = condition2roots[condition]
    for root in roots:
       root2condition[root] = condition
        

def build_from_root(id):
    tree = []
    sources_to_explore = [id]
    while len(sources_to_explore) > 0:
        current_source = sources_to_explore.pop()
        current_fragment = [current_source]
        for edge in graph['edges']:
            if edge['sourceId'] == current_source:

                current_fragment += [edge['targetId']]
                current_fragment += get_target_index(current_source, edge)
                sources_to_explore += [edge['targetId']]
        if len(current_fragment) == 1:
            current_fragment += ['<none>', '<none>']
        tree += [current_fragment]

def get_target_index(source_id, edge):
    print('EDGE : ' + str(edge))
    source_node = id2node[source_id]
    print('SOURCE NODE TEXT: ' + source_node['text'])
    
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
    print('QUESTION TYPE: ' + question_type)
    for i in range(0, 2):   
        text = source_node['text']  
        crop_start = text.index('[')
        crop_end = text.index(']') + 1
        crop_text = text[crop_start:crop_end]
        text = text.replace(crop_text, '')
    

    answer_label = '0'
    if question_type == 'slider':    
         
        minmax = crop_text.replace(' ','').replace('[', '').replace(']','')
        minmax = minmax.split(',')
        if edge['label'] != '':
            all_edges = graph['edges']
            other_answers = []
            other_ranges = []
            for other_edge in all_edges:
                if other_edge['sourceId'] == source_id:
                    if other_edge['label'] != '':
                        other_answers.append(other_edge['label'])
            for answer_set in other_answers:
                start_index = answer_set.index('(') + 1
                end_index = answer_set.index(')')
                other_ranges += [answer_set[start_index:end_index].replace(' ', '').split(',')]
            for i in range(0,len(other_ranges)):
                other_range = other_ranges[i]
                for j in range(0, len(other_range)):
                    other_range[j] = int(other_range[j])
                other_ranges[i] = other_range
            other_ranges = sorted(other_ranges, key = lambda other_range:other_range[0])
            
            edge_range = edge['label']
            start_index = edge_range.index('(') + 1
            end_index = edge_range.index(')') 
            edge_range = edge_range[start_index:end_index].replace(' ', '').split(',')
            for i in range(len(edge_range)):
                value = int(edge_range[i])
                edge_range[i] = value
            for i in range(len(other_ranges)):
                other_range = other_ranges[i]
                if other_range == edge_range:
                    answer_label = str(i)
        else:
            answer_label = '0'


        


        ###look through other answers to determine proper [min, max, cutoff], and cutoff idex for this question


    if question_type == ('mc' or 'ms'): #eventually change this to properly accoutn for ms
        answer_text = crop_text.replace('[', '').replace(']', '')
        answers = answer_text.split(',')
        if question_type == 'mc':
            if 'label' in edge.keys():
                for i in range(len(answers)):
                    if edge['label'].lower().replace(' ', '') == answers[i].lower().replace(' ', ''):
                        answer_label = str(i)
            else:
                answer_label = '0'

        else: #is ms.... we aren't handling these yet
            answer_label = '0'

            
        
        
    return answer_label

for id in id_is_root.keys():
    if id_is_root[id]:
        trees[root2condition[root]] = build_from_root(id)
        num_conditions = len(id2condition.keys())
print(str(num_conditions) + ' conditions found in graph.')
print(str(num_roots) + ' roots found in graph.')
print(str(len(graph['nodes'])) + ' nodes found in graph.')
