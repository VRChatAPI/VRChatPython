from vrcpy.objects import *

class Avatar(Avatar):
    async def author(self):
        resp = await self.client.api.call("/users/"+self.authorId)
        self.client._raise_for_status(resp)
        return User(self.client, resp["data"])

## World

class LimitedWorld(LimitedWorld):
    async def author(self):
        resp = await self.client.api.call("/users/"+self.authorId)
        self.client._raise_for_status(resp)
        return User(self.client, resp["data"])