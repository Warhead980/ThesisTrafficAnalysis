
import seaborn as sns
import matplotlib.pyplot as plt

def CorelationMatrix(df):
    #df = df.iloc[:, [0, 1, 2, 3, 5, 6, 8, 9, 12, 18, 1060, 1079, 1080, 1081]]
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