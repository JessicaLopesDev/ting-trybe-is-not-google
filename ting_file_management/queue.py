from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def contain(self, value):
        return any(file["nome_do_arquivo"] == value for file in self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        if len(self.__data) == 0:
            raise IndexError("Empty")
        return self.__data.pop(0)

    def search(self, index):
        if index not in range(len(self.__data)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.__data[index]
