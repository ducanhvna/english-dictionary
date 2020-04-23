from django.shortcuts import render
from .forms import MeaniningForm
from .main import translate

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id')
        # id = kwargs.get('id', 'Default Value if not there')
        # username = "hi"
        meaning = translate(id)
        content = {'message': id, "value": meaning}
        return Response(content)

# Create your views here.
def home(request):
    meaningform = MeaniningForm(request.POST or None)
    context = {'meaningform': meaningform}
    if meaningform.is_valid():
        response = meaningform.cleaned_data['word']
        meaning = translate(response)
        if type(meaning) == list:
            context['response_list'] = meaning
        else:
            context['response'] = meaning
        return render(request, 'index.html', context=context)
    return render(request, 'index.html', context=context)
