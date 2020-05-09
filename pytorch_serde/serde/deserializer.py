import torch
import numpy
from .abstract import AbstractDeserializer

class PyTorchDeserializer(AbstractDeserializer):

    def deserialize(self, serialized_state_dict):
        return {key : torch.from_numpy(numpy.asarray(item)).float() for key, item in serialized_state_dict.items()}
