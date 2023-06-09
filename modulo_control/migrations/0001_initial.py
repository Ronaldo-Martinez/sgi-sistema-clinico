# Generated by Django 3.2.12 on 2022-08-02 04:20

from django.conf import settings
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
            name='Empleado',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('codigo_empleado', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True)),
                ('nombres', models.CharField(db_column='NOMBRES', max_length=40, null=True)),
                ('apellidos', models.CharField(db_column='APELLIDOS', max_length=40, null=True)),
                ('sexo', models.CharField(db_column='SEXO', default='-', max_length=1)),
                ('direccion', models.CharField(db_column='DIRECCION', max_length=120, null=True)),
                ('email', models.EmailField(blank=True, db_column='EMAIL', max_length=100, null=True, unique=True)),
                ('es_activo', models.BooleanField(db_column='ES_ACTIVO', default=True)),
                ('es_staff', models.BooleanField(db_column='ES_STAFF', default=False)),
                ('es_superuser', models.BooleanField(db_column='IS_SUPERUSER', default=False)),
                ('last_login', models.DateField(db_column='LAST_LOGIN', null=True)),
                ('fechaCreacion', models.DateTimeField(db_column='FECHA_CREACION', default=django.utils.timezone.now)),
                ('fechaNacimiento', models.DateField(db_column='FECHA_NACMIENTO', null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=15)),
                ('codigo_rol', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id_secretaria', models.AutoField(primary_key=True, serialize=False)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LicLaboratorioClinico',
            fields=[
                ('id_lic_laboratorio', models.AutoField(primary_key=True, serialize=False)),
                ('jvplc', models.IntegerField(default=0)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermera',
            fields=[
                ('id_enfermera', models.AutoField(primary_key=True, serialize=False)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id_doctor', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('especialidad_doctor', models.CharField(max_length=40)),
                ('jvmp', models.IntegerField()),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='roles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='modulo_control.rol'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
