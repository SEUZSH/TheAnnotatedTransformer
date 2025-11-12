
import pandas as pd

splits = {'train': 'train.jsonl', 'validation': 'val.jsonl', 'test': 'test.jsonl'}
df = pd.read_json("hf://datasets/bentrevett/multi30k/" + splits["train"], lines=True)