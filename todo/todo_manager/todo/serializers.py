from rest_framework import serializers

from todo.models import Status, List, Task

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id',
                   'status_text',
                  )

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id'
                  'list_text')

class TaskSerializer(serializers.ModelSerializer):
    status = StatusSerializer(
        many=False,
        read_only==True
    )
    list_items = StatusSerializer(
        many=False,
        read_only==True
    )
    class Meta:
        model = Task
        fields = ('id',
                  'shorttext'
                  'longtext'
                  'till_when_date'
                  'list_items'
                  'status')
