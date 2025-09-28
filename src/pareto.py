def preparar_pareto(product_summary):
  #There must be a previous order about the classification (name) and sales amount numbers (from the largest to the smallest)
  #Pareto:Marking the products that account for 80% of sales / 売上の８０％を占める単品
  product_summary["Share"] = product_summary["SalesAmount"] / product_summary["SalesAmount"].sum()
  product_summary["CumulativeShare"] = product_summary["Share"].cumsum()
  product_summary["ParetoClass"] = product_summary["CumulativeShare"].apply(lambda x: "80%" if x <= 0.8 else "20%")    
  return product_summary     