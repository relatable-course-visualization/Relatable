import requests
import environ


env = environ.Env()
environ.Env.read_env()


def postTest():
        requests.post(f"{env('SERVER_URL')}/postTest", data={'name': 'Fraser', 'favColour': 'Blue', 'favNumber': 8})
        

postTest()