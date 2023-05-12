/*1*/
set @nom_dci = '';
select nom_commercial, conditionnement
from medicaments
where DCI = @nom_dci
order by nom_commercial asc, conditionnement asc;

/*2*/
/*retourne les pathologies qui sont traités par un type de spécialiste (y en a 119)*/ 
select pathology, count(distinct specialite) as nb_specialites 
from pathologies 
group by pathology 
having nb_specialites = 1;

/*4*/
set @nom_commercial = '';
set @date_vente = '';
select pt.nom, dp.date_vente
from dossiers_patients dp, patient pt
where pt.NISS = dp.NISS_patient and medicament_nom_commercial = @nom_commercial and date_vente > @date_vente;

/*5*/
/*Date vente ou date prescription*/
set @date_vente = '';
select pt.nom, dp.DCI
from dossiers_patients dp, patient pt
where pt.NISS = dp.NISS_patient and date_vente < @date_vente; 

/*6*/
/*7*/

/*8*/
select pathology, count(*) as nb_diagnostiques
from diagnostiques
group by pathology
order by nb_diagnostiques desc
limit 1;

/*9*/
select p.nom, p.prenom, COUNT(distinct dp.medecin) as nb_medecins_prescripteurs
from patient p
inner join dossiers_patients dp on p.niss = dp.niss_patient
group by p.niss, p.nom, p.prenom;

/*10*/
set @date_prescription = '';
select distinct medicament_nom_commercial
from dossiers_patients
where date_prescription <  @date_prescription and medicament_nom 
not in (
  select medicament_nom 
  from dossiers_patients 
  where date_prescription >=  @date_prescription
);