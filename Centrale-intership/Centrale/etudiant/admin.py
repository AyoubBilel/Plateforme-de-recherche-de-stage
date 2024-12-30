from django.contrib import admin
from.models import Users,Secteur,Entreprise,Offre_de_stage,Stage,Alumnis,Candidature
# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','password','username']

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display=['id','nom','secteur','description','logo_url','ville','lien_map_ville','lien_page_web']

@admin.register(Secteur)
class SecteurAdmin(admin.ModelAdmin):
    list_display=['id','nom','description']


@admin.register(Offre_de_stage)
class Offre_de_stageAdmin(admin.ModelAdmin):
    list_display = ['id','titre','secteur','description','type_stage','entrprise','durée','ville','RH_email','date_de_publication','logo_url','stage_valide']
    list_editable = ('titre','secteur','description','type_stage','entrprise','durée','ville','RH_email','logo_url')

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display=['id','type','secteur','entreprise']

@admin.register(Alumnis)
class AlumnisAdmin(admin.ModelAdmin):
    list_display=['nom', 'prenom', 'promotion', 'email', 'linkdn', 'photo', 'numero', 'stage_1A_ville', 'stage_1A_secteur', 'stage_1A_entreprise','stage_2A_ville', 'stage_2A_secteur', 'stage_2A_entreprise','stage_3A_ville', 'stage_3A_secteur', 'stage_3A_entreprise', 'emploi_secteur','emploi_entreprise']

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    pass


#----------------------------------------------------------------------------------------------------------------
#PARTIE SERVICE DE SCOLARITE
from .models import Service_users
@admin.register(Service_users)
class Service_usersAdmin(admin.ModelAdmin):
        list_display = ['first_name','last_name','email','password','username']

 #--------------------------------------------------------------------------------------------------------------
 #PARTIE SERVICE RH 
from .models import Rh_service,Rh_favories,Portfolio
@admin.register(Rh_service)
class Rh_serviceAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','password','username','entreprise','secteur']
    
@admin.register(Rh_favories)
class Rh_favorieAdmin(admin.ModelAdmin):
    list_display = ['RH','candidature']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'photo', 
        'specialite', 
        'introduction', 
        'formation', 
        'experiences_professionnelles', 
        'competences_techniques', 
        'soft_skills', 
        'projets_realises', 
        'certifications', 
        'publications', 
        'activites_extrascolaires', 
        'references'
    ]

 
   
from django.contrib import admin

# Register your models here.
# chatbot/admin.py

from django.contrib import admin
from .models import Sector, InterviewSession, InterviewQuestion

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(InterviewSession)
class InterviewSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sector', 'date')
    list_filter = ('date', 'sector')
    search_fields = ('user__username', 'sector__name')

@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'question', 'score')
    list_filter = ('session', 'score')
    search_fields = ('question', 'user_response', 'feedback')

