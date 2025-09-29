import pandas as pd
from src.pareto import preparar_pareto

def test_preparar_pareto():
    df_pareto = pd.DataFrame({
        "ItemName":["A料理","B料理","C料理","D料理","E料理","F料理","G料理"],
        "SalesQty":[5,200,90,30,38,11,50],
        "SalesAmount":[3000,200700,128900,60800,50400,20100,40200],    
        }).sort_values("SalesAmount", ascending=False)
    
    resultados = preparar_pareto(df_pareto.copy())
    #Columnas
    for col in ["Share", "CumulativeShare", "ParetoClass"]:
        assert col in resultados.columns
    #Share suma 1
    assert abs(resultados["Share"].sum() - 1.0) < 1e-6
    #ParetoClass contains 80% y/o 20%
    assert set(resultados["ParetoClass"].unique()).issubset({"80%", "20%"})
    #CumulativeShare siempre crece
    assert resultados["CumulativeShare"].is_monotonic_increasing
