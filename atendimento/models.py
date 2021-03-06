from django.db import models

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

class Versions(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    wiki_page_title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sharing = models.CharField(max_length=255)

    projeto_factor = models.PositiveSmallIntegerField(
        help_text="Projeto de uma versao",
        default=50
    )

    class Meta:
        managed = False
        db_table = 'versions'

class Issues(models.Model):
    tracker_id = models.IntegerField()
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
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