from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from moisture.models import MoistureLevel
from django.core.management import call_command


class MoistureView(View):
    def get(self, request):
        # Get the latest 25 moisture levels with 'saturated' and 'created_at' fields
        moisture_levels = MoistureLevel.objects.order_by('-id')[:20]

        # Check if the request is an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Prepare the data for JSON, ensuring dates are serialized
            moisture_levels_json = list(moisture_levels.values('saturated', 'created_at'))
            return JsonResponse(moisture_levels_json, safe=False)
        else:
            # Render the template, passing the queryset directly
            return render(
                request,
                "moisture/moisture.html",
                context={"moisture_levels": moisture_levels},
            )

    def post(self, request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            call_command('get_moisture')
            moisture_levels = MoistureLevel.objects.order_by('-id')[:20]
            moisture_levels_json = list(moisture_levels.values('saturated', 'created_at'))
            return JsonResponse(moisture_levels_json, safe=False)

