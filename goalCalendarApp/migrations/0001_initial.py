
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('activity', models.ForeignKey('Activity', on_delete=models.CASCADE, related_name='activity_events', default=0)),
                ('datetime', models.DateTimeField(verbose_name='datetime')),
            ],
        ),
    ]
