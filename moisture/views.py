from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from moisture.models import MoistureLevel
from django.utils import timezone

class MoistureView(View):
    def get(self, request):
        today = timezone.now().date()
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            moisture_levels = list(MoistureLevel.objects.filter(created_at__date=today).values('saturated', 'created_at'))
            return JsonResponse(moisture_levels, safe=False)
        else:
            moisture_levels = MoistureLevel.objects.filter(created_at__date=today)
            return render(
                request,
                "moisture/moisture.html",
                context={"moisture_levels": moisture_levels},
            )
