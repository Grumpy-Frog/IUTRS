from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name = 'base.html'


class ExecutiveCommittee(TemplateView):
    template_name = 'ExecutiveCommittee.html'


class about(TemplateView):
    template_name = 'about.html'


class home(TemplateView):
    template_name = 'home.html'

class leaderboard(TemplateView):
    template_name = 'leaderboard.html'
