import pandas as pd 
df = pd.read_excel(r"E:\descargas google\articulos_exportados.xlsx")

nuevo_df = df.filter(items=['id','codigo_barra', 'nombre', 'marca', 'precio', 'cantidad_xxs', 'cantidad_xs', 'cantidad_s', 'cantidad_m', 'cantidad_l', 'cantidad_xl', 'cantidad_xxl'])

print(nuevo_df)


cambio_nombre_columnas = nuevo_df.rename(columns={
    'codigo_barra': 'CODIGO',
    'marca': 'MARCA',
    'nombre': 'NOMBRE',
    'precio': 'PRECIO_VENTA',
    'cantidad_xxs': 'STOCK_XXS',
    'cantidad_xs': 'STOCK_XS',
    'cantidad_s': 'STOCK_S',
    'cantidad_m': 'STOCK_M',
    'cantidad_l': 'STOCK_L',
    'cantidad_xl': 'STOCK_XL',
    'cantidad_xxl': 'STOCK_XXL'
})
print(cambio_nombre_columnas)
cambio_nombre_columnas.to_excel(r"E:\descargas google\articulos_exportados_limpio.xlsx", index=False)