from project.topic import Topic
from project.category import Category

class Document:
    def __init__(self, doc_id: int, category_id: int, topic_id: int, file_name: str):
        self.id = doc_id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, doc_id: int, category: Category, topic: Topic, file_name: str):
        return cls(doc_id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        if tag_content in self.tags:
            return

        self.tags.append(tag_content)
        return

    def remove_tag(self, tag_content: str):
        if tag_content not in self.tags:
            return

        self.tags.remove(tag_content)
        return

    def edit(self, new_file_name: str):
        self.file_name = new_file_name

    def __repr__(self):
        result = f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {', '.join(self.tags)}"
        return result
