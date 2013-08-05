class SimpleChangeList():
    def __init__(self, request, model, list_display):
        self.model = model
        self.list_display = list_display
