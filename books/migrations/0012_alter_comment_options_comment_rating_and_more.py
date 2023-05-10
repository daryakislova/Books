# Generated by Django 4.1.7 on 2023-04-16 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0011_alter_comment_book_alter_comment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(blank=True, default=0, verbose_name='Оценка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(blank=True, default=0.0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=2023, verbose_name='Год издания'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='books.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]