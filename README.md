# Info
- simple TO DO webapp in python django
- WIP
- nothing usefule yet

# initialize database
- `python manage.py shell`
```python
from todo.models import Status
Status.objects.create(status_text="BackLog").save()
Status.objects.create(status_text="InProgress").save()
Status.objects.create(status_text="Done").save)
from todo.models import List
List.objects.create(list_text="FoodList").save()
List.objects.create(list_text="BookList").save()
List.objects.create(list_text="SynthList").save()
```
# usage:
- `python manage.py runserver`
