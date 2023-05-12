select pathology, count(*) as nb_diagnostiques
from diagnostiques
group by pathology
order by nb_diagnostiques desc
limit 1;