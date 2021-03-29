from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Chat
from chat.serializers import ChatSerializer, ChatCreateSerializer, ChatUpdateSerializer
from chat.service import PaginationMovies


class MessageListView(generics.ListAPIView):
    """ List of messages """
    queryset = Chat.objects.all().order_by('-created_date')
    serializer_class = ChatSerializer
    pagination_class = PaginationMovies


class MessageDetailView(generics.RetrieveAPIView):
    """ Show specific message"""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageCreateView(generics.CreateAPIView):
    """Create message"""

    serializer_class = ChatCreateSerializer


class MessageUpdateView(generics.UpdateAPIView):
    """Create message"""
    queryset = Chat.objects.all()
    serializer_class = ChatUpdateSerializer

# class Chatter(APIView):
#     """Chat dialog"""
#
#     def get(self, request):
#         chats = Chat.objects.all()
#         serializer = ChatSerializer(chats, many=True)
#         return Response({"data": serializer.data})

#     def post(self, request):
#         # room = request.data.get("room")
#         chat = ChatCreateSerializer(data=request.data)
#         if chat.is_valid():
#             chat.save(username=request.data['username'])
#             return Response(status=200)
#         else:
#             return Response(status=400)
