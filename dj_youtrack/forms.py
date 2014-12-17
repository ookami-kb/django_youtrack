# -*- encoding: utf-8 -*-
from django import forms
from django.conf import settings
from youtrack.connection import Connection
from youtrack import YouTrackException


class IssueForm(forms.Form):
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, project, subsystem=None, **kwargs):
        self.project = project
        self.subsystem = subsystem
        super(IssueForm, self).__init__(**kwargs)

    def submit(self):
        try:
            connection = Connection(settings.YOUTRACK_URL, settings.YOUTRACK_LOGIN, settings.YOUTRACK_PASSWORD)
            response, content = connection.createIssue(self.project, assignee=None,
                                                       summary=u'Issue from feedback form',
                                                       description=self.cleaned_data['description'])
            print response
            issue_id = response['location'].split('/')[-1]
            commands = 'Customer email ' + self.cleaned_data['email']
            if self.subsystem is not None:
                commands += ' Subsystem %s' % self.subsystem
            connection.executeCommand(issue_id, commands)
            return True
        except YouTrackException:
            return False