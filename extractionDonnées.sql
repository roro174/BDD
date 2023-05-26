LOAD DATA
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\dossiers_patients.csv'
INTO TABLE dossiers_patients
FIELDS TERMINATED BY ','
IGNORE 1 LINES
(NISS_patient,medecin,inami_medecin,pharmacien,inami_pharmacien,medicament_nom_commercial,DCI,@date_prescription,@date_vente,duree_traitement)
set date_prescription = str_to_date(@date_prescription, '%m/%d/%Y'),
date_vente = str_to_date(@date_vente, '%m/%d/%Y');

LOAD DATA
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\medicaments.csv'
INTO TABLE medicaments
FIELDS TERMINATED BY ','
IGNORE 1 LINES;

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\diagnostiques.xml'
INTO TABLE diagnostiques
ROWS IDENTIFIED BY '<diagnostique>'
(NISS, @date_diagnostic, @naissance, pathology, specialite)
set date_diagnostic = str_to_date(@date_diagnostic, '%m/%d/%Y'),
naissance = str_to_date(@naissance, '%m/%d/%Y');

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\medecins.xml'
INTO TABLE medecins
ROWS IDENTIFIED BY '<medecin>';

LOAD DATA
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pathologies.csv'
INTO TABLE pathologies
FIELDS TERMINATED BY ',';

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\patient.xml'
INTO TABLE patient
ROWS IDENTIFIED BY '<patient>'
(NISS, @date_de_naissance, genre, inami_medecin, inami_pharmacien, mail, nom, prenom, telephone)
set date_de_naissance = str_to_date(@date_de_naissance, '%m/%d/%Y');

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pharmaciens.xml'
INTO TABLE pharmacien
ROWS IDENTIFIED BY '<pharmacien>';

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\specialites.xml'
INTO TABLE specialite
ROWS IDENTIFIED BY '<medicament>';