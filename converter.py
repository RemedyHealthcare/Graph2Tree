import json
import numpy
import redis, os
import cPickle as pickle
from elasticsearch import Elasticsearch
import BeautifulSoup
graph_file = open('graph.json', 'rb')
graph = json.loads(graph_file.read())


id2condition = {}
id_is_root = {}
id2node = {}
condition2roots = {}
root2condition = {}
trees = {}
questions = {}
question_bank = {}
print_database = False
print_form = True
num_helpers = 4

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
            ##print(question_text)
            start_index = question_text.index(']') + 1
            question_type = question_text[:start_index]
            question_type = question_type[1:-1].lower()
             
            question_type_string = 'free_text'
            if question_type == 'mc' or question_type == 'ms':
                question_type_string = 'button'
            if question_type == 'slider':
                question_type_string = 'slider'
           
            question['question_type'] = question_type_string


            question_text_crop = question_text[start_index:].strip()
            ##print(question_text_crop)
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
            if question_type_string == 'slider':
                minmaxcut_string = question_text_crop[end_index:]
                minmaxcut_string = minmaxcut_string.replace('[','').replace(']','')
                minmaxcut = minmaxcut_string.split(',')
                slider_vals = [int(minmaxcut[0]), int(minmaxcut[1]), 0]
                question['answer_choices'] = json.dumps(slider_vals)

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
        #print(sources_to_explore)  
        current_source = sources_to_explore.pop()
        current_fragment = [current_source]
        for edge in graph['edges']:
            if edge['sourceId'] == current_source:
                current_fragment += [edge['targetId']]
                
                sources_to_explore += [edge['targetId']]

                target_indices = get_target_index(current_source, edge)
                for target_index in target_indices:
                    ##print('ADDING ' + target_index)
                    tree += [current_fragment + [target_index]]
                

                current_fragment = [current_source]
        if len(current_fragment) == 1:
            current_fragment += ['<null>', '<null>']
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
    text = source_node['text']

    ##print('CROPPING ' + text)
    crop_start = text.index('[')
    crop_end = text.index(']') + 1
    crop_text = text[crop_start:crop_end]
    text = text.replace(crop_text, '')
    

    answer_label = ['0']
    if question_type == 'slider':

        text = source_node['text']
        for i in range(0,2):
            ##print('CROPPING ' + text)
            crop_start = text.index('[')
            crop_end = text.index(']') + 1
            crop_text = text[crop_start:crop_end]
            text = text.replace(crop_text, '')
        
        
        #cutoff_point = source_node['tex
        #cutoff_text = source_node['text'][:cutoff_point]
        ##print(text)
        ##print(crop_text)
        minmax = crop_text.replace(' ','').replace('[', '').replace(']','')
        minmax = minmax.split(',')
        
        for q in range(len(minmax)):
            minmax[q] = int(minmax[q])

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
            
            cutoff_points = []
            for a_range in other_ranges:
                for val in a_range:
                    if val not in cutoff_points:
                        cutoff_points += [val]
            cutoff_points = sorted(cutoff_points)


            edge_range = edge['label']
            start_index = edge_range.index('(') + 1
            end_index = edge_range.index(')') 
            edge_range = edge_range[start_index:end_index].replace(' ', '').split(',')
            for i in range(len(edge_range)):
                value = int(edge_range[i])
                edge_range[i] = value
            
            question = questions[source_id]
         
           
            cutoffs = [int(minmax[0])]
            ##print(str(source_node))
            for a_range in other_ranges:
                #print(a_range)
                cutoffs += [int(a_range[1])]
            cutoffs += [int(minmax[1])]
            if minmax[0] < cutoffs[0]:
                cutoff_points.insert(0, minmax[0])
            if minmax[1] > cutoffs[-1]:
                cutoff_points += [minmax[1]] 

            question['answer_choices'] = json.dumps(cutoff_points)
        
            for i in range(len(cutoff_points) - 1):
                comp_range = cutoff_points[i:i+1]
                if (edge_range[0] < cutoff_points[1]) or (edge_range[1] > cutoff_points[0]):
                    if str(i) not in answer_label:
                        answer_label += [str(i)]


        else:
            answer_label = ['0']


        


        ###look through other answers to determine proper [min, max, cutoff], and cutoff idex for this question


    if question_type == ('mc' or 'ms'): #eventually change this to properly accoutn for ms
        if '[' in text:
            text = source_node['text']
            

            ##print('CROPPING ' + text)
            crop_start = text.index('[')
            crop_end = text.index(']') + 1
            crop_text = text[crop_start:crop_end]
            text = text.replace(crop_text, '')

                    
            start_index = text.index('[')
            text = text[start_index:]
            
            answer_text = text.replace('[', '').replace(']', '')
            answers = answer_text.split(',')
            if question_type == 'mc':
                if 'label' in edge.keys():
                    for i in range(len(answers)):
                        if edge['label'].lower().strip().replace('[','').replace(']','') == answers[i].lower().strip():

                            answer_label = [str(i)]
 

  
                else:
                    answer_label = ['0']

            else: #is ms.... we aren't handling these yet
                answer_label = ['0']

        else:
             print('NO ANSWERS FOR: ' + str(source_node)) 
        
        
    return answer_label



'''
for id in id_is_root.keys():
    if id_is_root[id]:
        trees[root2condition[id]] = build_from_root(id)
        num_conditions = len(id2condition.keys())
'''
for condition in condition2roots:
    roots = condition2roots[condition]
    condition_tree = []
    for root in roots:
        condition_tree += build_from_root(root)
    trees[condition] = condition_tree
num_conditions = len(trees.keys())

print(str(num_conditions) + ' conditions found in graph.')
print(str(num_roots) + ' roots found in graph.')
print(str(len(graph['nodes'])) + ' nodes found in graph.')
print(str(len(trees.keys())) + ' decision trees made.')

for condition in trees.keys():
    question_bank[condition] = [] 
    for edge in trees[condition]:
        if edge[0] not in question_bank[condition] and edge[0] != '<null>':
            question_bank[condition] = question_bank[condition] + [edge[0]]
        if edge[1] not in question_bank[condition] and edge[1] != '<null>':
            question_bank[condition] = question_bank[condition] + [edge[1]]
        
print(str(len(questions)) + ' questions made.') 

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_password = os.getenv('REDIS_PASSWORD', None)

r = redis.StrictRedis(host=redis_host, port=redis_port, db=0, password=redis_password)
r.flushdb()

condition2id = {}
for id in id2condition.keys():
    condition2id[id2condition[id]] = id 

def make_condition_name(condition):
    #start = condition.index('/')
    end = condition[1:].index('/') + 1
    condition_name = condition[end:]
    condition_name = condition_name.replace('-', ' ')
    condition_name = condition_name[0].upper() + condition_name[1:] 
    return condition_name

symcat_to_disease_id = pickle.load(open('symcat_to_remedy_id.p', 'rb'))



current_question_id = ''
current_doc_display_choices = []
doc_display_lines = open('questions_with_doc_display.txt', 'rb').readlines()
for line in doc_display_lines:
    if line[0] == '*':
        if current_question_id != '':
            questions[current_question_id]['doctor_display_choices'] = json.dumps(current_doc_display_choices)
        current_doc_display_choices = []
        current_question_id = line[1:].replace('\n', '')
    elif line[0] == '-':
        pass
    elif line[0] == '~':
        pass
    else:
        current_doc_display_choices += [line.replace('\n','')]


for condition in question_bank:
    questions_ids = question_bank[condition]
    for question_id in questions_ids:
        if question_id in questions: 
            question = questions[question_id]  
            r.set('question:' + question_id + ':text', question['text'])
            r.set('question:' + question_id + ':question_type', question['question_type'])
            if 'answer_choices' in question.keys():
                r.set('question:' + question_id + ':answer_choices', question['answer_choices'])
            if 'doctor_display_choices' in question.keys():
                r.set('question:' + question_id + ':doctor_display_choices', question['doctor_display_choices'])
        else:
            print('NO QUESTION FOR: ' + question_id)
    symcat_to_remedy_id = pickle.load(open('symcat_to_remedy_id.p', 'rb'))
    symcat_id = condition

    if symcat_id in symcat_to_remedy_id.keys():
        remedy_id = str(symcat_to_remedy_id[symcat_id]) 
        r.set('disease:' +  remedy_id + ':name', make_condition_name(condition))
        question_ids = question_bank[condition] 
        r.rpush('disease:' + remedy_id + ':questions', *question_ids)
        r.set('disease:' + remedy_id + ':decision_tree', json.dumps(trees[condition]))
    else:
        print(symcat_id + ' not in converter!')
if print_database:
    for key in r.scan_iter():
        if ":cond_vec" in key:
            pass
        else:
            try: 
                print key, r.get(key)
            except:
                try:
                    print r.lrange(key, 0, -1)
                except:
                    print r.zrange(key, 0, -1)



div = len(questions.keys())/num_helpers


if print_form:
    for i in range(num_helpers):
        outfile = open('form' + str(i) + '.txt', 'wb')
        if i == num_helpers - 1:
            question_ids = questions.keys()[i*div:]
        else:
            question_ids = questions.keys()[i*div:(i+1)*div]
        for question_id in question_ids:
            question = questions[question_id]
            outfile.write(('*'+question_id + '\n').encode('utf8'))
            outfile.write('-' + (question['question_type'] + ' ' + question['text'] + '\n').encode('utf8'))
            if question['question_type'] == 'button':
                for answer in json.loads(question['answer_choices']):
                    outfile.write(('~ ' + answer.strip() + '\n').encode('utf8'))
        outfile.close()
        


es_host = os.getenv('ELASTICSEARCH_HOST', 'localhost:9200')
es_auth = os.getenv('ELASTICSEARCH_AUTH', None)

if es_host != 'localhost:9200':
    es_host = 'https://' + es_host

es_http_auth = None
if es_auth is not None:
    es_http_auth = (es_auth.split(':')[0], es_auth.split(':')[1])

es = Elasticsearch(
                    [es_host],
                        http_auth=es_http_auth,
                        )
print("populating elasticsearch")
try:
    es.indices.delete("condition")
    es.indices.create("condition")
except:
    print "indices don't exist yet"
    es.indices.create("condition")

symcat = pickle.load(open('symcat_scrape.p', 'rb'))
#print(symcat['conditions'].keys())
for condition_id in question_bank:
    #remedy_id = symcat_to_remedy_id[condition_id]
    condition_questions = question_bank[condition_id]
    question_text = []
    #print('Populating ES for ' + condition_id)
    if condition_id in symcat['conditions'].keys():
        for q_id in condition_questions:
            question_text += [questions[q_id]['text']]
        doc_body = {
                'conditionId' : remedy_id,
                'name' : symcat['conditions'][condition_id]['name'],
                'description' : symcat['conditions'][condition_id]['description'],
                'questions' : question_text
                }
        es.index(index = "condition", doc_type = "v0", body = doc_body)
    else:
        print('Failed to populate ES for ' + condition_id)

'''
id2condition = {}
id_is_root = {}
id2node = {}
condition2roots = {}
root2condition = {}
trees = {}
questions = {}
question_bank = {}
'''

