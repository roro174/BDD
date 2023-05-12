set @date = '';
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