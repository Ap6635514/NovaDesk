import hashlib

class HashTool:
    def generate(self, text: str, algorithm: str):
        algorithm = algorithm.upper()
        algorithms = {
            "MD5": hashlib.md5,
            "SHA1": hashlib.sha1,
            "SHA256": hashlib.sha256,
            "SHA512": hashlib.sha512,
        }
        if algorithm not in algorithms:
            raise ValueError("Unsupported algorithm")
        return algorithms[algorithm](text.encode("utf-8")).hexdigest()
