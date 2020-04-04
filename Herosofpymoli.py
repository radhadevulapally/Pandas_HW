#import Dependencies
import pandas as pd
#Read CSV
mydf=pd.read_csv("data.csv")

#RESULT of player count
total=len(mydf['SN'].value_counts())
totalplayers=pd.DataFrame({"Total Players":[total]})
totalplayers

uniqueitems=len(mydf["Item ID"].unique())
uniqueitems
avg=mydf["Price"].mean()
avg
totalpurchases=len(mydf["Purchase ID"])
totalpurchases
totalrevenue=mydf["Price"].sum()

gender_df=mydf.groupby(["Gender"])
print(gender_df)
gender_df.count()
total_gender=gender_df["SN"].nunique()
total_players=total_gender.sum()
total_players
percentage=round(total_gender/total_players*100,2)
percentage
gender_demo=pd.DataFrame({"Total Count": total_gender,"Percentage of Players": percentage})

purchase_count=gender_df["Purchase ID"].count()
purchase_count
avg_purchase_price=round(gender_df["Price"].mean(),2)
avg_purchase_price
total_purchase=gender_df["Price"].sum()
total_purchase
avg_total_person=round(total_purchase/total_gender,2)
avg_total_person
Purchasing_Analysis=pd.DataFrame({"Purchase Count" : purchase_count,"Average Purchase Price" : avg_purchase_price,"Total Purchase Value": total_purchase,"Avg Total Purchase per Person":avg_total_person})
Purchasing_Analysis
Cleaned_df=Purchasing_Analysis.style.format({"Average Purchase Price":"${:,.2f}","Total Purchase Value":"${:,.2f}","Avg Total Purchase per Person":"${:,.2f}"})
Cleaned_df 

#RESULT
age_bins = [0, 9.11, 14.11, 19.11, 24.11, 29.11, 34.11, 39.11, 100]
age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
mydf["AG"] = pd.cut(mydf["Age"],bins=age_bins, labels=age_labels,include_lowest=True )
mydf
age_group_df = mydf.groupby("AG")
totalcountbyage = age_group_df["SN"].nunique()
per=round((totalcountbyage/total)*100,2)
age_demo_df=pd.DataFrame({"Total Count":totalcountbyage,"Percentage of players":per})
age_demo_df.index.name=None
print(age_demo_df)

purchase_count_byage=age_group_df["Purchase ID"].count()
purchase_count_byage
Avg_purchase_price=round(age_group_df["Price"].mean(),2)
Avg_purchase_price
total_purchase_value=age_group_df["Price"].sum()
total_purchase_value
avg_totalpurchaseper_person=round(total_purchase_value/totalcountbyage,2)
avg_totalpurchaseper_person
purchase_analysis_df=pd.DataFrame({"Purchase Count":purchase_count_byage,"Average Purchase Price":Avg_purchase_price,"Total Purchase Value":total_purchase_value,"Average Total Purchase per person":avg_totalpurchaseper_person})
purchase_analysis_df["Total Purchase Value"]=purchase_analysis_df["Total Purchase Value"].map("${:,.2f}".format)
purchase_analysis_df["Average Purchase Price"]=purchase_analysis_df["Average Purchase Price"].map("${:.2f}".format)
purchase_analysis_df["Average Total Purchase per person"]=purchase_analysis_df["Average Total Purchase per person"].map("${:.2f}".format)
purchase_analysis_df

topspenders=mydf.groupby("SN")
topspenders.count()
purchase_count=topspenders["Purchase ID"].count()
purchase_count
avg_purchase_price=round(topspenders["Price"].mean(),2)
avg_purchase_price
total_purchase=round(topspenders["Price"].sum(),2)
total_purchase
topspenders_df=pd.DataFrame({"Purchase Count":purchase_count,"Average Purchase Price":avg_purchase_price,"Total Purchase Value":total_purchase})
topspenders_df
formated_df=topspenders_df.sort_values(["Total Purchase Value"],ascending=False)
formated_df["Average Purchase Price"]=formated_df["Average Purchase Price"].map("${:.2f}".format)
formated_df["Total Purchase Value"]=formated_df["Total Purchase Value"].map("${:.2f}".format)
formated_df.head()

item_df=mydf[["Item ID", "Item Name", "Price"]]
item_df
item_id_grp=item_df.groupby(["Item ID","Item Name"])
item_id_grp.count()
purchase_count=item_id_grp["Price"].count()
purchase_sum=item_id_grp["Price"].sum()
item_price=purchase_sum/purchase_count
most_pop_items=pd.DataFrame({"Purchase Count":purchase_count,"Item Price":item_price,"Total Purchase Value":purchase_sum})
most_pop_items
sorted_df=most_pop_items.sort_values("Purchase Count",ascending=False)
sorted_df["Item Price"]=sorted_df["Item Price"].map("${:.2f}".format)
sorted_df["Total Purchase Value"]=sorted_df["Total Purchase Value"].map("${:.2f}".format)
sorted_df.head()

#RESULT
sorted_again_df=sorted_df.sort_values("Total Purchase Value",ascending=False)
sorted_again_df["Item Price"]=sorted_again_df["Item Price"].map("${:.2f}".format)
sorted_again_df["Total Purchase Value"]=sorted_again_df["Total Purchase Value"].map("${:.2f}".format)
sorted_again_df.head()
