from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'route': '/api/get_todos/',
            'description': 'Get all the todo objects.'
        },
        {
            'route': '/api/get_todo/:pk/',
            'description': 'Get the todo related to the pk (primary key) passed into the url.'
        },
        {
            'route': '/aoi/add_todo/',
            'description': 'It will add a todo to the database'
        },
        {
            'route': '/api/update_todo/',
            'description': 'It will update a single todo the database'
        },
        {
            'route': '/api/delete_todo/',
            'description': 'It will delete a single todo from the database'
        }
    ]
    return Response({'routes': routes})

@api_view(['GET'])
def get_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response({'todos': serializer.data})

@api_view(['GET'])
def get_todo(request, pk):
    todo = Todo.objects.filter(id=pk).first()
    serializer = TodoSerializer(todo, many=False)
    return Response({'todo': serializer.data})

def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        if not title or not description:
            return JsonResponse({"message": "Title or description cannot be blank!", "status": "error"})
        
        elif len(title) < 5 or len(description) < 5:
            return JsonResponse({"message": "Title or description cannot be under 5 characters!", "status": "error"})

        else:
            todo = Todo(title=title, description=description)
            todo.save()
            return JsonResponse({"message": "Your todo has been added successfully!", "status": "success"})

    else:
        return JsonResponse({"BadRequest": {"status": 400, "requestType": request.method}, "message": "{} method is not allowed on this url!".format(request.method)})

def update_todo(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        title = request.POST.get("title")
        description = request.POST.get("description")

        if not title or not description:
            return JsonResponse({"message": "Title or description cannot be blank!", "status": "error"})
        
        elif len(title) < 5 or len(description) < 5:
            return JsonResponse({"message": "Title or description cannot be under 5 characters!", "status": "error"})

        else:
            todo = Todo.objects.filter(id=todo_id).first()
            todo.title = title
            todo.description = description
            todo.save()
            return JsonResponse({"message": "Your todo has been updated successfully!", "status": "success"})

    else:
        return JsonResponse({"BadRequest": {"status": 400, "requestType": request.method}, "message": "{} method is not allowed on this url!".format(request.method)})

def delete_todo(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        todo = Todo.objects.filter(id=todo_id).first()
        todo.delete()
        return JsonResponse({"message": "Your todo has been deleted successfully!", "status": "success"})

    else:
        return JsonResponse({"BadRequest": {"status": 400, "requestType": request.method}, "message": "{} method is not allowed on this url!".format(request.method)})