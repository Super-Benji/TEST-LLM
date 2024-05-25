import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from collections import Counter
import sklearn
import re
import time

Start_time = time.time()

dataset = pd.read_json('test.json')


Q_A = dataset['input']

index_list = []

Question_list = []

Answer_list = []


for i in range(len(dataset)):
    
    mess = Q_A[i]
    
    Question = re.findall(r'Does.*?\?', mess)
    
    Question_list += Question
    
    Answer = re.findall(r'\s+(Yes|No)+\n\n', mess, flags = re.I)
    
    Answer_list +=  Answer
    
    Answer_list.append('Options: Yes or No')
    
    index_list += [i] * len(Question) 
    


dictionary_format = {'id': index_list,
                     'Question': Question_list,
                     'Answer': Answer_list}

refined_dataset = DataFrame(dictionary_format)

End_time = time.time()

Json_data = refined_dataset.to_json(orient='records')


#%%

counter = Counter(Answer_list)

Undecided_answer = counter.get('Options: Yes or No')

Decided_answer = len(refined_dataset) - Undecided_answer

Process_time = End_time - Start_time
    
print('The total number of question-answer pairs extracted from the dataset is \n',len(refined_dataset))

print('The total number of question-answer pairs with exact answer is \n',Decided_answer)

print('The total number of question-answer pairs with undecided answer is \n',Undecided_answer)

print(f'The time taken to complete the dataset cleanup and transformation process is \n {Process_time}s')
    
    
    




