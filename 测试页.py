import torch
import re

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

sos_token = 0
eos_token = 1
max_length = 10
data_path = 'data/eng-fra-v2.txt'
batch_size = 2

def normalizeString():
    s = s.lower().strip()
    s = re.sub(r'[^a-z!?]+',r'',s)