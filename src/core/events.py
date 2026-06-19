class EventManager:

    def __init__(self):
        self.events = {}

    def register(self, event, callback):
        self.events.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        for callback in self.events.get(event, []):
            callback(*args, **kwargs)