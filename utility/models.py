from django.db import models

# Create your models here.
from phoenix.settings import ADMIN_URL,STATIC_URL,MEDIA_URL
from django.shortcuts import reverse
from .calendar import DateHelper


class ImageHelper():
    def thumbnail(self):
        return None

class DateHelper():
    def persian_start_date(self):
        return PersianCalendar().from_gregorian(self.start_date)
    def persian_end_date(self):
        return PersianCalendar().from_gregorian(self.end_date)
    def persian_date(self):
        return PersianCalendar().from_gregorian(self.date)
    def persian_date_added(self):
        return PersianCalendar().from_gregorian(self.date_added)
    def persian_date_added(self):
        return PersianCalendar().from_gregorian(self.date_added)
    def persian_date_created(self):
        return PersianCalendar().from_gregorian(self.date_created)
    def persian_date_modified(self):
        return PersianCalendar().from_gregorian(self.date_modified)


class DateTimeHelper(DateHelper):
    def persian_start_datetime(self):
        return PersianCalendar().from_gregorian(self.start_datetime)
    def persian_end_datetime(self):
        return PersianCalendar().from_gregorian(self.end_datetime)
    def persian_datetime(self):
        return PersianCalendar().from_gregorian(self.datetime)
    def persian_transaction_datetime(self):
        return PersianCalendar().from_gregorian(self.transaction_datetime)
    def persian_print_datetime(self):
        return PersianCalendar().from_gregorian(self.print_datetime)
    def persian_document_datetime(self):
        return PersianCalendar().from_gregorian(self.document_datetime)
    

class ImageHelper:
    @property
    def image(self):
        image=""
        try:
            sss=self.image_origin
        except:
            return self.thumbnail

        if self.image_origin is None or str(self.image_origin)=="":
            try:
                image= f"{STATIC_URL}{self.app_name}/img/pages/image/{self.class_name}.png/"
            except:
                pass
        else:
            image= f"{MEDIA_URL}{self.image_origin}"

        return image
    @property
    def thumbnail(self):
        thumbnail=""
        if self.thumbnail_origin is None or str(self.thumbnail_origin)=="":
            try:
                thumbnail= f"{STATIC_URL}{self.app_name}/img/pages/thumbnail/{self.class_name}.png/"
            except:
                pass
        else:
            thumbnail= f"{MEDIA_URL}{self.thumbnail_origin}"

        return thumbnail



class LinkHelper():
    def get_edit_url(self):
        return f"{ADMIN_URL}{self.app_name}/{self.class_name}/{self.pk}/change/"
    def get_absolute_url(self):
        return reverse(f"{self.app_name}:{self.class_name}",kwargs={'pk':self.pk})
    def get_delete_url(self):
        return f"{ADMIN_URL}{self.app_name}/{self.class_name}/{self.pk}/delete/"
        
    def get_edit_url_admin(self):
        return f'{ADMIN_URL}{self.app_name}/{self.class_name}/{self.pk}/change/'


    def get_edit_btn(self):
        return f"""
          <a target="_blank" title="ویرایش" href="{self.get_edit_url()}"><i class="fa fa-edit text-warning"></i></a>
        """
    def get_delete_btn(self):
        return f"""
          <a target="_blank" title="حذف" href="{self.get_delete_url()}"><i class="fa fa-trash text-danger"></i></a>
        """