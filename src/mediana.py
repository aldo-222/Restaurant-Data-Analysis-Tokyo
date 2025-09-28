
#Classifying products based on their medians (not affected by outliers) (SalesQty and SalesAmount)
#売上金額と販売数の中央値で単品を分類する
def separate_mediana(product_summary):
    
    med_salesqty = product_summary["SalesQty"].median()
    med_salesamount = product_summary["SalesAmount"].median()
    def clasificar_producto(valor):
     if valor["SalesQty"] >= med_salesqty and valor["SalesAmount"] >= med_salesamount:
        return "StarProduct - 最高の単品"
     elif valor["SalesQty"] >= med_salesqty and valor["SalesAmount"] < med_salesamount:
        return "LowProfit - 低い利益"
     elif valor["SalesQty"] < med_salesqty and valor["SalesAmount"] >= med_salesamount:
        return "HiddenPremium - 隠れ優良単品"
     else:
        return "Atriskofremoval - リスク候補の単品"
    product_summary["ProductType"] = product_summary.apply(clasificar_producto, axis=1)

    return product_summary, med_salesqty, med_salesamount
