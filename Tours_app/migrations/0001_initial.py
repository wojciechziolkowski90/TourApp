# Generated by Django 3.2.7 on 2021-09-17 14:01

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
            name='DayName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.PositiveIntegerField(choices=[(1, 'Poniedziałek'), (2, 'Wtorek'), (3, 'Środa'), (4, 'Czwartek'), (5, 'Piątek'), (6, 'Sobota'), (7, 'Niedziela')])),
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
                ('user_name', models.CharField(max_length=100)),
                ('user_review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=150, unique=True)),
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
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=255)),
                ('tour_days', models.IntegerField()),
                ('tour_start', models.DateField()),
                ('tour_end', models.DateField()),
                ('tour_foto', models.ImageField(upload_to='images/', verbose_name='foto')),
                ('tour_attractions', models.ManyToManyField(through='Tours_app.AttractionPlan', to='Tours_app.TouristAttractions')),
                ('tour_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.tourtype')),
            ],
        ),
        migrations.AddField(
            model_name='attractionplan',
            name='attraction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.touristattractions'),
        ),
        migrations.AddField(
            model_name='attractionplan',
            name='day_name_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.dayname'),
        ),
        migrations.AddField(
            model_name='attractionplan',
            name='tour_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours_app.tour'),
        ),
    ]
