class ContextManager:
    def __enter__(self) -> None:
        pass

    def __exit__(self, *exc) -> None:
        pass


async def foo() -> None:
    async with ContextManager():  # [not-async-context-manager]
        pass
