from .image_node import BatchImageAndPrompt
from .node import BatchInputText, BatchInputCSV

NODE_CLASS_MAPPINGS = {
    "BatchInputText": BatchInputText,
    "BatchInputCSV": BatchInputCSV,
    "BatchImageAndPrompt": BatchImageAndPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BatchInputText": "📝Batch input text",
    "BatchInputCSV": "📝Batch input CSV",
    "BatchImageAndPrompt": "🖼Batch input image and prompt",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
