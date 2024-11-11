from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        self.categories.append(category) if category not in self.categories else None

    def add_topic(self, topic: Topic) -> None:
        self.topics.append(topic) if topic not in self.topics else None

    def add_document(self, document: Document) -> None:
        self.documents.append(document) if document not in self.documents else None

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.__edit_object(document_id, self.documents, new_file_name)

    @staticmethod
    def __get_object(object_id: int, object_list):
        return [obj for obj in object_list if obj.id == object_id][0]

    def __edit_object(self, object_id, object_list, *values) -> None:
        current_object = self.__get_object(object_id, object_list)
        current_object.edit(*values)

    def __delete_object(self, object_id, object_list):
        current_object = self.__get_object(object_id, object_list)
        object_list.remove(current_object)

    def delete_category(self, category_id) -> None:
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id) -> None:
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id) -> None:
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id):
        return self.__get_object(document_id, self.documents)

    def __repr__(self):
        return "\n".join(str(docu) for docu in self.documents)
