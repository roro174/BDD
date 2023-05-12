select CONCAT(FLOOR(year(date_de_naissance)/10)*10, ' - ', FLOOR(year(date_de_naissance)/10)*10+9) as decennie, medicament_nom_commercial, COUNT(*) AS nb_patients
from dossiers_patients dp, patient p
where year(date_de_naissance) >= 1950 and year(date_de_naissance) < 2020 and dp.niss_patient = p.niss
group by decennie, medicament_nom_commercial
having COUNT(*) = (
  select COUNT(*)
  from dossiers_patients dp2, patient p2
  where(p2.date_de_naissance) >= 1950 and year(p2.date_de_naissance) < 2020 and dp2.niss_patient = p2.niss
  and CONCAT(FLOOR(year(p2.date_de_naissance)/10)*10, ' - ', FLOOR(year(p2.date_de_naissance)/10)*10+9) = decennie
  group by medicament_nom_commercial
  order by COUNT(*) desc
  limit 1
);