# Generated by Django 5.0.3 on 2024-03-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0009_alter_person_nome_alter_person_sobrenome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]