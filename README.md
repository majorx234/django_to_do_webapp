# Info
- simple TO DO webapp in python django
- WIP
- nothing usefule yet

# initialize database
- change dir: `todo\todo_manager`
- init: `python manage.py migrate`
- `python manage.py shell`
```python
from todo.models import Status
Status.objects.create(status_text="BackLog").save()
Status.objects.create(status_text="InProgress").save()
Status.objects.create(status_text="Done").save()
from todo.models import List
List.objects.create(list_text="FoodList").save()
List.objects.create(list_text="BookList").save()
List.objects.create(list_text="SynthList").save()
```
# usage:
- `python manage.py runserver`

# Test
## Rest - interface
- `curl -X 'GET' 'http://localhost:8000/todo/rest-list'`
- `curl -X 'GET' 'http://localhost:8000/todo/rest-detail/1`
