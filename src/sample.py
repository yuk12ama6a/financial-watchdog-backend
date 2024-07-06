class Sample:
    def __init__(self, name: str) -> None:
        self.__name = name

    def say_hello(self) -> str:
        return f"Hello, {self.__name}"
