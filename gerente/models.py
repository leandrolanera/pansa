from django.db import models

class IssueCategories(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=60)
    assigned_to_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_categories'


class IssueRelations(models.Model):
    issue_from_id = models.IntegerField()
    issue_to_id = models.IntegerField()
    relation_type = models.CharField(max_length=255)
    delay = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_relations'
        unique_together = (('issue_from_id', 'issue_to_id'),)


class IssueStatuses(models.Model):
    name = models.CharField(max_length=30)
    is_closed = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    default_done_ratio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_statuses'


class Issues(models.Model):
    tracker_id = models.IntegerField()
    project_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField()
    assigned_to_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField()
    fixed_version_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField()
    lock_version = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    is_private = models.IntegerField()
    closed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'

class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    inherit_members = models.IntegerField()
    default_version_id = models.IntegerField(blank=True, null=True)
    default_assigned_to_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'
        ordering = ['name']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
    
    def __str__(self):
        # return self.name
        return "%s - %s" % (self.name, self.description)



class ProjectsTrackers(models.Model):
    project_id = models.IntegerField()
    tracker_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projects_trackers'
        unique_together = (('project_id', 'tracker_id'),)

class Versions(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    wiki_page_title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sharing = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'versions'


