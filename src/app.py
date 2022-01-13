# app.py
from concurrent import futures
import grpc
from src.generated.place_context.protos import place_pb2_grpc
from src.place_context.servicer import PlaceServicer


class Server:
    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        place_pb2_grpc.add_PlaceContextServicer_to_server(PlaceServicer(), server)
        server.add_insecure_port("[::]:50051")
        server.start()
        server.wait_for_termination()


if __name__ == "__main__":
    Server.run()
