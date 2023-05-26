set @nom_commercial = '$1';
set @date_vente = '$2';
select pt.nom, dp.date_vente
from dossiers_patients dp, patient pt
where pt.NISS = dp.NISS_patient and medicament_nom_commercial = @nom_commercial and date_vente > @date_vente;