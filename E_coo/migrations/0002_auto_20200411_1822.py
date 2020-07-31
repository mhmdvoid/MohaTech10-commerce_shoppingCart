# Generated by Django 3.0.5 on 2020-04-11 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('E_coo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('tag', models.ManyToManyField(to='E_coo.Tags')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_coo.Items')),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='products',
        ),
        migrations.AddField(
            model_name='orders',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_date_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_date_purchased',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='orders',
            name='items',
            field=models.ManyToManyField(to='E_coo.OrderedItems'),
        ),
    ]
