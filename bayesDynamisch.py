import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from sympy import O

plt.rcParams['font.size'] = 13


# The parametrized function to be plotted
def f1(praevalenz, sensitivitaet, spezifitaet):
    return 100 * praevalenz*sensitivitaet / (praevalenz*sensitivitaet + (100-praevalenz)*(100-spezifitaet))

def f2(praevalenz, sensitivitaet, spezifitaet):
    return 100 * praevalenz*(100-sensitivitaet) / (praevalenz*(100-sensitivitaet) + (100-praevalenz)*spezifitaet)

t = np.linspace(0, 100, 1000)

# Define initial parameters
init_sens = 90
init_spez = 97

# Define Labels and Colors
color2='tab:red'
color1='tab:green'
lab1 = '$P_{T}(K)$'
lab2 = '$P_{\overline{T}}(K)$'

# Create the figure and the line that we will manipulate
fig, ax1 = plt.subplots(figsize=(6,7))
ax2=ax1.twinx()
line1,  = ax1.plot(t, f1(t, init_sens, init_spez), lw=2, color=color1)
line2,  = ax2.plot(t, f2(t, init_sens, init_spez), lw=2, color=color2)
leg = fig.legend([line1, line2], labels=[lab1, lab2], bbox_to_anchor=(.25, 0, .5, 0), loc="lower left", mode="expand", ncol=2, frameon=False)

ax1.set_xlabel('Prävalenz [%]')
ax1.set_ylabel(lab1 + ' [%]', color=color1)
ax2.set_ylabel(lab2 + ' [%]', color=color2)

ax1.set_xlim(0,100)
ax1.set_ylim(0,100)
ax2.set_ylim(0,100)

lines = [line1, line2]
lined = {}  # Will map legend lines to original lines.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Enable picking on the legend line.
    lined[legline] = origline

# adjust the main plot to make room for the sliders
plt.subplots_adjust(bottom=0.35, top=0.95, right=.85, left=.15)

# Make a horizontal slider to control the frequency.
axsens = plt.axes([0.25, 0.1, 0.65, 0.03])
sens_slider = Slider(
    ax=axsens,
    label='Sensitivität [%]',
    valmin=0,
    valmax=100,
    valinit=init_sens,
)

# Make a vertically oriented slider to control the amplitude
axspec = plt.axes([0.25, 0.18, 0.65, 0.03])
spec_slider = Slider(
    ax=axspec,
    label="Spezifität [%]",
    valmin=0,
    valmax=100,
    valinit=init_spez
)


# The function to be called anytime a slider's value changes
def update(val):
    line1.set_ydata(f1(t, sens_slider.val, spec_slider.val))
    line2.set_ydata(f2(t, sens_slider.val, spec_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
sens_slider.on_changed(update)
spec_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    sens_slider.reset()
    spec_slider.reset()
button.on_clicked(reset)

def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    ax = origline.axes
    lab = ax.get_ylabel()
    ax.set_ylabel(lab, alpha=visible)
    fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()