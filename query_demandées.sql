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

/*3*/
select m.specialite, count(dp.medicament_nom_commercial) as nb_medicament
from medecins m, dossiers_patients dp
where dp.medecin = m.nom and dp.inami_medecin = m.inami
group by m.specialite
order by nb_medicament desc
limit 1;

/*4*/
set @nom_commercial = '';
set @date_vente = '';
select pt.nom, dp.date_vente
from dossiers_patients dp, patient pt
where pt.NISS = dp.NISS_patient and medicament_nom_commercial = @nom_commercial and date_vente > @date_vente;

/*5*/
set @date = '2012-3-12';
select distinct p.prenom, p.nom, dp.DCI
from dossiers_patients dp, patient p
where dp.DCI in (
  select dp2.DCI
  from dossiers_patients dp2
  where dp2.date_vente < @date
  and dp2.NISS_patient = dp.NISS_patient 
  and p.NISS = dp.NISS_patient
  group by dp2.DCI
  having COUNT(*) > 1
);


/*6*/
select distinct m.nom, m.specialite, dp.medicament_nom_commercial
from medecins m, specialite s, dossiers_patients dp
where dp.medicament_nom_commercial 
not in
(select medicament from specialite where name = m.specialite) 
and m.specialite = s.name 
and m.inami = dp.inami_medecin;

/*7*/
select CONCAT(FLOOR(year(date_de_naissance)/10)*10, ' - ', FLOOR(year(date_de_naissance)/10)*10+9) as decennie, medicament_nom_commercial, COUNT(*) AS nb_patients
from dossiers_patients dp, patient p
where year(date_de_naissance) >= 1950 and year(date_de_naissance) < 2020 and dp.niss_patient = p.niss
group by decennie, medicament_nom_commercial
having COUNT(*) = (
  select COUNT(*)
  from dossiers_patients dp2, patient p2
  where(p2.date_de_naissance) >= 1950 and year(p2.date_de_naissance) < 2020 and dp2.niss_patient = p2.niss
  and CONCAT(FLOOR(year(p2.date_de_naissance)/10)*10, ' - ', FLOOR(year(p2.date_de_naissance)/10)*10+9) = decennie
  group by medicament_nom_commercial
  order by COUNT(*) desc
  limit 1
);


/*8*/
select pathology, count(*) as nb_diagnostiques
from diagnostiques
group by pathology
order by nb_diagnostiques desc
limit 1;

/*9*/
select p.nom, p.prenom, dp.medicament_nom_commercial, COUNT(distinct dp.medecin) as nb_medecins_prescripteurs
from patient p, dossiers_patients dp
where p.NISS = dp.niss_patient
group by p.niss, p.nom, p.prenom, dp.medicament_nom_commercial;

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