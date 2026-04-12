import pickle
import numpy as np


with open ("model1.pkl", "rb") as f:
    model=pickle.load(f)

with open ("label_encoder1.pkl", "rb") as f:
    label_encoder1=pickle.load(f)

with open ("label_encoder2.pkl", "rb") as f:
    label_encoder2=pickle.load(f)

with open ("label_encoder3.pkl", "rb") as f:
    label_encoder3=pickle.load(f)

print(label_encoder1.classes_)
print(label_encoder2.classes_)
print(label_encoder3.classes_)

def predire_profit(product_category,unit_sold,unit_price,discount,city,segment):
    try:
        product_encoded=label_encoder3.transform([product_category])[0]
        city_encoded=label_encoder1.transform([city])[0]
        segment_encoded=label_encoder2.transform([segment])[0]
        data= np.array([[product_encoded,unit_sold,unit_price,discount,city_encoded,segment_encoded]])
        
        #Prediction profit
        profit=model.predict(data)[0]
        return f"profit estimé:$ {profit}"
    except Exception as e:
        return f"Erreur: {str(e)}"
    
import gradio as gr

theme = gr.themes.Soft(
    primary_hue="blue",      
    secondary_hue="orange",      
    neutral_hue="gray",        
    font=gr.themes.GoogleFont("Arial")  
)

interface=gr.Interface(
    fn=predire_profit,
    inputs=[
        gr.Dropdown(
            choices=["Accessories","Dresses","Jackets","Jeans","Shoes","T-Shirts'"],
            label="Catégorie de produits",
        ),
        #gr.Slider(
            #minimum=1,
            #maximum=5,
            #step=1,
            #label="Catégorie de produits :T-Shirts=0,Dresses=1,Shoes=2,Jeans=3,Accessories=4,jackets=5 ",
        #),
         gr.Slider(
            minimum=1,
            maximum=1000,
            step=1,
            label="Nombre de produit",
        ),
        gr.Slider(
            minimum=1,
            maximum=1000000,
            step=1,
            label="Prix du produit",
        ),
        gr.Slider(
            minimum=0,
            maximum=100,
            step=1,
            label="Pourcentage de la remise",
        ),
        gr.Dropdown(
            choices=["Ahmedabad","Bangalore","Delhi","Hyd","Hyderabad","Mumbai","Bangalore","Pune","bengaluru","hyderbad"],
            label="Ville",
        ),
        #gr.Slider(
            #minimum=0,
            #maximum=5,
            #step=1,
            #label="Catégorie de produits :Ahmedabad=0,Bangalore=1,Delhi=2,Hyd=3,Hyderabad=4,Mumbai=5,Bangalore=6,Pune=7,bengaluru=8,hyderbad=9",
        #),

        gr.Dropdown(
            choices=["B2C","B2B","Autre"],
            label="Segment",
        ),
        #gr.Slider(
            #minimum=0,
            #maximum=2,
            #step=1,
            #label="Segment :Autre=0, B2B=1, B2C=2",
        #),
        
    ],
    outputs=gr.Textbox(label="Profit prédit"),
    title="Prédiction du profit des commandes commerciales",
    description=("Entrez les caractéristiques de la commande commerciale pour préfire le profit et sélectionnez le modèle présent"),
    theme=theme
)
interface.launch()