from django.contrib import admin

# Register your models here.

from.models import (CourseDuration,Course,Trainer,Enquiry,Booking,Payment,)
admin.site.register([CourseDuration,Course,Trainer,Enquiry,Booking,Payment,])

