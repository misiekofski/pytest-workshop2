class HtmlFormatter:
    def __init__(self, text):
        self.text = text

    def bold(self):
        return f"<b>{self.text}</b>"

    def italic(self):
        return f"<i>{self.text}</i>"

    def deleted(self):
        return f"<del>{self.text}</del>"

    def custom_tag(self, tag):
        return f"<{tag}>{self.text}</{tag}>"
