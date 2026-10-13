


from django.urls import path
from spending.views import SignUpViews
from spending.views import GetMeView
from spending.views import ExpenseListCreateView
from spending.views import ExpenseRetriveUpdateDeleteView

from rest_framework.authtoken.views import ObtainAuthToken

from spending.views import ExpenseSummaryView

urlpatterns = [
    path("register/",SignUpViews.as_view()),
    path("me/",GetMeView.as_view()),
    path("expenses/",ExpenseListCreateView.as_view()),
    path("expenses/<int:pk>/",ExpenseRetriveUpdateDeleteView.as_view()),

    path("token/",ObtainAuthToken.as_view()),

    path("expenses/summary/",ExpenseSummaryView.as_view())
    
    
]