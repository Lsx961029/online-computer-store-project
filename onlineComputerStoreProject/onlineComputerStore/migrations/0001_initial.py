# Generated by Django 2.2.5 on 2021-05-02 21:25

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.CharField(max_length=4)),
                ('customer_name', models.CharField(max_length=20)),
                ('card_number', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(6), django.core.validators.MinLengthValidator(6)])),
            ],
        ),
        migrations.CreateModel(
            name='Clerk',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('balance', models.FloatField(default=0.0)),
                ('saved_address', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
            options={
                'permissions': [('add_balance', 'can add balance')],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('card_number', models.CharField(max_length=20)),
                ('csc', models.CharField(max_length=3)),
                ('expired_date', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('balance', models.FloatField(default=0.0)),
                ('saved_address', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
            options={
                'permissions': [('add_balance', 'can add balance')],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryCompany',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('brand', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('price', models.FloatField(default=None, null=True)),
                ('quantity', models.IntegerField(default=None, null=True)),
                ('discount', models.FloatField(blank=True, default=1, null=True)),
                ('rating', models.FloatField(blank=True, default=None, null=True)),
                ('quantity_sold', models.IntegerField(blank=True, default=0, null=True)),
                ('img', models.ImageField(blank=True, default='img/default_img/400x650.png', null=True, upload_to='img/item_img/')),
                ('url_slug', models.SlugField(default='', editable=False)),
                ('description', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='onlineComputerStore.Item')),
                ('architecture', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('num_cores', models.IntegerField(blank=True, default=None, null=True)),
                ('frequency', models.FloatField(blank=True, default=None, null=True)),
            ],
            bases=('onlineComputerStore.item',),
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='onlineComputerStore.Item')),
                ('chipset', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('num_cuda_cores', models.IntegerField(blank=True, default=None, null=True)),
                ('core_clock', models.FloatField(blank=True, default=None, null=True)),
                ('memory_size', models.FloatField(blank=True, default=None, null=True)),
            ],
            bases=('onlineComputerStore.item',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('clerk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='onlineComputerStore.Clerk')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('onlineComputerStore.clerk',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='onlineComputerStore.Item')),
                ('capacity', models.FloatField(blank=True, default=0.0, null=True)),
                ('type', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('frequency', models.IntegerField(blank=True, default=None, null=True)),
            ],
            bases=('onlineComputerStore.item',),
        ),
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.CharField(max_length=300)),
                ('finalized', models.BooleanField(default=False)),
                ('reported_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('amount', models.FloatField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='TabooList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, unique=True)),
                ('addBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Clerk')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.UUIDField(default=uuid.UUID('e5dc3192-ab8c-11eb-9fce-b975dfadb25a'), editable=False)),
                ('status', models.CharField(default='in progress', max_length=20)),
                ('address', models.CharField(default=None, max_length=50, null=True)),
                ('customer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Customer')),
                ('delivery_company', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.DeliveryCompany')),
                ('transaction', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('url_slug', models.SlugField(default='', editable=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bidfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('delivery_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.DeliveryCompany')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ForumWarning',
            fields=[
                ('warning_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='onlineComputerStore.Warning')),
                ('discuss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Discussion')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('onlineComputerStore.warning',),
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='onlineComputerStore.Item')),
                ('os', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('computer_cpu', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='onlineComputerStore.CPU')),
                ('computer_gpu', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='onlineComputerStore.GPU')),
                ('computer_memory', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='onlineComputerStore.Memory')),
            ],
            bases=('onlineComputerStore.item',),
        ),
    ]
