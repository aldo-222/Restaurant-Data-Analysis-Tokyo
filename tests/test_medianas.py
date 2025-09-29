import pandas as pd
from src.mediana import separate_mediana

def test_separate_mediana():
    df_mediana = pd.DataFrame({
        "ItemName":["あ単品","え単品","い単品","お単品","う単品"],
        "SalesQty":[70,90,30,10,50],
        "SalesAmount":[1500, 800, 3000, 200,1000],    
        })
    
    resultados, med_qty, med_amt = separate_mediana(df_mediana.copy())
    #comprobando que tenemos columnas
    assert "ProductType" in resultados.columns
    assert resultados["ProductType"].notna().all()
    #que existen las 4 categorías
    tipos = set(resultados["ProductType"].unique())
    esperados = {
        "StarProduct - 最高の単品",
        "LowProfit - 低い利益",
        "HiddenPremium - 隠れ優良単品",
        "Atriskofremoval - リスク候補の単品", }
    assert esperados.issubset(tipos)
    
    # Medianas
    qty_min, qty_max = resultados["SalesQty"].min(), resultados["SalesQty"].max()
    qty_unique = resultados["SalesQty"].nunique()
    if qty_unique > 1:
        assert qty_min < med_qty < qty_max
    else:
        assert qty_min == med_qty == qty_max 
    # SalesAmount
    amt_min, amt_max = resultados["SalesAmount"].min(), resultados["SalesAmount"].max()
    amt_unique = resultados["SalesAmount"].nunique()
    if amt_unique > 1:
        assert amt_min < med_amt < amt_max
    else:
        assert amt_min == med_amt == amt_max
