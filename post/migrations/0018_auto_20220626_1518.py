# Generated by Django 3.2.4 on 2022-06-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_post_accept_viewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.CharField(choices=[('1', 'Public'), ('2', 'Friend'), ('3', 'Excepttion people'), ('4', 'Private'), ('5', 'Specific friends'), ('6', 'Custom'), ('7', 'Best friend'), ('8', 'Unnamed list'), ('9', 'Acquaintance')], default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='viewer',
            field=models.CharField(choices=[('1', 'Public'), ('2', 'Friend'), ('3', 'Excepttion people'), ('4', 'Private'), ('5', 'Specific friends'), ('6', 'Custom'), ('7', 'Best friend'), ('8', 'Unnamed list'), ('9', 'Acquaintance')], default='Public', max_length=100),
        ),
        migrations.AlterField(
            model_name='story',
            name='viewer',
            field=models.CharField(choices=[('1', 'Public'), ('2', 'Friend'), ('3', 'Excepttion people'), ('4', 'Private'), ('5', 'Specific friends'), ('6', 'Custom'), ('7', 'Best friend'), ('8', 'Unnamed list'), ('9', 'Acquaintance')], default='Public', max_length=100),
        ),
    ]
