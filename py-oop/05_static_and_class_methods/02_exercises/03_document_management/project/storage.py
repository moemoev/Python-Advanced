from project.topic import Topic
from project.document import Document
from project.category import Category

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __get_obj_by_id(self, obj_id: int, obj_list: list):
        for obj in obj_list:
            if obj.id == obj_id:
                return obj

        return None

    def add_category(self, category: Category):
        obj = self.__get_obj_by_id(category.id, self.categories)
        if not obj:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        obj = self.__get_obj_by_id(topic.id, self.topics)
        if not obj:
            self.topics.append(topic)

    def add_document(self, document: Document):
        obj = self.__get_obj_by_id(document.id, self.documents)
        if not obj:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        obj = self.__get_obj_by_id(category_id, self.categories)
        obj.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        obj = self.__get_obj_by_id(topic_id, self.topics)
        obj.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        obj = self.__get_obj_by_id(document_id, self.documents)
        obj.edit(new_file_name)

    def delete_category(self, category_id: int):
        obj = self.__get_obj_by_id(category_id, self.categories)
        self.categories.remove(obj)

    def delete_topic(self, topic_id: int):
        obj = self.__get_obj_by_id(topic_id, self.topics)
        self.topics.remove(obj)

    def delete_document(self, document_id: int):
        obj = self.__get_obj_by_id(document_id, self.documents)
        self.documents.remove(obj)

    def get_document(self, document_id: int):
        return self.__get_obj_by_id(document_id, self.documents)

    def __repr__(self):
        result = '\n'.join(str(doc) for doc in self.documents)

        return result