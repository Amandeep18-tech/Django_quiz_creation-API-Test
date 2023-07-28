from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import Exam, Section, Question, MyUser, LoginLog,Topic
from .serializers import ExamSerializer, SectionSerializer, QuestionSerializer, UserSerializer, LoginLogSerializer, TopicSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        # Extract username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        if not username or not password:
            return Response({'message': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Hash the password
        hashed_password = make_password(password)

        # Create the MyUser with the hashed password
        user = MyUser.objects.create(username=username, password=hashed_password)

        # Serialize the created user and return the response
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginLogViewSet(viewsets.ModelViewSet):
    queryset = LoginLog.objects.all()
    serializer_class = LoginLogSerializer
    
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Create a login log when the user successfully logs in
            user_type = "Admin" if user.is_staff else "User"
            LoginLog.objects.create(user=user, user_type=user_type)

            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Include token in the response
            data = {
                'message': 'Login successful',
                'access_token': access_token,
                'user_type': user_type,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CreateQuizView(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]

    def post(self, request):
        text = request.data.get('text')
        option1 = request.data.get('option1')
        option2 = request.data.get('option2')
        option3 = request.data.get('option3')
        option4 = request.data.get('option4')
        correct_answer = request.data.get('correct_answer')
        topic_id = request.data.get('topic')
        print(topic_id)
        image = request.data.get('image')  # Assuming you will send the image file along with the request

        try:
            topic = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            return Response({'message': 'Invalid topic'}, status=status.HTTP_404_NOT_FOUND)
        

        question_data = {
            'text': text,
            'topic': topic_id,
            'image': image,
            'option1':option1,
            'option2':option2,
            'option3':option3,
            'option4':option4,
            'correct_answer':correct_answer,
        }
        question_serializer = QuestionSerializer(data=question_data)

        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttemptQuizView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user  # This will give you the authenticated user
        topic_id = request.data.get('topic')
        user_answers = request.data.get('answers', {})
        if not user_answers:
            return Response({'message': 'No answers provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Get all the questions related to the quiz (topic) attempted by the user
        quiz_questions = Question.objects.filter(topic=topic_id)

        # Calculate the user's score by comparing their answers with the correct answers
        correct_answers = 0
        total_questions_attempted = 0

        for question in quiz_questions:
            question_id = question.id
            user_answer = user_answers.get(str(question_id))
            if user_answer is not None and str(user_answer) == question.correct_answer:
                correct_answers += 1

            total_questions_attempted += 1

        # Calculate the percentage of correct answers
        percentage_correct = (correct_answers / total_questions_attempted) * 100

        # Store the user's score in the user table (assuming you have a field named 'quiz_score' in your MyUser model)
        try:
            user.quiz_score = percentage_correct
            user.save()
            return Response({'message': 'Quiz result saved successfully', 'score': percentage_correct}, status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

