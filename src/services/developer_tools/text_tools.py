class TextTools:
    def upper(self, text):
        return text.upper()

    def lower(self, text):
        return text.lower()

    def title(self, text):
        return text.title()

    def snake(self, text):
        return "_".join(text.lower().split())

    def camel(self, text):
        words = text.split()
        if not words:
            return ""
        return words[0].lower() + "".join(
            w.capitalize()
            for w in words[1:]
        )
