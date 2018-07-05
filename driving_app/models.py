from django.db import models

# Create your models here.


COURSE_STATUS =(
    (1,'Active'),
    (0,'Inactive'),
)

ENQUIRY_STATUS =(
    (3,'High'),
    (2,'Medium'),
    (1,'Low'),
)


class CourseDuration(models.Model):
    courseduration = models.CharField(max_length=128)

    def __repr__(self):
        return self.courseduration
    
    __str__=__repr__


class Course(models.Model):
    coursename = models.CharField(max_length=128,help_text="Please enter the course name")
    courseduration = models.ForeignKey(CourseDuration, null=True, on_delete=models.SET_NULL)
    fees = models.FloatField(help_text="Rs 5000")
    coursediscount = models.IntegerField(help_text="eg: 12 %")
    status = models.PositiveSmallIntegerField(choices=COURSE_STATUS)

    def __repr__(self):
        return self.coursename
    
    __str__=__repr__

class Trainer(models.Model):
    fullname = models.CharField(max_length=128,help_text="Please enter the full name")
    adress = models.TextField(help_text="Nayabazar,kathmandu")
    contactno = models.CharField(max_length=128, help_text="9818204111")
    email = models.EmailField(max_length=128,null=True,blank=True, help_text="mydomain@gmail.com")
    fees = models.FloatField(help_text="Rs 5000")
    bonus = models.FloatField(help_text="Rs 5000")

    def __repr__(self):
        return self.fullname
    
    __str__=__repr__

class Enquiry(models.Model):
    courseid = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    fullname = models.CharField(max_length=128,help_text="Please enter the full name")
    adress = models.TextField(help_text="Nayabazar,kathmandu")
    contactno = models.CharField(max_length=128, help_text="9818204111")
    email = models.EmailField(max_length=128,help_text="mydomain@gmail.com")
    fees = models.FloatField(help_text="Rs 5000")
    dob = models.DateField()
    status = models.PositiveSmallIntegerField(choices=ENQUIRY_STATUS)


    def __repr__(self):
        return self.courseid
    
    __str__=__repr__

class Booking(models.Model):
    enquiryid = models.ForeignKey(Enquiry, null=True, on_delete=models.SET_NULL)
    courseid = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    advance = models.FloatField(help_text="Rs 5000")

    def __repr__(self):
        return self.enquiryid
    
    __str__=__repr__


class Payment(models.Model):
    bookingid = models.ForeignKey(Enquiry, null=True, on_delete=models.SET_NULL)
    courseid = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    
    def __repr__(self):
        return self.bookingid
    
    __str__=__repr__