# Generated by Django 4.0.2 on 2022-02-22 20:43

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='f3QWNewhPb', max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, max_length=1024)),
                ('status', models.CharField(choices=[('Pre-GB', 'Pre-GB'), ('Ordered GB', 'Ordered GB'), ('Ordered In-Stock', 'Ordered In-Stock'), ('Shipping', 'Shipping'), ('Present', 'Present'), ('Sold', 'Sold')], max_length=255)),
                ('cost', models.FloatField()),
                ('aftermarket_seller', models.CharField(blank=True, max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('sell_price', models.FloatField(blank=True, null=True)),
                ('switch_type', models.CharField(choices=[('Linear', 'Linear'), ('Tactile', 'Tactile'), ('Clicky', 'Clicky')], max_length=255)),
                ('lube', models.CharField(blank=True, max_length=255)),
                ('film', models.CharField(blank=True, max_length=255)),
                ('actuation_force', models.FloatField(blank=True, null=True)),
                ('bottom_out_force', models.FloatField()),
                ('top_material', models.CharField(blank=True, max_length=255)),
                ('bottom_material', models.CharField(blank=True, max_length=255)),
                ('stem_material', models.CharField(blank=True, max_length=255)),
                ('spring_material', models.CharField(blank=True, max_length=255)),
                ('spring_length', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'switches',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Keycap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='f3QWNewhPb', max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, max_length=1024)),
                ('status', models.CharField(choices=[('Pre-GB', 'Pre-GB'), ('Ordered GB', 'Ordered GB'), ('Ordered In-Stock', 'Ordered In-Stock'), ('Shipping', 'Shipping'), ('Present', 'Present'), ('Sold', 'Sold')], max_length=255)),
                ('cost', models.FloatField()),
                ('aftermarket_seller', models.CharField(blank=True, max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('sell_price', models.FloatField(blank=True, null=True)),
                ('profile', models.CharField(max_length=255)),
                ('sets', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('production', models.CharField(choices=[('Doubleshot', 'Doubleshot'), ('Tripleshot', 'Tripleshot'), ('Dye-Sublimated', 'Dye-Sublimated'), ('Other', 'Other')], max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='f3QWNewhPb', max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, max_length=1024)),
                ('status', models.CharField(choices=[('Pre-GB', 'Pre-GB'), ('Ordered GB', 'Ordered GB'), ('Ordered In-Stock', 'Ordered In-Stock'), ('Shipping', 'Shipping'), ('Present', 'Present'), ('Sold', 'Sold')], max_length=255)),
                ('cost', models.FloatField()),
                ('aftermarket_seller', models.CharField(blank=True, max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('sell_price', models.FloatField(blank=True, null=True)),
                ('size', models.CharField(choices=[('Numpad', 'Numpad'), ('40%', '40%'), ('60%', '60%'), ('65%', '65%'), ('75%', '75%'), ('TKL', 'TKL'), ('1800', '1800'), ('Full', 'Full'), ('Other', 'Other')], max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('pcb', models.CharField(max_length=255)),
                ('plate', models.CharField(max_length=255)),
                ('wkl', models.CharField(choices=[('Y', 'Y'), ('N', 'N'), ('N/A', 'N/A')], max_length=255)),
                ('foam', models.CharField(blank=True, max_length=255)),
                ('material', models.CharField(blank=True, max_length=255)),
                ('front_height', models.FloatField(blank=True, null=True)),
                ('typing_angle', models.FloatField(blank=True, null=True)),
                ('mount', models.CharField(blank=True, max_length=255)),
                ('weight', models.CharField(blank=True, max_length=255)),
                ('knob', models.CharField(blank=True, max_length=255)),
                ('extra_pcbs', models.CharField(blank=True, max_length=255)),
                ('extra_plates', models.CharField(blank=True, max_length=255)),
                ('extra_accessories', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='f3QWNewhPb', max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, max_length=1024)),
                ('keyboard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.keyboard')),
                ('keycap', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.keycap')),
                ('switch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.switch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Artisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='f3QWNewhPb', max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, max_length=1024)),
                ('status', models.CharField(choices=[('Pre-GB', 'Pre-GB'), ('Ordered GB', 'Ordered GB'), ('Ordered In-Stock', 'Ordered In-Stock'), ('Shipping', 'Shipping'), ('Present', 'Present'), ('Sold', 'Sold')], max_length=255)),
                ('cost', models.FloatField()),
                ('aftermarket_seller', models.CharField(blank=True, max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('sell_price', models.FloatField(blank=True, null=True)),
                ('profile', models.CharField(blank=True, max_length=255)),
                ('build', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.build')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='f3QWNewhPb', max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, max_length=1024)),
                ('status', models.CharField(choices=[('Pre-GB', 'Pre-GB'), ('Ordered GB', 'Ordered GB'), ('Ordered In-Stock', 'Ordered In-Stock'), ('Shipping', 'Shipping'), ('Present', 'Present'), ('Sold', 'Sold')], max_length=255)),
                ('cost', models.FloatField()),
                ('aftermarket_seller', models.CharField(blank=True, max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('sell_price', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'accessories',
                'ordering': ['-name'],
            },
        ),
    ]
