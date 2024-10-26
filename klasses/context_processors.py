# klasses/context_processors.py
from .models import Klass

def klasses(request):
    return {
        'klasses': Klass.objects.all()
    }
