"""Example of code."""
import typer


def hello(name: str) -> str:
    """Just an greetings example.

    Args:
        name (str): Name to greet.

    Returns:
        str: greeting message

    Examples:
        .. code:: python

            >>> hello("Roman")
            'Hello Roman!'
    """
    print(f"Hello {name}!")
    return f"Hello {name}!"


if __name__ == "__main__":
    typer.run(hello)
