from django.db import models
from django.utils.translation import gettext as _
from .apps import APP_NAME
from .enums import *
from django.conf import settings
IMAGE_FOLDER=APP_NAME+"/images/"
from utility.models import LinkHelper,ImageHelper
from phoenix.settings_server import CREATE_PROFILE_ON_USER_ADD



if CREATE_PROFILE_ON_USER_ADD:
    from django.db.models.signals import post_save

    def create_profile_receiver(sender,instance,created,*args, **kwargs):  
        if created:
            profile=Profile(user_id=instance.id)
            profile.save()

    def save_profile_receiver(sender,instance,*args, **kwargs):    
        profile=instance.profile
        profile.save()
        # if profile.region is None:
        #     try:
        #         from core.models import Region
        #         profile.region=Region.objects.first()
        #         profile.save()
        #     except:
        #         pass
        try:
            pass

 

        except:
            pass
        

    post_save.connect(create_profile_receiver, sender=settings.AUTH_USER_MODEL)
    post_save.connect(save_profile_receiver, sender=settings.AUTH_USER_MODEL)



class Profile(models.Model,LinkHelper):
    app_name=APP_NAME
    class_name="profile"

    user=models.OneToOneField(settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,null=True,blank=True)
    mobile=models.CharField(_("شماره همراه"),null=True,blank=True, max_length=50)
    bio=models.CharField(_("بیو"),null=True,blank=True, max_length=50)
    address=models.CharField(_("آدرس"),null=True,blank=True, max_length=50)
    image_origin=models.ImageField(_("تصویر"),null=True,blank=True, upload_to=IMAGE_FOLDER+"profile/", height_field=None, width_field=None, max_length=None)
    header_origin=models.ImageField(_("سربرگ"),null=True,blank=True, upload_to=IMAGE_FOLDER+"profile/header/", height_field=None, width_field=None, max_length=None)
    enabled=models.BooleanField(_("فعال"),default=False)
    can_login=models.BooleanField(_("لاگین می کند ?"),default=False)
    status=models.CharField(_("وضعیت"),choices=ProfileStatusEnum.choices,default=ProfileStatusEnum.AAA, max_length=50)
    gender=models.CharField(_("جنسیت"),choices=GenderEnum.choices,default=GenderEnum.MALE, max_length=50)
    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name 
