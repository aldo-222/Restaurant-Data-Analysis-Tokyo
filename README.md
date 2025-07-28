# Discoveries in a restaurant in Tokyo: What the consumption data reveals 
## Summary
### Hallazgos
## Individual Products - 単品
### Tacos: The commercial axis in the restaurant
![Scatter plot - overview](images/overview.png)
Tacos are the top-selling individual product, both at lunch and dinner, in terms of units sold and total revenue. Quesadillas and burritos follow in third and fourth place, respectively. This data will be visualized in the next graph to identify relationhips.
### 33% of the products account for 80% sales
![](images/pareto.png)
If we rank products by sales performance (from highest to lowest), we will find that the top 33% account for 80% of sales.
A clear strategy is to push the sales of the top 5, so we can bias to get the 20% - 80% relation.
What about the rest of the products? Let's take a look:
### 76 Products at risk of removal (red dots)
Sales Amount vs Units Sold Matrix(log)
![](images/log.png)
The matrix shows 4 classifications (please open the preview in desktop for more details: [code](https://github.com/aldo-222/Restaurant-Data-Analysis-Tokyo/blob/main/notebooks/final_integrated_version.ipynb)) the red ones represent products that we could remove to make the menu lighter.
## Nomihoudai - 飲み放題 
### An Index that shows the customer's perception under noumihoudai options
![](images/index.png)
Finding relations between individual drinks and nomihoudai options: Under nomihoudai options (unlimited drinks in two hours), the perceived value of Sparkling Wine, Red Wine and Lemon Sour raises significantly. Corona and HighBall show more balanced consumption across menus, while Cola or Orange Juice are more frequently chosen in individual drinks.
This points to emphasizing the first two in the nomihoudai menus.
However, if we want to see each group by itself, we can break as: 
### Beer as the top drink in every option (individual, nomihoudai and premium)
[Top Nomihoudai](https://github.com/aldo-222/Restaurant-Data-Analysis-Tokyo/blob/main/images/heat_nomihoudai.png) / [Top Premium Nomihoudai](https://github.com/aldo-222/Restaurant-Data-Analysis-Tokyo/blob/main/images/heat_premium.png) / [Top Individual Drinks](https://github.com/aldo-222/Restaurant-Data-Analysis-Tokyo/blob/main/images/heat_individual.png)
In each of them, beer is on the top (Corona and Asahi). 
This leads to expanding beer options: adding more variety (IPA, craft beer, Bohemia) to the nomihoudai menu and using premium beer as a differentior in premium nomihoudai.
## Course - コース
Para ver el código completo, revisar la versión final en el preview 
