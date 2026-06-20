import secrets
import string


class PasswordGenerator:

    def generate(
        self,
        length=16,
        uppercase=True,
        lowercase=True,
        numbers=True,
        symbols=True
    ):

        characters = ""

        if uppercase:
            characters += string.ascii_uppercase

        if lowercase:
            characters += string.ascii_lowercase

        if numbers:
            characters += string.digits

        if symbols:
            characters += "!@#$%^&*()-_=+[]{}<>?"

        if not characters:
            raise ValueError(
                "At least one character set must be selected."
            )

        return "".join(
            secrets.choice(characters)
            for _ in range(length)
        )