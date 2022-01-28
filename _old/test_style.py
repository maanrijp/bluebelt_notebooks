import bluebelt.styles.styles as styles
import bluebelt.helpers.defaults as defaults

summary = styles.MatplotlibStyle('summary')

# histogram
summary.hist.alpha = 0.3 # alpha fraction 0-1
summary.hist.edgecolor = None # color name, hex or None
summary.hist.facecolor = defaults.dark_blue # color name, hex or None
summary.hist.fill = True #True, False
summary.hist.hatch = None # '/', '\', '|', '-', '+', 'x', 'o', 'O', '.' or '*'
summary.hist.linestyle = 'solid' # '-', '--', '-.', ':', '', (offset, on-off-seq), ...
summary.hist.linewidth = 1 # float


# fill_between
summary.fill_between.alpha=0.3
summary.fill_between.color=None
summary.fill_between.edgecolor=defaults.black
summary.fill_between.facecolor = defaults.blue # color name, hex or None
summary.fill_between.hatch=None
summary.fill_between.linewidth = 0 # edge linewidth

# boxplot
summary.boxplot.boxes = {'color': defaults.blue}

# plot (used for normal distribution)
summary.plot.color = defaults.blue
summary.plot.linestyle = 'dashed'
summary.plot.linewidth = 1


# axvline (used for std field and lines to boxplot, mean and median)
summary.axvline.color = defaults.blue
summary.axvline.linestyle = 'dotted'
summary.axvline.linewidth = 1

# text (used for sigma text)
summary.text.backgroundcolor = defaults.white