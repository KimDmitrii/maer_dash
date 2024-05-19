from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Report


# Create your views here.
@login_required
def report_view(request, report_id):
    report = Report.objects.get(id=report_id)
    part1 = "https://app.powerbi.com/view?"
    part2 = "r=eyJrIjoiODJkYmE0MD"
    part3 = "ctNDZiMC00MDE2LTliMmUtZDVjZDEzMmI2YjdiIiwidCI6IjA1NTgwMWU2LTQyZjAtN"
    part4 = "DcwZC04Njc5LTVhNmE3NjFhOGQ0YyIsImMiOjl9"
    return render(request, 'dashboard.html', {'report': report, 'part1': part1, 'part2': part2, 'part3': part3, 'part4': part4 })