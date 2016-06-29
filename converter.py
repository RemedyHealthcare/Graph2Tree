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
questions = {}


for i in range(len(graph['nodes'])):
    node = graph['nodes'][i]
    id2node[node['id']] = node
    id_is_root[node['id']] = False
    if 'onditions/' in node['text']:
        id = node['id']
        id2condition[id] = node['text'].lower()

for i in range(len(graph['nodes'])):
    node = graph['nodes'][i]
    if node['id'] not in id2condition.keys():
        question = {}
        question_text = node['text']

        if '[' in question_text:
            print(question_text)
            start_index = question_text.index(']') + 1
            question_type = question_text[:start_index]
            question_type = question_type[1:-1].lower()
            if question_type == ('mc' or 'ms'):
                question_type_string = 'button'
            if question_type == 'slider':
                question_type_string = 'slider'
            else: 
                question_type_string = 'free_text'
            question['question_type'] = question_type_string


            question_text_crop = question_text[start_index:].strip()
            print(question_text_crop)
            if '[' in question_text_crop:
                end_index = question_text_crop.index('[')
                text = question_text_crop[:end_index]
            else:
                text = question_text_crop
            question['text'] = text
            if question_type_string == 'button':
                answer_string = question_text_crop[end_index:]
                answer_string = answer_string.replace('[','').replace(']','')
                answer_options = answer_string.split(',')
                question['answer_choices'] = json.dumps(answer_options)
                
            questions[node['id']] = question



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
                tree += [current_fragment]
                current_fragment = [current_source]
        if len(current_fragment) == 1:
            current_fragment += ['<none>', '<none>']
            tree += [current_fragment]
      
    return tree
def get_target_index(source_id, edge):
   
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
    if question_type == 'slider':    
         
        minmax = text.replace(' ','').replace('[', '').replace(']','')
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
            
            question = questions[source_id]
         
           
            cutoffs = [int(minmax[0])]
            for a_range in other_ranges:
                cutoffs += [int(a_range[1])]
            cutoffs += [int(minmax[-1])]
            question['answer_choices'] = json.dumps(cutoffs)

            for i in range(len(other_ranges)):
                other_range = other_ranges[i]
                if other_range == edge_range:
                    answer_label = str(i)
        else:
            answer_label = '0'


        


        ###look through other answers to determine proper [min, max, cutoff], and cutoff idex for this question


    if question_type == ('mc' or 'ms'): #eventually change this to properly accoutn for ms
        if '[' in text:
                    
            start_index = text.index('[')
            text = text[start_index:]
            
            answer_text = text.replace('[', '').replace(']', '')
            answers = answer_text.split(',')
            if question_type == 'mc':
                if 'label' in edge.keys():
                    for i in range(len(answers)):
                        if edge['label'].lower().strip().replace('[','').replace(']','') == answers[i].lower().strip():

                            answer_label = str(i)
 

  
                else:
                    answer_label = '0'

            else: #is ms.... we aren't handling these yet
                answer_label = '0'

        else:
             print('NO ANSWERS FOR: ' + str(source_node)) 
        
        
    return answer_label

for id in id_is_root.keys():
    if id_is_root[id]:

        trees[root2condition[id]] = build_from_root(id)
        num_conditions = len(id2condition.keys())

print(str(num_conditions) + ' conditions found in graph.')
print(str(num_roots) + ' roots found in graph.')
print(str(len(graph['nodes'])) + ' nodes found in graph.')
print(str(len(trees.keys())) + ' decision trees made.')
