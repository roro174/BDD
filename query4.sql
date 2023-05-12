set @nom_commercial = '';
set @date_vente = '';
select pt.nom, dp.date_vente
from dossiers_patients dp, patient pt
where pt.NISS = dp.NISS_patient and medicament_nom_commercial = @nom_commercial and date_vente > @date_vente;