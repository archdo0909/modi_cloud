# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import modi_ai_cloud_pb2 as modi__ai__cloud__pb2


class Data_Model_HandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendObjects = channel.unary_unary(
                '/modi_cloud.Data_Model_Handler/SendObjects',
                request_serializer=modi__ai__cloud__pb2.ObjectsSend.SerializeToString,
                response_deserializer=modi__ai__cloud__pb2.ModelReply.FromString,
                )
        self.SendObjectsAgain = channel.unary_unary(
                '/modi_cloud.Data_Model_Handler/SendObjectsAgain',
                request_serializer=modi__ai__cloud__pb2.ObjectsSend.SerializeToString,
                response_deserializer=modi__ai__cloud__pb2.ModelReply.FromString,
                )
        self.TransferComplete = channel.unary_unary(
                '/modi_cloud.Data_Model_Handler/TransferComplete',
                request_serializer=modi__ai__cloud__pb2.TransferCompleteSend.SerializeToString,
                response_deserializer=modi__ai__cloud__pb2.TransferCompleteReply.FromString,
                )
        self.LearningComplete = channel.unary_unary(
                '/modi_cloud.Data_Model_Handler/LearningComplete',
                request_serializer=modi__ai__cloud__pb2.LearningCompleteSend.SerializeToString,
                response_deserializer=modi__ai__cloud__pb2.LearningCompleteReply.FromString,
                )


class Data_Model_HandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendObjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendObjectsAgain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferComplete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LearningComplete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Data_Model_HandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.SendObjects,
                    request_deserializer=modi__ai__cloud__pb2.ObjectsSend.FromString,
                    response_serializer=modi__ai__cloud__pb2.ModelReply.SerializeToString,
            ),
            'SendObjectsAgain': grpc.unary_unary_rpc_method_handler(
                    servicer.SendObjectsAgain,
                    request_deserializer=modi__ai__cloud__pb2.ObjectsSend.FromString,
                    response_serializer=modi__ai__cloud__pb2.ModelReply.SerializeToString,
            ),
            'TransferComplete': grpc.unary_unary_rpc_method_handler(
                    servicer.TransferComplete,
                    request_deserializer=modi__ai__cloud__pb2.TransferCompleteSend.FromString,
                    response_serializer=modi__ai__cloud__pb2.TransferCompleteReply.SerializeToString,
            ),
            'LearningComplete': grpc.unary_unary_rpc_method_handler(
                    servicer.LearningComplete,
                    request_deserializer=modi__ai__cloud__pb2.LearningCompleteSend.FromString,
                    response_serializer=modi__ai__cloud__pb2.LearningCompleteReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'modi_cloud.Data_Model_Handler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Data_Model_Handler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modi_cloud.Data_Model_Handler/SendObjects',
            modi__ai__cloud__pb2.ObjectsSend.SerializeToString,
            modi__ai__cloud__pb2.ModelReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendObjectsAgain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modi_cloud.Data_Model_Handler/SendObjectsAgain',
            modi__ai__cloud__pb2.ObjectsSend.SerializeToString,
            modi__ai__cloud__pb2.ModelReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransferComplete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modi_cloud.Data_Model_Handler/TransferComplete',
            modi__ai__cloud__pb2.TransferCompleteSend.SerializeToString,
            modi__ai__cloud__pb2.TransferCompleteReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LearningComplete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modi_cloud.Data_Model_Handler/LearningComplete',
            modi__ai__cloud__pb2.LearningCompleteSend.SerializeToString,
            modi__ai__cloud__pb2.LearningCompleteReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
