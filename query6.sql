select distinct m.nom, m.specialite, group_concat(distinct dp.medicament_nom_commercial separator ', ') as medicaments_prescrits
from medecins m, specialite s, dossiers_patients dp
where m.specialite = s.name and m.inami = dp.inami_medecin and dp.medicament_nom_commercial 
not in
(select medicament from specialite where name = m.specialite) 
group by m.nom, m.specialite;