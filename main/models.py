from django.db import models

from django.contrib.auth.models import User


try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_field
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile',on_delete=models.CASCADE)
    avatar_url = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return force_text(self.user.email+self.avatar_url)

    class Meta():
        db_table = 'user_profile'




class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        picture = sociallogin.account.extra_data['picture']

        profile = UserProfile(user=user,avatar_url=picture)
        profile.save()
        

    def populate_user(self, request, sociallogin, data):

        print("sadlfhjdshfjkasdlfk")
        user = super().populate_user(request, sociallogin, data)



        print("my user 1",user)
        
        try:
            picture = sociallogin.account.extra_data['picture']
            print("picture:",picture)
            user_field(user, "profile_photo", picture)
            print("my user:",user)

            # user.save()

            # profile = UserProfile(user=user,avatar_url=picture)
            # profile.save()
        except (KeyError, AttributeError):
            print("error")
        return user