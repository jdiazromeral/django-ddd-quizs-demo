from django.urls import path

from service.infrastructure.controllers.all_quiz_finder_controller import AllQuizFinderController
from service.infrastructure.controllers.all_quiz_finder_mongo_controller import (
    AllQuizFinderMongoController,
)
from service.infrastructure.controllers.create_quiz_controller import CreateQuizController
from service.infrastructure.controllers.create_quiz_mongo_controller import CreateQuizMongoController

urlpatterns = [
    path("all", AllQuizFinderController.as_view(), name="all"),
    path("all_mongo", AllQuizFinderMongoController.as_view(), name="all_mongo"),
    path("create", CreateQuizController.as_view(), name="create"),
    path("create_mongo", CreateQuizMongoController.as_view(), name="create__mongo"),
]
