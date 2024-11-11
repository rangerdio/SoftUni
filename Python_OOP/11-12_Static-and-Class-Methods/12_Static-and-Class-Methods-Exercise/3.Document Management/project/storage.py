from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        self.categories.append(category) if category not in self.categories else None

    def add_topic(self, topic: Topic):
        self.topics.append(topic) if topic not in self.topics else None

    def add_document(self, document: Document):
        self.documents.append(document) if document not in self.documents else None

    def edit_category(self, category_id: int, new_name: str):
        category = self.get_category(category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.get_topic(topic_id)
        topic.topic, topic.storage_folder = new_topic, new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return [doc for doc in self.documents if doc.id == document_id][0]

    def get_category(self, category_id):
        return [cat for cat in self.categories if cat.id == category_id][0]

    def get_topic(self, topic_id):
        return [top for top in self.topics if top.id == topic_id][0]

    def __repr__(self):
        result = []
        result.extend(repr(document) for document in self.documents)
        return "\n".join(result)
