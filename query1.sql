set @nom_dci = '$1';
select nom_commercial, conditionnement
from medicaments
where DCI = @nom_dci
order by nom_commercial asc, conditionnement asc;