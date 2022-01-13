# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from place_context.protos import place_pb2 as place__context_dot_protos_dot_place__pb2


class PlaceContextStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPlace = channel.unary_unary(
            "/PlaceContext/GetPlace",
            request_serializer=place__context_dot_protos_dot_place__pb2.Place.SerializeToString,
            response_deserializer=place__context_dot_protos_dot_place__pb2.Place.FromString,
        )


class PlaceContextServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPlace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PlaceContextServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetPlace": grpc.unary_unary_rpc_method_handler(
            servicer.GetPlace,
            request_deserializer=place__context_dot_protos_dot_place__pb2.Place.FromString,
            response_serializer=place__context_dot_protos_dot_place__pb2.Place.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "PlaceContext", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PlaceContext(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPlace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/PlaceContext/GetPlace",
            place__context_dot_protos_dot_place__pb2.Place.SerializeToString,
            place__context_dot_protos_dot_place__pb2.Place.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
