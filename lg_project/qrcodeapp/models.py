# from django.db import models

# gender_choices = ("Male", "Female")
# marital_status = ("Single", "Married", "Divored")
# # Create your models here.



# def passport_directory(instance, filename):
#     return "/".join(["documents", str(instance.first_name), "passport", filename])


# class UserAccount(models.Model):
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     email = models.EmailField(max_length=100)
#     gender = models.CharField(max_length=250, choices=gender_choices)
#     state_of_origin = models.CharField(max_length=250)
#     local_origin = models.CharField(max_length=250)
#     Occupation = models.CharField(max_length=250)
#     marital_status = models.CharField(max_length=250, choices=marital_status)
#     father_name = models.CharField(max_length=250)
#     mother_name = models.CharField(max_length=250)
#     contact_addres = models.CharField(max_length=250)
#     date_of_birth = models.DateField()
#     place_of_birth = models.CharField(max_length=100)
#     passport = models.ImageField(upload_to=passport_directory)
#     created_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):

#         return f"{self.first_name} {self.last_name}"
    