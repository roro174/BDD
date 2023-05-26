CREATE SCHEMA patient_informatise;

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
duree_traitement int  NULL,
PRIMARY KEY (NISS_patient)
);

CREATE TABLE medicaments(
DCI char(255),
nom_commercial char(255),
système_anatomique char (255),
conditionnement int,
PRIMARY KEY (DCI)
);

CREATE TABLE diagnostiques(
NISS bigint,
date_diagnostic date,
naissance date,
pathology char(255),
specialite char(255),
PRIMARY KEY (NISS)
);

CREATE TABLE medecins(
inami bigint,
mail char(255),
nom char(255),
specialite char(255),
telephone bigint,
PRIMARY KEY (inami)
);

CREATE TABLE pathologies(
pathology char(255),
specialite char(255),
PRIMARY KEY (pathology)
);

CREATE TABLE patient(
NISS bigint,
date_de_naissance date,
genre int,
inami_medecin bigint,
inami_pharmacien bigint,
mail char(255),
nom char(255),
prenom char(255),
telephone bigint,
PRIMARY KEY (NISS)
);

CREATE TABLE pharmacien(
inami bigint,
mail char(255),
nom char(255),
tel bigint,
PRIMARY KEY (inami)
);

CREATE TABLE specialite(
name char(255),
medicament char(255),
PRIMARY KEY (name)
);