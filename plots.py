import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
df=pd.read_csv('ToyotaCorolla.csv')
print(df.head())
df=df.drop(['Id','Model'],axis=1,errors='ignore')
df=df.dropna()
print(df.describe())
# Scatter Plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x='Age_08_04',y='Price')
plt.title('Scatter Plot: Age vs Price')
plt.show()
#Box Plot 
plt.figure(figsize=(50,30))
sns.boxplot(data=df)
plt.title('Box Plots of Features')
plt.show()
#Heat Map
plt.figure(figsize=(50,30))
corr=df.corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()
#Contour Plot
X=df['Age_08_04']
Y=df['KM']
Z=np.sin(X)*np.cos(Y)
plt.tricontour(X,Y,Z,levels=190,cmpa='virdis')
plt.colorbar()
plt.title('Contour Plot of sin(x)*cos(y)')
plt.xlabel('Age_08_04')
plt.ylabel('KM')
plt.show()
#3D Surface Plot
fig=plt.figure(figsize=(50,30))
ax=fig.add_subplot(111,projection='3d')
x=np.linspace(df['Age_08_04'].min(),df['Age_08_04'].max(),15)
y=np.linspace(df['Price'].min(),df['Price'].max(),15)
x,y=np.meshgrid(x,y)
z=np.sin(x)*np.cos(y)
ax.plot_surface(x,y,z,cmap='plasma')

ax.set_title('3D Surface Plot')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()