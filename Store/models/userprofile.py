from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# USER_CHOICES =(
#     ("Customer", "Customer"),
#     ("Farmer", "Farmer"),
   
# )
  
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.TextField(max_length=300, blank=True, default='')
    national_id_no = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    image = models.FileField(default = 'upload/pkrishokImage/blank.png', upload_to = 'upload/pkrishokImage/', blank=True)
    national_id = models.FileField(default= 'upload/IDImage/blank.png',upload_to = 'upload/IDImage/', blank=True)

    

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return self.user.username
        
    def save_profile(self):
        self.save()

        # this is not needed if small_image is created at set_image
    # def save(self, *args, **kwargs):
    #     super(UserProfile, self).save(*args, **kwargs)

    @staticmethod
    def get_info_of_user(user_id):
        return UserProfile.objects.filter(user = user_id)

   