select m.specialite, count(dp.medicament_nom_commercial) as nb_medicament
from medecins m, dossiers_patients dp
where dp.medecin = m.nom and dp.inami_medecin = m.inami
group by m.specialite
order by nb_medicament desc
limit 1;