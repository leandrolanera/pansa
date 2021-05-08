from django.shortcuts import render
from .models import Projects
from .forms import ProjectsForm
from django.db import connections


def home(request):
    return render(request, 'home.html')
    
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def lista_projetos(request):
    sql = "select distinct (A.name) as projeto," 
    sql = sql +  " count(B.id) as demandas,"
    sql = sql +  " (select max(CC.name) from redmine.issues BB inner join redmine.versions CC ON (BB.fixed_version_id = CC.id) "
    sql = sql +  " where BB.project_id = A.id and BB.tracker_id = 23) as ultimaversao"
    sql = sql +  " from redmine.projects A"
    sql = sql +  " inner join redmine.issues B ON (A.id = B.project_id)"
    sql = sql +  " inner join redmine.versions C ON (B.fixed_version_id = C.id)"
    sql = sql +  " where A.parent_id = 166"
    sql = sql +  " and C.id = (select max(CC.id) from redmine.issues BB "
    sql = sql +  "              inner join redmine.versions CC ON (BB.fixed_version_id = CC.id) where BB.project_id = A.id and BB.tracker_id = 23)"
    sql = sql +  " group by A.name"
    sql = sql +  " order by A.name"

    with connections['redminedb'].cursor() as cursor:
        cursor.execute(sql)
        SasProjetos = dictfetchall(cursor)
    
    return render(request, 'lista-projetos.html',{'projects':SasProjetos})