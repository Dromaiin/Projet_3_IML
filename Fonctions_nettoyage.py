#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


# Création d'une fonction pour supprimer les valeurs manquantes par colonne
def supprimer_colonne_vide(data : pd.DataFrame , pourcentage_val_manquantes : float) -> pd.DataFrame:
    """
    Fonction pour supprimer des colonnes en spécifiant le pourcentage de valeurs manquantes dans la colonne
    """
    colonne_a_garder = []
    for colonne in data.columns:
        if data[colonne].isna().sum()/data.shape[0] <= pourcentage_val_manquantes:
            colonne_a_garder.append(colonne)
    return data[colonne_a_garder]

# Création fonction pour observer les valeurs manquantes par colonne
def pourcentage_val_manquantes(data : pd.DataFrame):
    """
    Fonction qui sort un DataFrame avec 3 colonnes, les variables, le pourcentage de valeurs manquantes par variable et le nombre de valeurs manquantes
    """
    dataframe = pd.DataFrame(columns=['Variable', 'Pourcentage_valeurs_manquantes','Valeurs_manquantes'])
    dataframe['Variable'] = data.columns
    val_manquantes = list()
    val_manquantes_pourcentage = list()
    for col in data.columns:
        val1 = data[col].isna().sum().sum()
        val2 = data[col].isna().sum()/data.shape[0]
        val_manquantes.append(val1)
        val_manquantes_pourcentage.append(val2)
    dataframe['Pourcentage_valeurs_manquantes'] = list(val_manquantes_pourcentage)
    dataframe['Valeurs_manquantes'] = list(val_manquantes)
        
    return dataframe.sort_values(by = 'Pourcentage_valeurs_manquantes', ascending = False)

# Création fonction pour observer sous forme de graphique en bar le % de valeurs manquantes par colonne
def plot_pourcentage_val_manquantes_par_variable(data: pd.DataFrame, sample=False):
    """
    Mettre un échantillon du jeu de données si le dataset est trop lourd
    Permet d'afficher le pourcentage de valeur manquantes/non manquantes par variable sous forme de graphique en bar
    """
    if sample:
        subdata = data.sample(frac=0.5)
    else:
        subdata = data
    sns.displot(data=subdata.isna().melt(value_name="missing"),y="variable",hue="missing",multiple="fill",aspect=3.25)
    plt.gcf().set_size_inches(20, 30)


#Remplacer valeur manquantes pas un string
def remplacer_valeurs_manquantes_string(data: pd.DataFrame, colonne: str, valeur: str) -> pd.DataFrame:
    """
    Renseigner le jeu de données ainsi que la colonne dans laquelle on veut remplacer les valeurs. Enfin, il faut écrire par quoi on veut remplacer les valeurs manquantes
    """
    data[colonne] = data[colonne].fillna(valeur)

