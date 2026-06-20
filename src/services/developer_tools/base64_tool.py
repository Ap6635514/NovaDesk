import base64

class Base64Tool:
    def encode(self, text: str):
        return base64.b64encode(
            text.encode('utf-8')
        ).decode('utf-8')

    def decode(self, text: str):
        return base64.b64decode(
            text.encode('utf-8')
        ).decode('utf-8')

