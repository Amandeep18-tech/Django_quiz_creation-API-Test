from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExamViewSet, SectionViewSet, QuestionViewSet, UserViewSet, LoginLogViewSet, UserLoginView, AttemptQuizView, CreateQuizView,TopicViewSet

router = DefaultRouter()
router.register(r'exams', ExamViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'users', UserViewSet)
router.register(r'login-logs', LoginLogViewSet)
router.register(r'topics',TopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('attempt-quiz/', AttemptQuizView.as_view(), name='attempt-quiz'),
    path('create-quiz/', CreateQuizView.as_view(), name='create-quiz'),
   
    
]
