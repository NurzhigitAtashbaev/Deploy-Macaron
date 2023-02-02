from django.urls import path
from .views import TableListView, TableDetailView, AdminClearAllTables, AdminCreateTable

urlpatterns = [
    path('list/', TableListView.as_view(), name='table_booking'),
    path('buy/<int:number>/', TableDetailView.as_view(), name='buy_table'),
    path('create/', AdminCreateTable.as_view(), name='create-table'),
    path('clear/<int:number>/', AdminClearAllTables.as_view(), name='clear-tables')
]
