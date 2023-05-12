CREATE TABLE dossiers_patients(
NISS_patient bigint NULL,
medecin char(255)  NULL,
inami_medecin bigint  NULL,
pharmacien char(255)  NULL,
inami_pharmacien bigint  NULL,
medicament_nom_commercial char(255)  NULL,
DCI char(255)  NULL,
date_prescription date  NULL,
date_vente date  NULL,
duree_traitement int  NULL
);

LOAD DATA
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\dossiers_patients.csv'
INTO TABLE dossiers_patients
FIELDS TERMINATED BY ','
IGNORE 1 LINES
(NISS_patient,medecin,inami_medecin,pharmacien,inami_pharmacien,medicament_nom_commercial,DCI,@date_prescription,@date_vente,duree_traitement)
set date_prescription = str_to_date(@date_prescription, '%m/%d/%Y'),
date_vente = str_to_date(@date_vente, '%m/%d/%Y');

CREATE TABLE medicaments(
DCI char(255),
nom_commercial char(255),
système_anatomique char (255),
conditionnement int
);

LOAD DATA
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\medicaments.csv'
INTO TABLE medicaments
FIELDS TERMINATED BY ','
IGNORE 1 LINES;

CREATE TABLE diagnostiques(
NISS bigint,
date_diagnostic date,
naissance date,
pathology char(255),
specialite char(255)
);

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\diagnostiques.xml'
INTO TABLE diagnostiques
ROWS IDENTIFIED BY '<diagnostique>'
(NISS, @date_diagnostic, @naissance, pathology, specialite)
set date_diagnostic = str_to_date(@date_diagnostic, '%m/%d/%Y'),
naissance = str_to_date(@naissance, '%m/%d/%Y');

CREATE TABLE medecins(
inami bigint,
mail char(255),
nom char(255),
specialite char(255),
telephone bigint
);

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\medecins.xml'
INTO TABLE medecins
ROWS IDENTIFIED BY '<medecin>';

CREATE TABLE pathologies(
pathology char(255),
specialite char(255)
);

LOAD DATA
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pathologies.csv'
INTO TABLE pathologies
FIELDS TERMINATED BY ',';

CREATE TABLE patient(
NISS bigint,
date_de_naissance date,
genre int,
inami_medecin bigint,
inami_pharmacien bigint,
mail char(255),
nom char(255),
prenom char(255),
telephone bigint
);

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\patient.xml'
INTO TABLE patient
ROWS IDENTIFIED BY '<patient>'
(NISS, @date_de_naissance, genre, inami_medecin, inami_pharmacien, mail, nom, prenom, telephone)
set date_de_naissance = str_to_date(@date_de_naissance, '%m/%d/%Y');

drop table pharmacien;
CREATE TABLE pharmacien(
inami bigint,
mail char(255),
nom char(255),
tel bigint
);

LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pharmaciens.xml'
INTO TABLE pharmacien
ROWS IDENTIFIED BY '<pharmacien>';

/*Problème car le nombre d'attributs par tuples varie (voir comment faire ça)*/


CREATE TABLE specialite(
name char(255),
medicament char(255)
);
LOAD XML
INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\specialites.xml'
INTO TABLE specialite
ROWS IDENTIFIED BY '<medicament>';


