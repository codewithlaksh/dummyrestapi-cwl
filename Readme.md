# Dummy Rest API

This is a dummy rest api with many todos made using django. You can use this api with no cost.

### Note:-
The database will be reset every 24 hourse prior to when this project was deployed on heroku platform.

### This project is live on the following heroku platform
- [https://dummyrestapi-cwl.herokuapp.com](https://dummyrestapi-cwl.herokuapp.com)

### Usage
- The following routes of this api are accepting get requests
  - The following route can be used to get all the todos
  ```python
  /api/get_todos/
  ```
  - The following route can be used to get one todo with id in the url
  ```python
  /api/get_todo/:id
  ```

- The following routes of this api are accepting post requests
  - The following route can be used to add a todo
  ```python
  /api/add_todo/
  ```
  - The following route can be used to update one todo
  ```python
  /api/update_todo/
  ```
  - The following route can be used to delete one todo
  ```python
  /api/delete_todo/
  ```

#### Thanks for using this api