from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Table
from .serializers import TableSerializer, TableBuySerializer


class TableListView(generics.ListAPIView):
    queryset = Table.objects.filter(busy=False)
    serializer_class = TableSerializer


class TableDetailView(generics.RetrieveUpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableBuySerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        table = self.get_object()
        if table.busy == False:
            serializer.save()
        else:
            raise Exception("Table is not available")

    def get_object(self):
        table = super().get_object()
        if table.busy:
            raise Http404("Table is not available")
        return table


class AdminClearAllTables(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        tables = Table.objects.all()
        tables.update(busy=False, visitor_name=None, visitor_number=None, start_time=None)
        return Response({"message": "All tables cleared and set to available"})


class AdminCreateTable(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TableSerializer
