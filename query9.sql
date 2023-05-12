select p.nom, p.prenom, dp.medicament_nom_commercial, COUNT(distinct dp.medecin) as nb_medecins_prescripteurs
from patient p, dossiers_patients dp
where p.NISS = dp.niss_patient
group by p.niss, p.nom, p.prenom, dp.medicament_nom_commercial;