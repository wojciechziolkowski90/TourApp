# Generated by Django 3.2.7 on 2021-09-26 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttractionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveIntegerField(choices=[(1, 'Dzień 1'), (2, 'Wtorek'), (3, 'Środa'), (4, 'Czwartek'), (5, 'Piątek'), (6, 'Sobota'), (7, 'Niedziela')])),
                ('order', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=100)),
                ('region_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='Imię')),
                ('user_review', models.TextField(verbose_name='Opinia')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=255, verbose_name='Nazwa wycieczki')),
                ('tour_days', models.IntegerField(verbose_name='Ilość dni')),
                ('tour_start', models.DateField(verbose_name='Wyjazd')),
                ('tour_end', models.DateField(verbose_name='Powrót')),
                ('tour_foto', models.ImageField(blank=True, null=True, upload_to='Tours_app/static/images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='Tours_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('e_mail', models.EmailField(max_length=254)),
                ('tour_reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TouristAttractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attraction_name', models.CharField(max_length=100)),
                ('attraction_description', models.CharField(max_length=255)),
                ('attraction_type', models.IntegerField(choices=[(1, 'Przyrodnicza'), (2, 'Miejska'), (3, 'Kulturowa'), (4, 'Aktywna'), (5, 'Winiarska')])),
                ('attraction_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.region')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_attractions',
            field=models.ManyToManyField(through='Tours_app.AttractionPlan', to='Tours_app.TouristAttractions'),
        ),
        migrations.AddField(
            model_name='attractionplan',
            name='attraction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.touristattractions'),
        ),
        migrations.AddField(
            model_name='attractionplan',
            name='day_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.day'),
        ),
        migrations.AddField(
            model_name='attractionplan',
            name='tour_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.tour'),
        ),
    ]
