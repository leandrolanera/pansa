# Generated by Django 2.2.19 on 2021-05-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IssueCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('name', models.CharField(max_length=60)),
                ('assigned_to_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'issue_categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IssueRelations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_from_id', models.IntegerField()),
                ('issue_to_id', models.IntegerField()),
                ('relation_type', models.CharField(max_length=255)),
                ('delay', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'issue_relations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracker_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('category_id', models.IntegerField(blank=True, null=True)),
                ('status_id', models.IntegerField()),
                ('assigned_to_id', models.IntegerField(blank=True, null=True)),
                ('priority_id', models.IntegerField()),
                ('fixed_version_id', models.IntegerField(blank=True, null=True)),
                ('author_id', models.IntegerField()),
                ('lock_version', models.IntegerField()),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('done_ratio', models.IntegerField()),
                ('estimated_hours', models.FloatField(blank=True, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('root_id', models.IntegerField(blank=True, null=True)),
                ('lft', models.IntegerField(blank=True, null=True)),
                ('rgt', models.IntegerField(blank=True, null=True)),
                ('is_private', models.IntegerField()),
                ('closed_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'issues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IssueStatuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_closed', models.IntegerField()),
                ('position', models.IntegerField(blank=True, null=True)),
                ('default_done_ratio', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'issue_statuses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('homepage', models.CharField(blank=True, max_length=255, null=True)),
                ('is_public', models.IntegerField()),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('identifier', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField()),
                ('lft', models.IntegerField(blank=True, null=True)),
                ('rgt', models.IntegerField(blank=True, null=True)),
                ('inherit_members', models.IntegerField()),
                ('default_version_id', models.IntegerField(blank=True, null=True)),
                ('default_assigned_to_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectsTrackers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('tracker_id', models.IntegerField()),
            ],
            options={
                'db_table': 'projects_trackers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Versions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('wiki_page_title', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('sharing', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'versions',
                'managed': False,
            },
        ),
    ]
