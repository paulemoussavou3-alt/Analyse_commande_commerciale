1)Analyse des commandes commer iales d'une entreprise et prédiction du Profit de ces dernières.

Utilisation de l'Analyse Exploratoire des données (EDA) et du Machine Learning afin de prédire les commandes commerciales de l'entreprise.

2)Contexte

Une entreprise souhaite prédire le profit d'une commande en prenant en compte le taux de remise appliquée sur la commande , le nombre d'unités vendus du / des produit(s) , le prix de l'unité , la catégorie du produit , la ville de livraison et le segment qui le reçoit.

3)Données

-Source : AfriAI

-Taille : 2500 lignes x 12 colonnes.

-Variable : Product_Category, Units_Sold , Unit_Price , Discount_% , City , Segment , Sales_Amount , Order_ID , Customer_Name , Customer_Name , Order_Date.

-Variable cible : Profit.

4)Méthodologie

-Nettoyage des données.

-Analyse Exploratoire des Données ( Analyse des corrélations , des statistiques descriptives et des visualisations ).

-Prédiction avec des modèles différents.

5)Résultats

-Pour qu'un modèle soit assez correct , nous devons avoir au moins un R2 supérieur à 0 mais pour nos deux modèles , nos R2 sont négatifs , ce qui signifie que les deux modèles sont à rejeter!!

-Pour les deux modèles on a un RMSE qui est très élevé ce qui est indicateur d'un mauvais modèle car nous savons que plus petit un RMSE est , meilleur un modèle est.

A l'issu de cette analyse , nous avons mit en place une interface Gradio qui permet d'utiliser le modèle mis en place. 
Je joins ci-après le lien de l'interface graphique : https://huggingface.co/spaces/2903paule/Prediction_profit

-Le MAE aussi traduit l'écart entre les valeurs réelles et les valeurs prédites  les deux MAE observées pour nos modèles sont très grands ce qui met en lumière une énorme différence dans les prédictions.

Après avoir mieux observé nos données , nous avons compris que les modèles n'étaient pas bons car les variables explicatives , n'expliquaient pas bien le modèle : aucune n'a une bonne corrélation avec la variable Profit.
