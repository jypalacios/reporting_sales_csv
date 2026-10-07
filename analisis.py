import pandas as pd
import matplotlib.pyplot as plt


# 1. Cargar datos del CSV
datos = pd.read_csv('dataset_ventas.csv')
print(datos.head())
#parsear fechas
datos['Order Date'] = pd.to_datetime(datos['Order Date'])
#validar datos numericos
datos['Sales Channel'] = pd.to_numeric(datos['Sales Channel'], errors='coerce')

# 2. Calcular ventas totales por mes
datos['Order Date'] = datos['Order Date'].dt.to_period('M')
ventas_por_mes = datos.groupby('Order Date').apply(lambda d: (d['Units Sold'] * d['Unit Price']).sum())
ventas_por_mes = ventas_por_mes.sort_index()
print("Ventas por mes:")
print(ventas_por_mes)

# 3. Determinar producto más vendido y con mayor ingresos
datos['ingreso'] = datos['Units Sold'] * datos['Unit Price']
ventas_prod = datos.groupby('Item Type').agg({'Units Sold': 'sum','ingreso': 'sum'})
mas_vendido = ventas_prod['Units Sold'].idxmax()
mayor_ingreso = ventas_prod['ingreso'].idxmax()
print(f"Producto más vendido en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'Units Sold']})")
print(f"Producto con mayores ingresos: {mayor_ingreso} (total {ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f} €)")


# 4. Graficar ventas por mes
plt.plot(ventas_por_mes.index, ventas_por_mes.values)
plt.show()

# 5. Graficar top 5 productos por ingresos
top5 = ventas_prod.nlargest(5, 'ingreso')
plt.figure(figsize=(6,4))
plt.bar(top5.index, top5['ingreso'])
plt.title("Top 5 Productos por Ingresos")
plt.ylabel("Ingresos (€)")
plt.xlabel("Producto")
plt.tight_layout()
plt.savefig("top5_productos.png")
plt.show()
