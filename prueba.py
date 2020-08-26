import pandas as pd

dataframe = pd.read_csv('winequality-red.csv',sep=';')
dataframe.head()

Media_Alcohol = dataframe.alcohol.median()
Media_pH = dataframe.pH.median()
Media_citric_acid = dataframe.citric_acid.median()
Media_residual_sugar = dataframe.residual_sugar.median()

#Determina media alta y media baja
def funcion(x,y,z):
    for i, x in enumerate(x):
        if x >= z:
            dataframe.loc[i,y] = 'Media Alta'
        else:
            dataframe.loc[i,y] = 'Media Baja'
    print(dataframe.groupby(y).quality.mean())

#(dataframe.columna, 'nombre bajo el que se muestra', Media_columna)
funcion(dataframe.alcohol, 'alcohol', Media_Alcohol)
funcion(dataframe.pH, 'pH', Media_pH)
funcion(dataframe.citric_acid, 'citric_acid', Media_citric_acid)
funcion(dataframe.residual_sugar, 'residual_sugar', Media_residual_sugar)
