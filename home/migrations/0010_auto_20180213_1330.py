# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180213_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsliderimage',
            name='h1_animation',
            field=models.CharField(blank=True, choices=[('bounce', 'bounce'), ('flash', 'flash'), ('pulse', 'pulse'), ('rubberBand', 'rubberBand'), ('shake', 'shake'), ('headShake', 'headShake'), ('swing', 'swing'), ('tada', 'tada'), ('wobble', 'wobble'), ('jello', 'jello'), ('bounceIn', 'bounceIn'), ('bounceInDown', 'bounceInDown'), ('bounceInLeft', 'bounceInLeft'), ('bounceInRight', 'bounceInRight'), ('bounceInUp', 'bounceInUp'), ('bounceOut', 'bounceOut'), ('bounceOutDown', 'bounceOutDown'), ('bounceOutLeft', 'bounceOutLeft'), ('bounceOutRight', 'bounceOutRight'), ('bounceOutUp', 'bounceOutUp'), ('fadeIn', 'fadeIn'), ('fadeInDown', 'fadeInDown'), ('fadeInDownBig', 'fadeInDownBig'), ('fadeInLeft', 'fadeInLeft'), ('fadeInLeftBig', 'fadeInLeftBig'), ('fadeInRight', 'fadeInRight'), ('fadeInRightBig', 'fadeInRightBig'), ('fadeInUp', 'fadeInUp'), ('fadeInUpBig', 'fadeInUpBig'), ('fadeOut', 'fadeOut'), ('fadeOutDown', 'fadeOutDown'), ('fadeOutDownBig', 'fadeOutDownBig'), ('fadeOutLeft', 'fadeOutLeft'), ('fadeOutLeftBig', 'fadeOutLeftBig'), ('fadeOutRight', 'fadeOutRight'), ('fadeOutRightBig', 'fadeOutRightBig'), ('fadeOutUp', 'fadeOutUp'), ('fadeOutUpBig', 'fadeOutUpBig'), ('flipInX', 'flipInX'), ('flipInY', 'flipInY'), ('flipOutX', 'flipOutX'), ('flipOutY', 'flipOutY'), ('lightSpeedIn', 'lightSpeedIn'), ('lightSpeedOut', 'lightSpeedOut'), ('rotateIn', 'rotateIn'), ('rotateInDownLeft', 'rotateInDownLeft'), ('rotateInDownRight', 'rotateInDownRight'), ('rotateInUpLeft', 'rotateInUpLeft'), ('rotateInUpRight', 'rotateInUpRight'), ('rotateOut', 'rotateOut'), ('rotateOutDownLeft', 'rotateOutDownLeft'), ('rotateOutDownRight', 'rotateOutDownRight'), ('rotateOutUpLeft', 'rotateOutUpLeft'), ('rotateOutUpRight', 'rotateOutUpRight'), ('hinge', 'hinge'), ('jackInTheBox', 'jackInTheBox'), ('rollIn', 'rollIn'), ('rollOut', 'rollOut'), ('zoomIn', 'zoomIn'), ('zoomInDown', 'zoomInDown'), ('zoomInLeft', 'zoomInLeft'), ('zoomInRight', 'zoomInRight'), ('zoomInUp', 'zoomInUp'), ('zoomOut', 'zoomOut'), ('zoomOutDown', 'zoomOutDown'), ('zoomOutLeft', 'zoomOutLeft'), ('zoomOutRight', 'zoomOutRight'), ('zoomOutUp', 'zoomOutUp'), ('slideInDown', 'slideInDown'), ('slideInLeft', 'slideInLeft'), ('slideInRight', 'slideInRight'), ('slideInUp', 'slideInUp'), ('slideOutDown', 'slideOutDown'), ('slideOutLeft', 'slideOutLeft'), ('slideOutRight', 'slideOutRight'), ('slideOutUp', 'slideOutUp')], help_text='Выбрать вид анимации, который будет применён к h1', max_length=250, verbose_name='Анимация h1'),
        ),
        migrations.AddField(
            model_name='aboutsliderimage',
            name='h1_is_animated',
            field=models.BooleanField(default=True, help_text='Добавить к h1 класс animated?', verbose_name='Animated h1?'),
        ),
        migrations.AddField(
            model_name='aboutsliderimage',
            name='h1_is_infinite',
            field=models.BooleanField(default=False, help_text='Добавить к h1 класс infinite?', verbose_name='infinite h1?'),
        ),
        migrations.AddField(
            model_name='aboutsliderimage',
            name='h3_animation',
            field=models.CharField(blank=True, choices=[('bounce', 'bounce'), ('flash', 'flash'), ('pulse', 'pulse'), ('rubberBand', 'rubberBand'), ('shake', 'shake'), ('headShake', 'headShake'), ('swing', 'swing'), ('tada', 'tada'), ('wobble', 'wobble'), ('jello', 'jello'), ('bounceIn', 'bounceIn'), ('bounceInDown', 'bounceInDown'), ('bounceInLeft', 'bounceInLeft'), ('bounceInRight', 'bounceInRight'), ('bounceInUp', 'bounceInUp'), ('bounceOut', 'bounceOut'), ('bounceOutDown', 'bounceOutDown'), ('bounceOutLeft', 'bounceOutLeft'), ('bounceOutRight', 'bounceOutRight'), ('bounceOutUp', 'bounceOutUp'), ('fadeIn', 'fadeIn'), ('fadeInDown', 'fadeInDown'), ('fadeInDownBig', 'fadeInDownBig'), ('fadeInLeft', 'fadeInLeft'), ('fadeInLeftBig', 'fadeInLeftBig'), ('fadeInRight', 'fadeInRight'), ('fadeInRightBig', 'fadeInRightBig'), ('fadeInUp', 'fadeInUp'), ('fadeInUpBig', 'fadeInUpBig'), ('fadeOut', 'fadeOut'), ('fadeOutDown', 'fadeOutDown'), ('fadeOutDownBig', 'fadeOutDownBig'), ('fadeOutLeft', 'fadeOutLeft'), ('fadeOutLeftBig', 'fadeOutLeftBig'), ('fadeOutRight', 'fadeOutRight'), ('fadeOutRightBig', 'fadeOutRightBig'), ('fadeOutUp', 'fadeOutUp'), ('fadeOutUpBig', 'fadeOutUpBig'), ('flipInX', 'flipInX'), ('flipInY', 'flipInY'), ('flipOutX', 'flipOutX'), ('flipOutY', 'flipOutY'), ('lightSpeedIn', 'lightSpeedIn'), ('lightSpeedOut', 'lightSpeedOut'), ('rotateIn', 'rotateIn'), ('rotateInDownLeft', 'rotateInDownLeft'), ('rotateInDownRight', 'rotateInDownRight'), ('rotateInUpLeft', 'rotateInUpLeft'), ('rotateInUpRight', 'rotateInUpRight'), ('rotateOut', 'rotateOut'), ('rotateOutDownLeft', 'rotateOutDownLeft'), ('rotateOutDownRight', 'rotateOutDownRight'), ('rotateOutUpLeft', 'rotateOutUpLeft'), ('rotateOutUpRight', 'rotateOutUpRight'), ('hinge', 'hinge'), ('jackInTheBox', 'jackInTheBox'), ('rollIn', 'rollIn'), ('rollOut', 'rollOut'), ('zoomIn', 'zoomIn'), ('zoomInDown', 'zoomInDown'), ('zoomInLeft', 'zoomInLeft'), ('zoomInRight', 'zoomInRight'), ('zoomInUp', 'zoomInUp'), ('zoomOut', 'zoomOut'), ('zoomOutDown', 'zoomOutDown'), ('zoomOutLeft', 'zoomOutLeft'), ('zoomOutRight', 'zoomOutRight'), ('zoomOutUp', 'zoomOutUp'), ('slideInDown', 'slideInDown'), ('slideInLeft', 'slideInLeft'), ('slideInRight', 'slideInRight'), ('slideInUp', 'slideInUp'), ('slideOutDown', 'slideOutDown'), ('slideOutLeft', 'slideOutLeft'), ('slideOutRight', 'slideOutRight'), ('slideOutUp', 'slideOutUp')], help_text='Выбрать вид анимации, который будет применён к h3', max_length=250, verbose_name='Анимация h3'),
        ),
        migrations.AddField(
            model_name='aboutsliderimage',
            name='h3_is_animated',
            field=models.BooleanField(default=True, help_text='Добавить к h3 класс animated?', verbose_name='Animated h3?'),
        ),
        migrations.AddField(
            model_name='aboutsliderimage',
            name='h3_is_infinite',
            field=models.BooleanField(default=False, help_text='Добавить к h3 класс infinite?', verbose_name='infinite h3?'),
        ),
    ]
