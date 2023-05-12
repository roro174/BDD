select pathology, count(distinct specialite) as nb_specialites 
from pathologies 
group by pathology 
having nb_specialites = 1;