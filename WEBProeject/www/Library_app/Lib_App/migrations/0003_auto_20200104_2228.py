# Generated by Django 2.2.2 on 2020-01-04 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lib_App', '0002_borrower_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='books_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='persons',
            name='person_due',
            field=models.IntegerField(max_length=1),
        ),
    ]
