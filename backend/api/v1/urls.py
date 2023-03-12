from django.urls import include, path

urlpatterns = [
    path("", include("api.v1.user.urls")),
    path("", include("api.v1.answer.urls")),
    path("", include("api.v1.explantaion.urls")),
    path("", include("api.v1.question.urls"))
]
