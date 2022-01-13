from src.generated.place_context.protos import place_pb2_grpc, place_pb2


class PlaceServicer(place_pb2_grpc.PlaceContextServicer):
    def get_place(self, _request, _context) -> place_pb2.Place:
        return place_pb2.Place(value=1.234)
