from codex.baseerror import *
from codex.baseview import APIView
from DailyJournal.models import *

from datetime import datetime, timedelta


class JournalCreate(APIView):
    def post(self):
        self.check_input('content', 'evalution')
        journal = Journal()
        journal.evalution = self.input['evalution']
        journal.date = datetime.now() + timedelta(hours=8)
        journal.content = self.input['content']
        journal.save()

        return journal.id


class JournalDelete(APIView):
    def post(self):
        self.check_input('id', 'content', 'evalution')
        journal = Journal.safe_get(id=self.input['id'])
        journal.delete()

        return self.input['id']


class JournalList(APIView):
    def get(self):
        data = []
        for journal in Journal.objects.filter(date__gt=datetime.now().date()).order_by('-date'):
            act_data = {
                'id': journal.id,
                'date': journal.date.strftime("%Y-%m-%d %H:%M:%S"),
                'content': journal.content,
                'evalution': journal.evalution,
            }
            data.append(act_data)
        return data

# Create your views here.
