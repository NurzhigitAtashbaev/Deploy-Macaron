from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Table
from .serializers import TableSerializer, TableBuySerializer


class TableListView(generics.ListAPIView):
    queryset = Table.objects.filter(busy=True)
    serializer_class = TableSerializer


class TableDetailView(generics.RetrieveUpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableBuySerializer
    lookup_field = 'number'

    def perform_update(self, serializer):
        table = self.get_object()

        if table.busy == False:

            serializer.save(busy=True)
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
        number = kwargs.get("number")
        table = Table.objects.get(number=number)
        table.busy = False
        table.visitor_name = None
        table.visitor_number = None
        table.start_time = None
        table.message = " "
        table.save()

        return Response({"message": f"Table {number} cleared and set to available"})


class AdminCreateTable(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TableSerializer
