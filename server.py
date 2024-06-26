# server.py
import aiocoap.resource as resource
import aiocoap
class AlarmResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.state = "OFF"

    async def render_put(self, request):
        self.state = request.payload
        print('Atualizar estado do alarme: %s' % self.state)
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.state)

import asyncio

def main():
    root = resource.Site()
    root.add_resource(['alarm'], AlarmResource())
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('localhost', 5683)))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
