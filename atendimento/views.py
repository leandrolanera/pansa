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
    sql = "select distinct A.id, (A.name) as projeto,identifier as identificador," 
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

    try:
        with connections['redminedb'].cursor() as cursor:
            cursor.execute(sql)
            SasProjetos = dictfetchall(cursor)
        return render(request, 'lista-projetos.html',{'projects':SasProjetos})
    except:
       return render(request, 'erro.html') 
    

def detalhe_projeto(request, id):
    
    sql = "select A.name, A.identifier as indentificador,"
    sql = sql + " (select max(CC.name) from redmine.issues BB inner join redmine.versions CC ON (BB.fixed_version_id = CC.id)"
    sql = sql + "             where BB.project_id = A.id and BB.tracker_id = 23) as ultimaversao "
    sql = sql + " from redmine.projects A where id = % s" % id
    
    try:
        with connections['redminedb'].cursor() as cursor:
            cursor.execute(sql)
            ProjetoPrinc = dictfetchall(cursor)
    except:
       return render(request, 'erro.html') 

    sql = " select distinct C.name as versao,C.id as idVersao,C.description as descVersao,"
    sql = sql + " (A.name) as nome,A.identifier as identificador,"
    sql = sql + " count(B.id) as demandas,"
    sql = sql + " count(IF(B.closed_on is null,1,null)) as demabertas,"
    sql = sql + " count(IF(B.tracker_id=23,1,null)) as temaceite"
    sql = sql + " from redmine.projects A"
    sql = sql + " inner join redmine.issues B ON (A.id = B.project_id)"
    sql = sql + " inner join redmine.versions C ON (B.fixed_version_id = C.id)"
    sql = sql + " where A.id = % s" % id
    sql = sql + " group by C.name"
    sql = sql + " order by  INET_ATON(SUBSTRING_INDEX(CONCAT(C.name,'.0.0.0'),'.',4)) desc"

    try:
        with connections['redminedb'].cursor() as cursor:
            cursor.execute(sql)
            DetProjeto = dictfetchall(cursor)
        return render(request, 'detalhes-projeto.html',{'detalhesProjeto':DetProjeto, 'projetoPrinc':ProjetoPrinc})
    except:
       return render(request, 'erro.html') 
    

def lista_baseline(request, nomeVersao):
    
    # sql = "select A.name "
    # sql = sql + " from redmine.projects A where id = % s" % idProjeto
    
    # with connections['redminedb'].cursor() as cursor:
    #     cursor.execute(sql)
    #     ProjetoPrinc = dictfetchall(cursor)

    sql = "select distinct A.name as nome, "
    sql = sql + " case when (position(',' in GROUP_CONCAT(distinct C.name ORDER BY INET_ATON(SUBSTRING_INDEX(CONCAT(C.name,'.0.0.0'),'.',4)) DESC))) > 0 then "
    sql = sql + " 	SUBSTR(GROUP_CONCAT(distinct C.name ORDER BY INET_ATON(SUBSTRING_INDEX(CONCAT(C.name,'.0.0.0'),'.',4)) DESC),1,position(',' in GROUP_CONCAT(distinct C.name ORDER BY INET_ATON(SUBSTRING_INDEX(CONCAT(C.name,'.0.0.0'),'.',4)) DESC))-1) "
    sql = sql + " else GROUP_CONCAT(distinct C.name ORDER BY INET_ATON(SUBSTRING_INDEX(CONCAT(C.name,'.0.0.0'),'.',4)) DESC) "
    sql = sql + " end as versao "
    sql = sql + " from redmine.projects A "
    sql = sql + " inner join redmine.issues B ON (A.id = B.project_id) "
    sql = sql + " inner join redmine.versions C ON (B.fixed_version_id = C.id) "
    sql = sql + " where INET_ATON(SUBSTRING_INDEX(CONCAT(C.name,'.0.0.0'),'.',4)) <= INET_ATON(SUBSTRING_INDEX(CONCAT('% s','.0.0.0'),'.',4)) " % nomeVersao
    sql = sql + " and A.parent_id = 166"
    sql = sql + " group by A.name "

    try:
        with connections['redminedb'].cursor() as cursor:
            cursor.execute(sql)
            baseline = dictfetchall(cursor)
        return render(request, 'lista-baseline.html',{'baseline':baseline, 'nomeVersao':nomeVersao})
    except:
       return render(request, 'erro.html') 
    
def lista_versoes(request):
    sql = "select distinct  C.name, C.description,C.id," 
    sql = sql + " count(distinct A.id) as sistemas" 
    sql = sql + " from redmine.projects A" 
    sql = sql + " left join redmine.issues B ON (A.id = B.project_id)" 
    sql = sql + " left join redmine.versions C ON (B.fixed_version_id = C.id)" 
    sql = sql + " where  A.parent_id = 166" 
    sql = sql + " group by C.name" 
    sql = sql + " order by INET_ATON(SUBSTRING_INDEX(CONCAT(C.name,'.0.0.0'),'.',4)) desc"

    try:
        with connections['redminedb'].cursor() as cursor:
            cursor.execute(sql)
            SasVersoes = dictfetchall(cursor)
        return render(request, 'lista-versoes.html',{'versoes':SasVersoes})
    except:
       return render(request, 'erro.html') 
        