"""``async``/``await`` and coroutines — concurrency without threads."""

import asyncio

from runner.koan import Koan, __


class AboutAsync(Koan):

    def test_coroutine_function_returns_a_coroutine(self):
        async def hello():
            return "hello"
        # Calling it does not run the body.
        coro = hello()
        self.assertEqual(__, type(coro).__name__)
        # Close it to avoid a "never awaited" warning.
        coro.close()

    def test_running_a_coroutine_with_asyncio_run(self):
        async def hello():
            return "hello"
        self.assertEqual(__, asyncio.run(hello()))

    def test_awaiting_within_a_coroutine(self):
        async def inner():
            return 21
        async def outer():
            x = await inner()
            return x * 2
        self.assertEqual(__, asyncio.run(outer()))

    def test_gather_runs_concurrently(self):
        async def value(n):
            await asyncio.sleep(0)  # yield to the loop
            return n
        async def main():
            return await asyncio.gather(value(1), value(2), value(3))
        self.assertEqual(__, asyncio.run(main()))

    def test_async_for_iterates_async_iterator(self):
        class Counter:
            def __init__(self, n):
                self.n = n
                self.i = 0
            def __aiter__(self):
                return self
            async def __anext__(self):
                if self.i >= self.n:
                    raise StopAsyncIteration
                self.i += 1
                return self.i

        async def collect():
            out = []
            async for v in Counter(3):
                out.append(v)
            return out

        self.assertEqual(__, asyncio.run(collect()))

    def test_async_context_manager(self):
        class Tracer:
            def __init__(self, log):
                self.log = log
            async def __aenter__(self):
                self.log.append("enter")
                return self
            async def __aexit__(self, *exc):
                self.log.append("exit")
                return False

        async def run():
            log = []
            async with Tracer(log):
                log.append("body")
            return log

        self.assertEqual(__, asyncio.run(run()))
