# Projet : Nettoyage et Analyse de Transactions Bancaires (FinanceCore)

## Description
Ce projet automatise le processus de nettoyage, de détection d'anomalies et d'ingénierie de données pour un dataset de transactions bancaires. Il fait partie d'un pipeline de données robuste conçu pour transformer des données brutes en un ensemble de données prêt pour l'analyse ou le machine learning.

## Structure du Projet
Le projet est organisé de la manière suivante :

- `main.py` : Le point d'entrée principal qui orchestre tout le pipeline.
- `src/` : Contient les modules de traitement :
    - `import_data.py` : Chargement des données à partir de fichiers CSV.
    - `data_cleaning.py` : Nettoyage (doublons, types de données, valeurs manquantes).
    - `anomaly_detection.py` : Détection des valeurs aberrantes (Outliers) sur les montants et les scores de crédit.
    - `feature_engineering.py` : Création de nouvelles variables (temporelles, indicateurs de risque, vérification EUR).
    - `export_data.py` : Validation finale et exportation des données nettoyées.
- `data/` : Dossier contenant le dataset source (`bank-transactions.csv`).
- `output/` : Dossier où les résultats nettoyés sont sauvegardés (`financecore_clean.csv`).
- `notebooks/` : Contient des notebooks Jupyter pour l'exploration interactive.
- `JSON – PlanificationProjetFinanceCore/` : Documentation de planification du projet.

## Fonctionnalités Principales

### 1. Nettoyage des Données (`data_cleaning.py`)
- Suppression des doublons basés sur `transaction_id`.
- Conversion et harmonisation des formats de dates.
- Nettoyage des chaînes de caractères (suppression d'espaces, standardisation de la casse).
- Gestion des valeurs manquantes par imputation (médienne pour les scores, mode pour les agences).

### 2. Détection d'Anomalies (`anomaly_detection.py`)
- Détection des montants suspects via la méthode IQR (Interquartile Range).
- Identification des scores de crédit hors normes (inférieur à 0 ou supérieur à 850).
- Marquage global des anomalies (`is_anomaly`).

### 3. Ingénierie de Données (`feature_engineering.py`)
- Extraction temporelle : Année, Mois, Trimestre, Jour de la semaine.
- Validation des calculs de devises (vérification de la conversion en EUR).
- Catégorisation du risque client (High, Medium, Low) basée sur le `score_credit_client`.

## Installation et Utilisation

### Prérequis
- Python 3.x
- Pandas
- Scipy
- Numpy

### Installation
Clonez le dépôt et installez les dépendances nécessaires :
```bash
pip install pandas scipy numpy
```

### Exécution
Pour lancer le pipeline complet, exécutez simplement le fichier `main.py` :
```bash
python main.py
```

## Validation finale
Le script affiche un résumé des données après traitement, incluant :
- Le nombre de doublons restants.
- Les valeurs manquantes restantes.
- Les statistiques descriptives du dataset final.
- La forme (shape) du DataFrame.

---
*Ce projet a été réalisé dans le cadre d'une formation Simplon.*
