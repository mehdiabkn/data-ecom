import pandas as pd
import matplotlib.pyplot as plt
import shopify
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt
import os
import calendar

# Authentification à l'API Shopify
shop_url ='https://dohashop-.myshopify.com'
token='shpat_0b7e402977e901930d08'
api_session= shopify.Session(shop_url, '2023-04', token)
shopify.ShopifyResource.activate_session(api_session)
#orders= getData('Order')


a= shopify.Order.find(limit=250, status='any')
date_format = "%Y-%m-%dT%H:%M:%S%z"
weekdays_orders = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0
}
hours_dict = {str(hour).zfill(2): 0 for hour in range(24)}


for i in a:
    print(date.today())
    date = datetime.strptime(i.created_at, date_format)
    day_of_week = date.strftime("%A")
    weekdays_orders[day_of_week]+=1
    heure_commande = i.created_at[11:13]
    hours_dict[heure_commande] += 1



plt.figure(figsize=(8, 6))
plt.bar(weekdays_orders.keys(), weekdays_orders.values())
plt.xlabel('Jour de la semaine')
plt.ylabel('Fréquence')
plt.title('Distribution des jours de la semaine')
plt.show()

# Création du graphique pour le dictionnaire 2
plt.figure(figsize=(10, 6))
plt.bar(hours_dict.keys(), hours_dict.values())
plt.xlabel('Heure')
plt.ylabel('Fréquence')
plt.title('Distribution des heures de la journée')
plt.show()