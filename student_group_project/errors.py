class GroupLimitError(Exception):

    def __init__(self, message="Кількість студентів у групі не може перевищувати 10"):
        self.message = message
        super().__init__(self.message)
