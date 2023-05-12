select distinct m.nom, m.specialite, dp.medicament_nom_commercial
from medecins m, specialite s, dossiers_patients dp
where dp.medicament_nom_commercial 
not in
(select medicament from specialite where name = m.specialite) 
and m.specialite = s.name 
and m.inami = dp.inami_medecin;