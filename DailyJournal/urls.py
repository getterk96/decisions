from django.conf.urls import url
from DailyJournal.views import *


urlpatterns = [
    url(r'^list/?$', JournalList.as_view()),
    url(r'^create/?$', JournalCreate.as_view()),
]
