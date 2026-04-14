import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        allws = set()

        allw = positive + negative

        for s in allw:
            for w in s.split():
                allws.add(w) 

        sorted_l = sorted(list(allws))
        word_to_i = {}

        for i, c in enumerate(sorted_l):
            word_to_i[c] = i + 1

        def encode(s):
            integers = []
            for w in s.split():
                integers.append(word_to_i[w])
            return integers

        var_len_tensor = []

        for s in allw:
            var_len_tensor.append(torch.tensor(encode(s)))

        return nn.utils.rnn.pad_sequence(var_len_tensor, batch_first=True)
