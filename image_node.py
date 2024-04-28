import torch
import numpy as np
from PIL import Image, ImageOps


class BatchImageAndPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_list": ("STRING", {
                    "multiline": True,
                    "default": "output/ComfyUI_00001_.png,output/ComfyUI_00002_.png,apple\n"
                               "output/ComfyUI_00003_.png,output/ComfyUI_00004_.png,pineapple"
                }),
                "delimiter": ("STRING", {
                    "default": ","
                })
            },
        }

    RETURN_TYPES = ("IMAGE", "IMAGE", "STRING")
    RETURN_NAMES = ("image1", "image2", "prompt")

    FUNCTION = "split"
    OUTPUT_NODE = False
    CATEGORY = "🐳BatchInput"
    OUTPUT_IS_LIST = (True, True, True)

    def split(self, text_list, delimiter):
        text_list = text_list.split("\n")
        image1_list = []
        image2_list = []
        prompt_list = []
        for line in text_list:
            path1, path2, text1 = line.split(delimiter)
            image1_list.append(self.load_image(path1))
            image2_list.append(self.load_image(path2))
            prompt_list.append(text1)
        return image1_list, image2_list, prompt_list

    @staticmethod
    def load_image(image_path):
        i = Image.open(image_path)
        i = ImageOps.exif_transpose(i)
        image = i.convert("RGB")
        image = np.array(image).astype(np.float32) / 255.0
        return torch.from_numpy(image)[None,]
