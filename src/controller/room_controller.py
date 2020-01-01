from random import Random

from src.model import Room


class RoomController:


    def get_list(self):
        room= Room()
        rooms= room.select().dicts().execute()
        data = []
        for i in rooms:
            data.append(i)
        return {"success": True, "rooms": data}
