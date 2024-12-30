from django import forms
from .models import Candidature,Offre_de_stage,Entreprise,Secteur,Users,Alumnis,Stage,Portfolio

class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['cv', 'lettre']
        widgets = {
            'cv': forms.FileInput(attrs={'class': 'form-control'}),
            'lettre': forms.FileInput(attrs={'class': 'form-control'}),
        }

class OffreDeStageForm(forms.ModelForm):
    class Meta:
        model = Offre_de_stage
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'offre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'Missions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Missions'}),
            'Profil_recherché': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Profil recherché'}),
            'Ce_que_nous_offrons': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ce que nous offrons'}),
            'secteur':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Secteur'}),
            'type_stage': forms.Select(attrs={'class': 'form-control'}),
            'entrprise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrprise'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'RH_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email RH'}),
            'logo_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL du logo'}),
            'durée': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Durée en mois'}),
            'validé':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'valide?'}),
        }
        
        
        
class RHOffreDeStageForm(forms.ModelForm):
    class Meta:
        model = Offre_de_stage
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'offre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'Missions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Missions'}),
            'Profil_recherché': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Profil recherché'}),
            'Ce_que_nous_offrons': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ce que nous offrons'}),
            'secteur':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Secteur'}),
            'type_stage': forms.Select(attrs={'class': 'form-control'}),
            'entrprise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrprise'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'RH_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email RH'}),
            'logo_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL du logo'}),
            'durée': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Durée en mois'}),
        }
      
        
        
class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['nom', 'secteur', 'description', 'ville', 'lien_map_ville', 'logo_url', 'lien_page_web']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'entreprise'}),
            'secteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Secteur'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description de l\'entreprise'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'lien_map_ville': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Lien Google Maps'}),
            'logo_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL du logo'}),
            'lien_page_web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Lien de la page web'}),
        }
        

class SecteurForm(forms.ModelForm):
    class Meta:
        model = Secteur
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du secteur'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description du secteur'}),
        }
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email', 'password','annee_etude']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse e-mail'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
            'annee_etude':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'année d\'etude'}),
            
        }


class AlumnisForm(forms.ModelForm):
    class Meta:
        model = Alumnis
        fields = ['nom', 'prenom', 'promotion', 'email', 'linkdn', 'photo', 'numero', 'stage_1A_ville', 'stage_1A_secteur', 'stage_1A_entreprise','stage_2A_ville', 'stage_2A_secteur', 'stage_2A_entreprise','stage_3A_ville', 'stage_3A_secteur', 'stage_3A_entreprise', 'emploi_secteur','emploi_entreprise']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'promotion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promotion'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'linkdn': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
            'stage_1A_entreprise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_1A_Entreprise'}),
            'stage_1A_secteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_1A_Secteur'}),
            'stage_1A_ville':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_1A_Ville'}),
            'stage_2A_entreprise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_2A_Entreprise'}),
            'stage_2A_secteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_2A_Secteur'}),
            'stage_2A_ville':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_2A_Ville'}),
            'stage_3A_entreprise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_3A_Entreprise'}),
            'stage_3A_secteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_3A_Secteur'}),
            'stage_3A_ville':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stage_3A_Ville'}),
            'emploi_entreprise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'emploi_Entreprise'}),
            'emploi_secteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'emploi_Secteur'}),


            'emploi': forms.Select(attrs={'class': 'form-control'}),
        }
        
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['type', 'secteur', 'entreprise']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'secteur': forms.Select(attrs={'class': 'form-control'}),
            'entreprise': forms.Select(attrs={'class': 'form-control'}),
        }
        


from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ['user']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spécialité'}),
            'introduction': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Brève présentation personnelle, objectifs professionnels, résumé des compétences principales.'}),
            'formation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Informations sur la formation académique, diplômes obtenus, projets académiques significatifs.'}),
            'experiences_professionnelles': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Stagiaires, alternances, emplois avec détails des responsabilités et réalisations'}),
            'competences_techniques': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'competences_techniques'}),
            'soft_skills': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Soft skills'}),
            'projets_realises': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description détaillée des projets significatifs.'}),
            'certifications': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Certifications techniques et formations suivies.'}),
            'publications': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Articles publiés et participation à des conférences.'}),
            'activites_extrascolaires': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Activités extrascolaires'}),
            'references': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Références'}),
        }



from django import forms
from .models import Sector

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['name']
