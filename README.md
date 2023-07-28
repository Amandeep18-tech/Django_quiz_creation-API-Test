**API Documentation**

Below is the documentation for the APIs provided by the quiz application:

### Authentication

**1. User Login**

- Endpoint: `/api/login/`
- Method: POST
- Request Body:
  ```
  { 
      "username": "your_username",
      "password": "your_password"
  }
  ```
- Response:
  ```
  {
      "message": "Login successful",
      "access_token": "your_access_token",
      "user_type": "User/Admin"
  }
  ```
- Description: This endpoint allows users to log in and obtain a JWT access token for authentication.

### Quizzes

**2. List All Exams**

- Endpoint: `/api/exams/`
- Method: GET
- Description: Retrieves a list of all available exams.

**3. Create Exam (Admin Only)**

- Endpoint: `/api/exams/`
- Method: POST
- Request Body:
  ```
  {
      "name": "Exam Name"
  }
  ```
- Description: Creates a new exam. Only accessible to admin users.

**4. List All Sections**

- Endpoint: `/api/sections/`
- Method: GET
- Description: Retrieves a list of all available sections.

**5. Create Section (Admin Only)**

- Endpoint: `/api/sections/`
- Method: POST
- Request Body:
  ```
  {
      "name": "Section Name",
      "exam": "exam_id"
  }
  ```
- Description: Creates a new section under a specific exam. Only accessible to admin users.

**6. List All Topics**

- Endpoint: `/api/topics/`
- Method: GET
- Description: Retrieves a list of all available topics.

**7. Create Topic (Admin Only)**

- Endpoint: `/api/topics/`
- Method: POST
- Request Body:
  ```
  {
      "name": "Topic Name",
      "section": "section_id"
  }
  ```
- Description: Creates a new topic under a specific section. Only accessible to admin users.

**8. List All Questions**

- Endpoint: `/api/questions/`
- Method: GET
- Description: Retrieves a list of all available questions.

**9. Create Question (Admin Only)**

- Endpoint: `/api/questions/`
- Method: POST
- Request Body:
  ```
  {
      "text": "Question Text",
      "image": "image_url",
      "option1": "Option 1",
      "option2": "Option 2",
      "option3": "Option 3",
      "option4": "Option 4",
      "correct_answer": "Correct Option",
      "topic": "topic_id"
  }
  ```
- Description: Creates a new question under a specific topic. Only accessible to admin users.

**10. Attempt Quiz**

- Endpoint: `/api/attempt-quiz/`
- Method: POST
- Request Body:
  ```
  {
      "topic": "topic_id",
      "answers": {
          "question_id_1": "user_answer_1",
          "question_id_2": "user_answer_2",
          ...
      }
  }
  ```
- Response:
  ```
  {
      "message": "Quiz result saved successfully",
      "score": "percentage_correct"
  }
  ```
- Description: Allows users to attempt a quiz and calculate their score based on the provided answers.

### Users

**11. List All Users (Admin Only)**

- Endpoint: `/api/users/`
- Method: GET
- Description: Retrieves a list of all registered users. Only accessible to admin users.

**12. Create User (Admin Only)**

- Endpoint: `/api/users/`
- Method: POST
- Request Body:
  ```
  {
      "username": "username",
      "password": "password"
  }
  ```
- Description: Creates a new user with the given username and password. Only accessible to admin users.

**Note**: All endpoints marked as "Admin Only" require an access token obtained through user authentication with admin privileges.

---

Please note that the API documentation assumes the use of JWT for user authentication and user permissions based on admin status. Ensure you have the necessary authentication tokens for accessing admin-only endpoints. The provided views and serializers are utilized to implement these APIs, allowing for user authentication, quiz management, and user score tracking.

These are all APIs :

1. User APIs:
   - `POST /api/users/`: Create a new user.
   - `GET /api/users/`: List all users.
   - `GET /api/users/{user_id}/`: Retrieve a specific user.
   - `PUT /api/users/{user_id}/`: Update a specific user.
   - `DELETE /api/users/{user_id}/`: Delete a specific user.

2. User Authentication APIs:
   - `POST /api/login/`: User login (to obtain an authentication token).

3. Attempt Quiz API:
   - `POST /api/attempt-quiz/`: Attempt quiz (select exam, section, and get a list of quiz questions).

4. Quiz Result API:
   - This API has not been implemented yet in the provided examples.

5. Admin APIs:
   - `POST /api/exams/`: Create a new exam.
   - `GET /api/exams/`: List all exams.
   - `GET /api/exams/{exam_id}/`: Retrieve a specific exam.
   - `PUT /api/exams/{exam_id}/`: Update a specific exam.
   - `DELETE /api/exams/{exam_id}/`: Delete a specific exam.
   - `POST /api/sections/`: Create a new section.
   - `GET /api/sections/`: List all sections.
   - `GET /api/sections/{section_id}/`: Retrieve a specific section.
   - `PUT /api/sections/{section_id}/`: Update a specific section.
   - `DELETE /api/sections/{section_id}/`: Delete a specific section.
   - `POST /api/questions/`: Create a new question.
   - `GET /api/questions/`: List all questions.
   - `GET /api/questions/{question_id}/`: Retrieve a specific question.
   - `PUT /api/questions/{question_id}/`: Update a specific question.
   - `DELETE /api/questions/{question_id}/`: Delete a specific question.
   - `POST /api/login-logs/`: Create a new login log.
   - `GET /api/login-logs/`: List all login logs.
   - `GET /api/login-logs/{login_log_id}/`: Retrieve a specific login log.
   - `PUT /api/login-logs/{login_log_id}/`: Update a specific login log.
   - `DELETE /api/login-logs/{login_log_id}/`: Delete a specific login log.
   - `POST /api/create-quiz/`: Create a new quiz topic-wise according to exam and section.

