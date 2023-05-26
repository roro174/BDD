select distinct m.inami, m.nom, m.specialite
from medecins m
inner join dossiers_patients dp on m.inami = dp.inami_medecin
inner join medicaments me on dp.medicament_nom_commercial = me.nom_commercial
inner join specialite s on me.système_anatomique = s.medicament
where s.name <> m.specialite
order by m.nom;