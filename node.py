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


NODE_CLASS_MAPPINGS = {
    "BatchInputText": BatchInputText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BatchInputText": "📝Batch input text",
}
