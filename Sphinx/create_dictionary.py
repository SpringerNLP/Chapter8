import collections
import os

counter = collections.Counter()
dir = '/data/datasets/CommonVoice_dataset/cv-valid-train/txt/'
for filename in os.listdir(dir):
    with open(os.path.join(dir, filename)) as f:
        counter += collections.Counter(f.read().split())

with open('test.dic', 'w') as f: 
    for item in counter:
        f.write(item.lower() + '\n')
