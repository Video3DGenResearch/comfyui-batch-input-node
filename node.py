class BatchInputText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_list": ("STRING", {
                    "multiline": True,
                    "default": "apple\nbanana\ncherry\norange\nkiwi\npear\npineapple\nmelon",
                }),
                "delimiter": ("STRING", {
                    "default": ", "
                }),
                "batch_size": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 64,
                    "step": 1,
                    "display": "number"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "split"
    OUTPUT_NODE = False
    CATEGORY = "🐳BatchInput"
    OUTPUT_IS_LIST = (True, )

    def split(self, text_list, join_tag, batch_size):
        text_list = text_list.split("\n")
        text_batch = [join_tag.join(text_list[i:i + batch_size]) for i in range(0, len(text_list), batch_size)]
        return (text_batch,)


class BatchInputCSV:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_list": ("STRING", {
                    "multiline": True,
                    "default": "./data/v11.mp4,./data/v12.mp4,apple\n./data/v21.mp4,./data/v22.mp4,banana"
                }),
                "delimiter": ("STRING", {
                    "default": ","
                })
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("video1", "video2", "prompt")

    FUNCTION = "split"
    OUTPUT_NODE = False
    CATEGORY = "🐳BatchInput"
    OUTPUT_IS_LIST = (True, True, True)

    def split(self, text_list, delimiter):
        text_list = text_list.split("\n")
        text1_list = []
        text2_list = []
        text3_list = []
        for line in text_list:
            text1, text2, text3 = line.split(delimiter)
            text1_list.append(text1)
            text2_list.append(text2)
            text3_list.append(text3)
        return text1_list, text2_list, text3_list


NODE_CLASS_MAPPINGS = {
    "BatchInputText": BatchInputText,
    "BatchInputCSV": BatchInputCSV,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BatchInputText": "📝Batch input text",
    "BatchInputCSV": "📝Batch input CSV",
}
