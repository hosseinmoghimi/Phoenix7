# Generated by Django 5.0.6 on 2024-10-02 05:44

import django.db.models.deletion
import utility.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Access',
                'verbose_name_plural': 'Accesss',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('muted', 'muted'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('rose', 'rose'), ('dark', 'dark')], default='primary', max_length=50, verbose_name='color')),
                ('type', models.CharField(blank=True, max_length=200, null=True, verbose_name='type')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('code', models.CharField(max_length=200, verbose_name='code')),
                ('pure_code', models.IntegerField(default=0, verbose_name='pure_code')),
                ('bedehkar', models.IntegerField(default=0, verbose_name='bedehkar')),
                ('bestankar', models.IntegerField(default=0, verbose_name='bestankar')),
                ('balance', models.IntegerField(default=0, verbose_name='balance')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('logo_origin', models.ImageField(blank=True, null=True, upload_to='accounting/images/account', verbose_name='logo')),
                ('priority', models.IntegerField(default=100)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.profile', verbose_name='profile')),
            ],
            bases=(models.Model, utility.models.LinkHelper),
        ),
        migrations.CreateModel(
            name='AccountingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='date_time')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date_modified ')),
            ],
            options={
                'verbose_name': 'AccountingDocument',
                'verbose_name_plural': 'AccountingDocuments',
            },
            bases=(models.Model, utility.models.LinkHelper),
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('color_origin', models.CharField(blank=True, choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('muted', 'muted'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('rose', 'rose'), ('dark', 'dark')], max_length=50, null=True, verbose_name='color')),
            ],
            options={
                'verbose_name': 'EventCategory',
                'verbose_name_plural': 'EventCategories',
            },
            bases=(models.Model, utility.models.LinkHelper),
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.page')),
            ],
            options={
                'verbose_name': 'Thing',
                'verbose_name_plural': 'Thingس',
            },
            bases=('core.page', utility.models.LinkHelper),
        ),
        migrations.CreateModel(
            name='AccountGroup',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.account')),
            ],
            options={
                'verbose_name': 'AccountGroup',
                'verbose_name_plural': 'AccountGroups',
            },
            bases=('accounting.account',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.account')),
                ('prefix', models.CharField(choices=[('آقای', 'آقای'), ('خانم', 'خانم'), ('شرکت', 'شرکت'), ('دکتر', 'دکتر'), ('مهندس', 'مهندس')], max_length=50, verbose_name='prefix')),
                ('first_name', models.CharField(max_length=50, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last_name')),
            ],
            options={
                'verbose_name': 'شخص',
                'verbose_name_plural': 'اشخاص',
            },
            bases=('accounting.account',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.page')),
                ('status', models.CharField(choices=[('پیش نویس', 'پیش نویس'), ('در جریان', 'در جریان'), ('آماده تحویل', 'آماده تحویل'), ('تایید شده', 'تایید شده'), ('تحویل شده', 'تحویل شده'), ('کنسل شده', 'کنسل شده'), ('برگشت از تحویل', 'برگشت از تحویل'), ('تایید نهایی شده', 'تایید نهایی شده'), ('پاس شده', 'پاس شده'), ('مانده حساب از قبل', 'مانده حساب از قبل')], default='پیش نویس', max_length=50, verbose_name='وضعیت')),
                ('amount', models.IntegerField(default=0, verbose_name='مبلغ')),
                ('payment_method', models.CharField(choices=[('پیش نویس', 'پیش نویس'), ('همراه بانک', 'همراه بانک'), ('فروش کالا', 'فروش کالا'), ('فروش خدمات', 'فروش خدمات'), ('نقدی', 'نقدی'), ('چک', 'چک'), ('کارتخوان', 'کارتخوان'), ('فیش بانکی', 'فیش بانکی'), ('کارت به کارت', 'کارت به کارت')], default='پیش نویس', max_length=50, verbose_name='نوع پرداخت')),
                ('event_datetime', models.DateTimeField(verbose_name='تاریخ تراکنش')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.profile', verbose_name='ثبت شده توسط')),
                ('pay_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events_from', to='accounting.account', verbose_name='پرداخت کننده')),
                ('pay_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events_to', to='accounting.account', verbose_name='دریافت کننده')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.eventcategory', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=('core.page',),
        ),
        migrations.CreateModel(
            name='AccountingDocumentLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='date_time')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date_modified ')),
                ('bedehkar', models.IntegerField(default=0, verbose_name='بدهکار')),
                ('bestankar', models.IntegerField(default=0, verbose_name='بستانکار')),
                ('balance', models.IntegerField(default=0, verbose_name='بالانس')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.account', verbose_name='account')),
                ('accounting_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.accountingdocument', verbose_name='accountingdocument')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounting.event', verbose_name='event')),
            ],
            options={
                'verbose_name': 'AccountingDocumentLine',
                'verbose_name_plural': 'AccountingDocumentLines',
            },
            bases=(models.Model, utility.models.LinkHelper),
        ),
        migrations.CreateModel(
            name='EventPrint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('print_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ چاپ')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.event', verbose_name='تراکنش')),
            ],
            options={
                'verbose_name': 'EventPrint',
                'verbose_name_plural': 'EventPrints',
            },
        ),
        migrations.CreateModel(
            name='FinancialDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.account', verbose_name='account')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.event', verbose_name='event')),
            ],
            options={
                'verbose_name': 'FinancialDocument',
                'verbose_name_plural': 'FinancialDocuments',
            },
            bases=(utility.models.LinkHelper, models.Model),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('thing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.thing')),
                ('barcode', models.CharField(blank=True, max_length=100, null=True, verbose_name='بارکد')),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالا ها',
            },
            bases=('accounting.thing',),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('thing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.thing')),
            ],
            options={
                'verbose_name': 'خدمت',
                'verbose_name_plural': 'خدمات',
            },
            bases=('accounting.thing',),
        ),
        migrations.CreateModel(
            name='BasicAccount',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.account')),
                ('account_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.accountgroup', verbose_name='account group')),
            ],
            options={
                'verbose_name': 'BasicAccount',
                'verbose_name_plural': 'BasicAccounts',
            },
            bases=('accounting.account',),
        ),
        migrations.CreateModel(
            name='MoeinAccount',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.account')),
                ('basic_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.basicaccount', verbose_name='basicaccount')),
                ('moein_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.moeinaccount', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'MoeinAccount',
                'verbose_name_plural': 'MoeinAccounts',
            },
            bases=('accounting.account',),
        ),
        migrations.CreateModel(
            name='TafsiliAccount',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.account')),
                ('mobile', models.CharField(blank=True, max_length=50, null=True, verbose_name='mobile')),
                ('tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='tel')),
                ('moein_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.moeinaccount', verbose_name='moein account')),
                ('tafsili_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.tafsiliaccount', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'حساب تفصیلی',
                'verbose_name_plural': 'حساب های تفصیلی',
            },
            bases=('accounting.account',),
        ),
    ]
