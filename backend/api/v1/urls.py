from django.urls import include, path

urlpatterns = [
    path("", include("api.v1.user.urls")),
    path("question/<question_id>/", include("api.v1.answer.urls")),
    path("", include("api.v1.explanation.urls")),
    path("", include("api.v1.question.urls")),
    path("", include("api.v1.submit_answer.urls")),
]
