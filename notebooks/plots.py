import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.ticker import MaxNLocator, MultipleLocator
import numpy as np

def plot_vel(xmesh, ymesh, data, ax=None, contours=False, **kwargs):
    
    surf = ax.pcolormesh(xmesh, ymesh, data, cmap='RdBu_r', **kwargs)
    #cb = figV.colorbar(surf, ax=axV, extend='both', pad=0.03, format='%.2f', fraction=0.046)
    #cb.set_label(label=r'${\rm v_{0} \quad (m\,s^{-1})}$', rotation=270, labelpad=15)
    #cb.minorticks_on()

    # Plot the contour
    if contours == True:
        #ax.contour(xmesh, ymesh, data, 10, colors='k', linewidths=0.5)
        ax.contour(xmesh, ymesh, data, np.arange(-6000, 6000, 800), colors='b', linewidths=1.0)

    #axV.set_title(f'PA = {PA}, inc = {inc}, twist = {twist}, tilt = {tilt}')

    #axV.set_xlim(xlim)
    #axV.set_ylim(ylim)
    ax.set_xlabel('Offset (arcsec)')
    ax.set_ylabel('Offsec (arcsec)')

    ax.grid(ls='--', color='k', alpha=0.2, lw=0.5)
    ax.xaxis.set_major_locator(MaxNLocator(5, min_n_ticks=3))
    ax.yaxis.set_major_locator(MaxNLocator(5, min_n_ticks=3))
    ticks = np.diff(ax.xaxis.get_majorticklocs()).mean() / 5.0
    ax.xaxis.set_minor_locator(MultipleLocator(ticks))
    ax.yaxis.set_minor_locator(MultipleLocator(ticks))
    ax.set_aspect(1)
    return surf