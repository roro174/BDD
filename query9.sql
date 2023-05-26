select p.nom, p.prenom, count(distinct dp.medecin) as nb_medecins_prescripteurs
from patient p, dossiers_patients dp
where p.NISS = dp.niss_patient
group by p.nom, p.prenom
order by p.nom;
