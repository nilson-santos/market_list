# Generated by Django 5.0.3 on 2024-03-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0016_alter_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(blank=True, default='#ffffff', max_length=7),
            preserve_default=False,
        ),
    ]
