from pydantic.dataclasses import dataclass

@dataclass
class Foo:
    bar: str


if __name__ == "__main__":
    print(Foo(bar="hello"))
    print(Foo(bar="hello", not_valid="huh"))
