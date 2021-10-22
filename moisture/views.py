from django.shortcuts import render
from django.views.generic import View

from moisture.models import MoistureLevel


class MoistureView(View):
    def get(self, request):
        moisture_levels = MoistureLevel.objects.all()
        return render(
            request,
            "moisture/moisture.html",
            context={"moisture_levels": moisture_levels},
        )
