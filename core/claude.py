from anthropic import Anthropic


class Claude:
    def __init__(self, model: str) -> None:
        self.client = Anthropic()
        self.model = model 


