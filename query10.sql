set @date_prescription = '';
select distinct medicament_nom_commercial
from dossiers_patients
where date_prescription <  @date_prescription and medicament_nom 
not in (
  select medicament_nom 
  from dossiers_patients 
  where date_prescription >=  @date_prescription
);