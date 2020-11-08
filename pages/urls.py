from django.urls import path
from .views import *

# manages the urls associated with the pages app
urlpatterns = [
    path('', landingPageView, name='landingPage'),
    path('home/', homePageView, name="homePage"),
    path('import/', importPageView, name='importPage'),
    path('visualizations/', visPageView, name='visPage'),
    path('vmcadmin/', vmcAdminPageView, name='vmcAdminPage'),
    path('vmcadmin/changePassword', changePassView, name='changePassPage'),
    path('vmcadmin/changeEmail', changeEmailView, name='changeEmailPage'),
    path('vmcadmin/changeProfileInfo', changeProfileView, name='changeProfilePage'),
    path('vmcadmin/ViewAccountsList', accountsView, name='accountsView'),
    path('vmcadmin/ViewAccountsList/newAccount', newAccount, name='newAccount')

]