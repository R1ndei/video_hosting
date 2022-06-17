## VIDEO HOSTING API

This is a REST API for a Video hosting service built for fun and learning with FastAPI, Ormar and Sqlite3.


## ROUTES TO IMPLEMENT

| METHOD   | ROUTE                         | FUNCTIONALITY            | ACCESS       |
|----------|-------------------------------|--------------------------|--------------|
| *GET*    | ```/```                       | _Google auth_            | _All users_  |
| *POST*   | ```/google/auth```            | _Google auth_            | _All users_  |
| *POST*   | ```/video```                  | _Create video_           | _Auth users_ |
| *GET*    | ```/video/user/{user_name}``` | _Get List Video_         | _Auth users_ |
| *GET*    | ```/video/index/{video_pk}``` | _Get Video_              | _Auth users_ |
| *GET*    | ```/video/video/{video_pk}``` | _Get Streaming Video_    | _Auth users_ |
| *GET*    | ```/video/404```              | _Error 404_              | _All users_  |
| *POST*   | ```/video/{video_pk}```       | _Add like_               | _Auth users_ |
| *GET*    | ```/followers/```             | _My list Following_      | _Auth users_ |
| *POST*   | ```/followers/```             | _Add Follower_           | _Auth users_ |
| *DELETE* | ```/followers/{username}```   | _Delete Follower_        | _Auth users_ |
| *GET*    | ```/followers/me```           | _My List Follower_       | _Auth users_ |

## How to run the Project

- Install Python
- Git clone the project with ``` git clone https://github.com/R1ndei/video_hosting.git```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```
- Create you database with `uvicorn main:app`
- Finally run the API
  ``` uvicorn main:app ```
