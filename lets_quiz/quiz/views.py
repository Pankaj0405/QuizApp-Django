from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import QuizProfile, Question, AttemptedQuestion,Payment
from .forms import UserLoginForm, RegistrationForm
import razorpay



def home(request):
    user = request.user

    context = {}
    total_amount= 1.0
    mydata = Payment.objects.filter(user=user).values()
    if mydata.exists():
        check = "True"
    else:
        check = "False"
    client = razorpay.Client(auth=('rzp_test_TxzRfdOWgmXKmu', 'geylCeb5ycAW7X1pyhBfXLC9'))
    response_payment = client.order.create(dict(amount=total_amount * 100,
                                                currency='INR')
                                           )
    return render(request, 'quiz/home.html', {'context':context,'check':check,'totalamount':total_amount,'payment': response_payment,'mymembers': mydata})
@login_required
def payment_done(request):


 response = request.GET
 params_dict = {
  'razorpay_order_id': response['razorpay_order_id'],
  'razorpay_payment_id': response['razorpay_payment_id'],
  'razorpay_signature': response['razorpay_signature']
 }

 # client instance
 client = razorpay.Client(auth=('rzp_test_TxzRfdOWgmXKmu', 'geylCeb5ycAW7X1pyhBfXLC9'))
 user = request.user

 status = client.utility.verify_payment_signature(params_dict)
 if (status):
     mydata = Payment.objects.filter(user=user).values()
     if mydata.exists():
         record = Payment.objects.get(user=user)
         record.payment_done = status
         record.save()
         print("hello")
         return redirect('/')



     else:
         book = Payment(user=user, payment_done=status)
         book.save()
         return redirect('/')





 else:
  return render(request, 'quiz/home.html', {'status': False})

@login_required()
def user_home(request):
    user = request.user

    context = {}
    total_amount = 1.0
    mydata = Payment.objects.filter(user=user).values()
    if mydata.exists():
        check = "True"
    else:
        check = "False"
    client = razorpay.Client(auth=('rzp_test_TxzRfdOWgmXKmu', 'geylCeb5ycAW7X1pyhBfXLC9'))
    response_payment = client.order.create(dict(amount=total_amount * 100,
                                                currency='INR')
                                           )
    return render(request, 'quiz/home.html',
                  {'context': context, 'check': check, 'totalamount': total_amount, 'payment': response_payment,
                   'mymembers': mydata})


def leaderboard(request):

    top_quiz_profiles = QuizProfile.objects.order_by('-total_score')[:500]
    total_count = top_quiz_profiles.count()
    context = {
        'top_quiz_profiles': top_quiz_profiles,
        'total_count': total_count,
    }
    return render(request, 'quiz/leaderboard.html', context=context)


@login_required()
def play(request):
    p=0

    quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')

        attempted_question = quiz_profile.attempts.select_related('question').get(question__pk=question_pk)

        choice_pk = request.POST.get('choice_pk')

        try:
            selected_choice = attempted_question.question.choices.get(pk=choice_pk)
        except ObjectDoesNotExist:
            raise Http404

        quiz_profile.evaluate_attempt(attempted_question, selected_choice)

        return redirect(attempted_question)

    else:
        question = quiz_profile.get_new_question()
        if question is not None:
            quiz_profile.create_attempt(question)
            p=p+1

        context = {
            'question': question,
            'num':p,
        }

        return render(request, 'quiz/play.html', context=context)


@login_required()
def submission_result(request, attempted_question_pk):
    # attempted_question = get_object_or_404(AttemptedQuestion, pk=attempted_question_pk)
    # context = {
    #     'attempted_question': attempted_question,
    # }

    # return render(request, 'quiz/submission_result.html', context=context)

    return render(request, 'quiz/submission_result.html')

@login_required()
def notsubmission_result(request):
    # attempted_question = get_object_or_404(AttemptedQuestion, pk=attempted_question_pk)
    # context = {
    #     'attempted_question': attempted_question,
    # }

    # return render(request, 'quiz/submission_result.html', context=context)

    return render(request, 'quiz/notsubmission_result.html')

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        # password = form.cleaned_data.get("password")
        user = authenticate(username=username, password="Pankaj@1234")
        login(request, user)
        return redirect('/')
    return render(request, 'quiz/login.html', {"form": form, "title": title})


def register(request):
    title = "Create account"
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'quiz/registration.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')

#
# def error_404(request):
#     data = {}
#     return render(request, 'quiz/error_404.html', data)
#
#
# def error_500(request):
#     data = {}
#     return render(request, 'quiz/error_500.html', data)
