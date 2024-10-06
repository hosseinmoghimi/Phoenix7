from django.utils.translation import gettext as _
from django.db.models import TextChoices

class ProfileStatusEnum(TextChoices):
    AAA="AAA" , _("AAA")
    BBB="BBB" , _("BBB")

class GenderEnum(TextChoices):
    MALE="مرد" , _("مرد")
    FEMALE="زن" , _("زن")

    
class PersonPrefixEnum(TextChoices):
    MR="آقای",_("آقای")
    MRS="خانم",_("خانم")
    COMPANY="شرکت",_("شرکت")
    DR="دکتر",_("دکتر")
    ENGINEER="مهندس",_("مهندس")


class ProfileContactTypeEnum(TextChoices):
    MOBILE="موبایل" , _("موبایل")
    TEL="تلفن" , _("تلفن")
    FAX="فکس" , _("فکس")
    EMAIL="ایمیل" , _("ایمیل")
    WHATSAPP="واتسپ" , _("واتسپ")
    TELEGRAM="تلگرام" , _("تلگرام")
    YOUTUBE="یوتوب" , _("یوتوب")
    INSTAGRAM="اینستاگرام" , _("آدرس")
    ADDRESS="آدرس" , _("آدرس")
    WEBSITE="وب سایت" , _("وب سایت")

class AUTH_PictureNameEnum(TextChoices):
    LOGIN_FORM_HEADER="سربرگ فرم لاگین" , _("سربرگ فرم لاگین")
    REGISTER_FORM_HEADER="سربرگ فرم ثبت نام" , _("سربرگ فرم ثبت نام")
    CHANGE_PASSWORD_FORM_HEADER="سربرگ فرم تغییر کلمه عبور" , _("سربرگ فرم تغییر کلمه عبور")
