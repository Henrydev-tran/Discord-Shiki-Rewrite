import asyncio
import threading

class Cooldown:
    def __init__(self, _seconds, _callback):
        self.wait_limit = _seconds
        self._wait_until_done = self.wait_limit
        self._callback = _callback
        self._wait_temp = self._wait_until_done
        self.disabled = False

    def enable(self, restart):
        self.restart()
        self.disabled = False
        if restart:
            self.start()
    
    async def _wait(self):
        if self._wait_until_done > 0:
            await asyncio.sleep(1)

        self._wait_until_done -= 1

    def restart(self):
        self._wait_until_done = self.wait_limit
        self._wait_temp = self._wait_until_done

    def alive(self):
        return self._wait_until_done > 1 or self.disabled

    def start(self):
        if self.disabled:
            return

        def start_wait():
            wait = asyncio.new_event_loop()
            asyncio.set_event_loop(wait)

            wait.run_until_complete(self._wait())
            wait.close()

            if self._wait_until_done != self._wait_temp:
                self._wait_temp = self._wait_until_done
                self.start()
                return

        if self._wait_until_done > 0:
            _thread = threading.Thread(target=start_wait)
            _thread.start()

        if self._wait_until_done == 0:
            self._callback()
            self.disabled = True