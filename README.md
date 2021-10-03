# Quiz 

To build the project

```
docker-compose up -d --build api
```


## Considerations
This repo is a sample for the package Django-ddd
(package here https://github.com/jdiazromeral/django-ddd).
This package is a proof of concept to adapt Django apps folder structure to something
more like hexagonal architecture.

Project is build using docker-compose, so we don't need to set a local environment; we can
directly use the one provided by docker-compose and docker.

All the code is in the ```src``` folder, under the ```service``` context. You can 
find entities, repository definitions, exceptions and business validation rules under ```domain```, 
application services for the different features under ```application``` and all infrastructure related stuff, 
mainly API controllers, in memory and mongodb repositories, under ```infrastructure```.

Each endpoint is listed in ```config/urls.py``` file.

### Domain Model
You can find all the domain definitions under ```service/domain```. Main entities are:
- Quiz
- Question
- Answers

### Database
Added two samples:
- In memory repository
- MongoDB repository (sorry, a bit quick and dirty one) using PyMongo

In the future we will add one using Django models. 

### API

We can retrieve all quizs available with a get call to http://localhost:8000/all

We can create quizs with a post call to: http://localhost:8000/create

Sample calls:
```
curl --location --request GET 'http://localhost:8000/all
or 
curl --location --request GET 'http://localhost:8000/all_mongo
```

Response
```
[
    {
        "id": "d8a13304-d815-4db4-b801-efb3f91d55f3",
        "title": "quiz title",
        "description": "quiz description",
        "type": "quiz type",
        "time": 10,
        "questions": [
            {
                "id": "a201429b-35d9-469c-9af1-125359d7d76e",
                "text": "text question",
                "skill": "LISTENING",
                "answers": {
                    "ff83bc63-cd97-453a-b9b1-287522ad00b1": {
                        "id": "ff83bc63-cd97-453a-b9b1-287522ad00b1",
                        "text": "answer text",
                        "question_id": "a201429b-35d9-469c-9af1-125359d7d76e"
                    },
                    "f099b566-7615-40a8-8a7b-1f5c174083c1": {
                        "id": "f099b566-7615-40a8-8a7b-1f5c174083c1",
                        "text": "answer text",
                        "question_id": "a201429b-35d9-469c-9af1-125359d7d76e"
                    }
                },
                "correct_answer": [
                    "ff83bc63-cd97-453a-b9b1-287522ad00b1"
                ],
                "quiz": "d8a13304-d815-4db4-b801-efb3f91d55f3"
            }
        ]
    }
]
```


To create you can use `create` or `create_mongo`:
```
curl --location --request POST 'http://localhost:8000/create \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "d8a13304-d815-4db4-b801-efb3f91d55f3",
    "title": "quiz title",
    "description": "quiz description",
    "type": "quiz type",
    "time": 10,
    "questions": [
        {
            "id": "a201429b-35d9-469c-9af1-125359d7d76e",
            "text": "text question",
            "skill": "LISTENING",
            "answers": [
                {
                    "id": "ff83bc63-cd97-453a-b9b1-287522ad00b1",
                    "text": "answer text",
                    "question_id": "a201429b-35d9-469c-9af1-125359d7d76e"
                },
                {
                    "id": "f099b566-7615-40a8-8a7b-1f5c174083c1",
                    "text": "answer text",
                    "question_id": "a201429b-35d9-469c-9af1-125359d7d76e"
                }
            ],
            "correct_answer": ["ff83bc63-cd97-453a-b9b1-287522ad00b1"],
            "quiz_id": "d8a13304-d815-4db4-b801-efb3f91d55f3"
        }
    ]
}'
```




