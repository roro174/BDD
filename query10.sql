set @date_prescription = '';
select distinct medicament_nom_commercial
from dossiers_patients
where date_prescription <  @date_prescription and medicament_nom_commercial
not in (
  select medicament_nom_commercial 
  from dossiers_patients 
  where date_prescription >=  @date_prescription
);