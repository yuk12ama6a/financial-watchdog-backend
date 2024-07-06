from src.sample import Sample


class TestSample:

    def test_say_hello(self) -> None:
        actual = Sample(name="Yswd").say_hello()

        assert actual == "Hello, Yswd"
