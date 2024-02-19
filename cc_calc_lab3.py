
!pip install cartopy

import numpy as np
import matplotlib.pyplot as plt

lats = np.load('lats.npy')
lons = np.load('lons.npy')
data = np.load('data.npy')

proj = ccrs.PlateCarree() #let's set the map's projection

fig, ax = plt.subplots(subplot_kw=dict(projection=proj), figsize=(10, 20))#now we need to create a figure with the pre-set projection and a size

ax.set_extent([-160, -105, 40 ,70], crs=ccrs.PlateCarree())#let's limit the coordinates to have only the region of MODIS product

plt.contourf(lons, lats, data,
             transform=ccrs.PlateCarree(), cmap = 'summer') #let's add a countor of the data using matplotlib
'''Adding nice cartopy features'''
ax.add_feature(cfeature.BORDERS, edgecolor='black', linewidth=1) 
ax.add_feature(cfeature.LAKES,  alpha=0.5)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1)
ax.add_feature(cartopy.feature.RIVERS, edgecolor='blue', linewidth=0.5)
states_provinces = cfeature.NaturalEarthFeature(
            category='cultural',  name='admin_1_states_provinces',
            scale='10m', facecolor='none')
ax.add_feature(states_provinces, edgecolor='black', zorder=10, linestyle = '-', linewidth=0.5)


ax.gridlines(draw_labels=True)#formating the grid

lon, lat = -122.8414, 55.1119 
ax.plot(lon,lat,  'bo', markersize=6, color = 'red', transform=ccrs.Geodetic())#adding some random marker to the map
