# Generated by Django 4.2.7 on 2023-12-08 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_name', models.CharField(default=None, max_length=80)),
                ('complete_email', models.EmailField(max_length=254)),
                ('complete_password', models.CharField(default=None, max_length=20)),
                ('complete_image', models.ImageField(upload_to='media/')),
                ('complete_description', models.TextField()),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'CadastroUsuario',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('is_verified', models.BooleanField(default=False)),
                ('token', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastrousuario')),
            ],
            options={
                'db_table': 'Post',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.cadastrousuario')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='CadastroUsuarioHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_anterior', models.CharField(max_length=80)),
                ('descricao_anterior', models.TextField()),
                ('data_atualizacao', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastrousuario')),
            ],
            options={
                'db_table': 'CadastroUsuarioHistorico',
            },
        ),
        migrations.CreateModel(
            name='Banimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=255)),
                ('data_banimento', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastrousuario')),
            ],
        ),
    ]
