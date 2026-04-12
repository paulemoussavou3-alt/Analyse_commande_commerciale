import pickle
import numpy as np

with open ("model1.pkl", "rb") as f:
    model=pickle.load(f)

with open ("label_encoder.pkl", "rb") as f:
    label_encoder=pickle.load(f)

def predire_profit(product_category,unit_sold,unit_price,discount,city,segment,model_choice ):
    try:
        product_encoded=label_encoder.transform([product_category])[0]
        city_encoded=label_encoder.transform([city])[0]
        segment_encoded=label_encoder.transform([segment])[0]
        données= np.array([product_encoded,unit_sold,unit_price,discount,city_encoded,segment_encoded])
        if model_choice=="Linear_Regression":
            modeel=model
    

        #Prediction profit
        prix=model.predict(données)[0]
        return f"profit estimé:${prix}"
    except Exception as e:
        return f"Erreur: {str(e)}"
    
import gradio as gr