import requests


class CheckIp:
    URL = "https://checkip.amazonaws.com"
    TIMEOUT_SECS = 5

    def check(self) -> str:
        try:
            response = requests.get(url=self.URL, timeout=self.TIMEOUT_SECS)
            return response.content.decode("utf8").strip()
        except (requests.ConnectionError, requests.Timeout):
            raise self.NoConnectivity()

    class NoConnectivity(Exception):
        pass
