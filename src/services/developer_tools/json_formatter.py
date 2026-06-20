import json


class JSONFormatter:

    def pretty(self, text: str):

        obj = json.loads(text)

        return json.dumps(
            obj,
            indent=4,
            ensure_ascii=False
        )

    def minify(self, text: str):

        obj = json.loads(text)

        return json.dumps(
            obj,
            separators=(",", ":"),
            ensure_ascii=False
        )

    def validate(self, text: str):

        try:

            json.loads(text)

            return True, "✅ Valid JSON"

        except json.JSONDecodeError as e:

            return (
                False,
                f"❌ Invalid JSON\n\nLine {e.lineno}\nColumn {e.colno}\n\n{e.msg}"
            )