# pytorch-serde

Serialization and Deserialization Utilities for PyTorch.

## Usage

Serialization:
```
from pytorch_serde.serde import PyTorchSerializer

# https://pytorch.org/tutorials/beginner/saving_loading_models.html
# state_dict = model.state_dict()
PyTorchSerializer().serialize(state_dict)
```

Deserialization:
```
from pytorch_serde.serde import PyTorchDeserializer

# serialized_state_dict = serialized state dict from serialization example
PyTorchDeserializer().deserialize(serialized_state_dict)
```
