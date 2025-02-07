from dataclasses import dataclass
from typing import List

@dataclass
class DocumentationTemplate:
    version: str
    sections: List[dict]

class TemplateRegistry:
    def __init__(self):
        self.templates = {}

    def register_template(self, name: str, template: DocumentationTemplate):
        self.templates[name] = template

    def get_template(self, name: str) -> DocumentationTemplate:
        return self.templates.get(name)
