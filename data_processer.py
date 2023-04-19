import json
import random
import os

def get_category(f=''):
  return f.replace('_', ' ').replace('5', '').replace(' .json', '')

file_names = os.listdir('./origin')
categories = [get_category(f) for f in file_names]

data = []
for (file_name, category) in zip(file_names, categories):
  with open(f'./origin/{file_name}') as f:
    for line in f:
      review = json.loads(line)
      review['category'] = category

      year = int(review['reviewTime'].split(' ')[-1])
      if year == 2017 or year == 2018 or year == 2016:
        data.append(review)

final_data = random.sample(data, 100000)

print(len(final_data))

with open(f'./processed/data_small.json', 'w') as f:
	for review in final_data:
		f.write(json.dumps(review)+'\n')
