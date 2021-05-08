from django.shortcuts import render
from .models import Projects
from .forms import ProjectsForm
from django.db import connections
from django.db import connection


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
    sql = "select distinct A.id, (A.name) as projeto," 
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

def detalhe_projeto(request, id):
    
    sql = "select A.name, "
    sql = sql + " (select max(CC.name) from redmine.issues BB inner join redmine.versions CC ON (BB.fixed_version_id = CC.id)"
    sql = sql + "             where BB.project_id = A.id and BB.tracker_id = 23) as ultimaversao "
    sql = sql + " from redmine.projects A where id = % s" % id
    
    with connections['redminedb'].cursor() as cursor:
        cursor.execute(sql)
        ProjetoPrinc = dictfetchall(cursor)

    sql = " select distinct C.name as versao,"
    sql = sql + " (A.name) as nome,"
    sql = sql + " count(B.id) as demandas,"
    sql = sql + " count(IF(B.closed_on is null,1,null)) as demabertas,"
    sql = sql + " count(IF(B.tracker_id=23,1,null)) as temaceite"
    sql = sql + " from redmine.projects A"
    sql = sql + " inner join redmine.issues B ON (A.id = B.project_id)"
    sql = sql + " inner join redmine.versions C ON (B.fixed_version_id = C.id)"
    sql = sql + " where A.id = % s" % id
    sql = sql + " group by C.name"
    sql = sql + " order by  C.name desc"

    with connections['redminedb'].cursor() as cursor:
        cursor.execute(sql)
        DetProjeto = dictfetchall(cursor)

    return render(request, 'detalhes-projeto.html',{'detalhesProjeto':DetProjeto, 'projetoPrinc':ProjetoPrinc})