import time


class Sleep:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("image", {}),
                "seconds": ("FLOAT", {"default": 60.0, "min": 0.0, "step": 60.0}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    CATEGORY = "utils"
    FUNCTION = "sleep"

    def sleep(self, image, seconds):
        time.sleep(seconds)
        return (image,)
