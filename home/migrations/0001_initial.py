# Generated by Django 4.1 on 2022-09-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_text1', models.TextField(blank=True, null=True)),
                ('event_text2', models.TextField(blank=True, null=True)),
                ('event_text3', models.TextField(blank=True, null=True)),
                ('event_text4', models.TextField(blank=True, null=True)),
                ('event_text5', models.TextField(blank=True, null=True)),
                ('event_text6', models.TextField(blank=True, null=True)),
                ('event_text7', models.TextField(blank=True, null=True)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='images/event')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('heading1', models.CharField(blank=True, max_length=256, null=True)),
                ('text1', models.TextField(blank=True, null=True)),
                ('heading2', models.CharField(blank=True, max_length=256, null=True)),
                ('text21', models.TextField(blank=True, null=True)),
                ('text22', models.TextField(blank=True, null=True)),
                ('text23', models.TextField(blank=True, null=True)),
                ('text24', models.TextField(blank=True, null=True)),
                ('text25', models.TextField(blank=True, null=True)),
                ('heading3', models.CharField(blank=True, max_length=256, null=True)),
                ('text31', models.TextField(blank=True, null=True)),
                ('text32', models.TextField(blank=True, null=True)),
                ('text33', models.TextField(blank=True, null=True)),
                ('text34', models.TextField(blank=True, null=True)),
                ('text35', models.TextField(blank=True, null=True)),
                ('heading4', models.CharField(blank=True, max_length=256, null=True)),
                ('text41', models.TextField(blank=True, null=True)),
                ('text42', models.TextField(blank=True, null=True)),
                ('text43', models.TextField(blank=True, null=True)),
                ('text44', models.TextField(blank=True, null=True)),
                ('text45', models.TextField(blank=True, null=True)),
                ('project_image1', models.ImageField(blank=True, null=True, upload_to='images/project')),
                ('project_image2', models.ImageField(blank=True, null=True, upload_to='images/project')),
                ('project_image3', models.ImageField(blank=True, null=True, upload_to='images/project')),
                ('project_image4', models.ImageField(blank=True, null=True, upload_to='images/project')),
                ('project_image5', models.ImageField(blank=True, null=True, upload_to='images/project')),
                ('project_image6', models.ImageField(blank=True, null=True, upload_to='images/project')),
            ],
        ),
    ]
