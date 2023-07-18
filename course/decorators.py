# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.http import Http404
from coursemanagement.models import CourseSetting



is_calender_on = CourseSetting.objects.filter(add_drop=True).count() > 0