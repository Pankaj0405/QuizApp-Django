# Quiz-Django App

## Current Features

### Site access features:

- User must be logged in to access the Quiz.
- For signup user is required to give _username_, _first name_, _last name_, _e-mail address_ and _password_.
- For login the user will be required to enter _username_ only.

### Features of the quiz:

- All questions are multiple choice question.
- Live Quiz app
- Each question is displayed only once per user.
- Questions are displayed randomly for every user.
- If the user by-mistake presses refresh or go back to the previous page, there will be a new question for the user and the
  question he/she was on will be marked as attempted.
- A message will be displayed after every attempted question whether the answer was correct or incorrect
- Rozarpay Integration

### Leaderboard features:

- Leaderboard is a shorted list according to the score obtained by the users.
- If two users are having same score, the user who has signed up earlier will have good ranking than the one who joined late.

### Administrative features:

- Only admin can add questions.
- Admin can add questions and modify them until they are not marked as _Has been published?_
- Once a question has been published, it can neither be modified nor can be accessed. Admin can only see a list of questions.
- Admin can search questions by question text or choice text.
- Admin can filter questions based on whether the questions have been published or not.

### 1. Clone this repository

```bash
git clone https://github.com/akashgiricse/lets-quiz.git
cd lets_quiz
```

### 2. Install [Pipenv](https://pipenv.pypa.io/en/latest/)

### 3. Create the virtualenv

```bash
## run following command from `lets_quiz` directory
pipenv shell
```

### 4. Install python packages

```bash
pip install -r requirements.txt
```

### 5. Setup the database

_TODO - Add instructions for this when I start using MySQL database._

### 6. Run database migrations

```bash
cd lets_quiz
python manage.py migrate
```

### 7. Create superuser

```bash
python manage.py createsuperuser

```

### 8. Run development server

```bash
python manage.py runserver
```

## ScreenShot
<img src="https://github.com/Pankaj0405/QuizApp-Django/assets/91046820/0145da7c-6a42-42fc-a961-02e698ba6fda" height="360" width="560">
<img src="https://github.com/Pankaj0405/QuizApp-Django/assets/91046820/3f72b023-7966-48c0-965c-13a1c5071d24" height="760" width="360">
<img src="https://github.com/Pankaj0405/QuizApp-Django/assets/91046820/2476ea9f-3e1b-477e-876f-de27b36df937" height="760" width="360">
<img src="https://github.com/Pankaj0405/QuizApp-Django/assets/91046820/013d4a7e-dffb-48a3-8afc-f364597c4355" height="760" width="360">
<img src="https://github.com/Pankaj0405/QuizApp-Django/assets/91046820/7dd1d165-4574-4e79-9be9-2c006dcece14" height="760" width="360">


## Acknowledgements

 - This project was inspired by the idea of providing an interactive and educational quiz application.

- Thanks to the open-source community for providing libraries and resources that made this project possible.

## License

The QuizApp project is licensed under the MIT License.

