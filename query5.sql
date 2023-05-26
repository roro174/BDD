set @date = '';
set @dci = '';
select distinct p.prenom, p.nom, dp.DCI
from dossiers_patients dp, patient p
where dp.NISS_patient = p.NISS 
and date_add(dp.date_prescription, interval dp.duree_traitement day)  < @date 
and dp.DCI = @dci;