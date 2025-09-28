#What if n(50) customers change their individual orders for ordering courses?
#もし50人のお客様が単品を注文する代わりにコースを注文するとしたら、どうなる？

def simulated_info (df_course, dinnerticket_average, new_coursecustomers = 50):
#Creating the table // 対比の表を作成する
  df_impacto = df_course[["ItemName", "UnitPrice"]].copy()
  df_impacto["Dinner Average Ticket"] = dinnerticket_average
  df_impacto["Potencial Extra Revenue"] = df_impacto["UnitPrice"] - dinnerticket_average
  df_impacto["New Costumers"] = new_coursecustomers
  df_impacto["Estimated Adittional Revenue"] = df_impacto["Potencial Extra Revenue"] * new_coursecustomers
#Rounding numbers #四捨五入する
  redondear = ["UnitPrice", "Potencial Extra Revenue", "Estimated Adittional Revenue", "Dinner Average Ticket"]
  df_impacto[redondear] = df_impacto[redondear].astype(int)

  return df_impacto