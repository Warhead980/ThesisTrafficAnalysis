
import seaborn as sns
import matplotlib.pyplot as plt

def CorelationMatrix(df):

    corr = df.corr(method='kendall')
    ax = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        annot=True,
        square=True)

    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right')

    print(corr)
    plt.show()