import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
	 # Import data
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

    # Filter out data
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
            (df['value'] <= df['value'].quantile(0.975))]



def draw_line_plot():
    df_line = df.copy()

    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)

    # Add titles and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    
    ax.tick_params(axis='x', rotation=45)
    plt.show()

    # Save and return figure
    fig.savefig('line_plot.png')
    return fig
    
    

def draw_bar_plot():
    df_bar = df.copy()    
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.strftime('%B')
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack()
    fig, ax = plt.subplots(figsize=(10, 10))
    df_bar.plot(kind='bar', ax=ax)
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Monthly Average Page Views per Year')
    ax.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ])

    
    plt.tight_layout()
    plt.show()
    fig.savefig('bar_plot.png')
    return fig
    
    
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month'] = pd.Categorical(df_box['month'],categories = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],ordered = True)
    
    fig,ax= plt.subplots(1,2,figsize=(10,10))
    sns.boxplot(x= 'year',y='value',data = df_box,hue = 'year',ax =ax[0],legend = False)
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(x= 'month',y='value',data = df_box,hue ='month',ax =ax[1])
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    plt.tight_layout()
    plt.show()
    
    # Save image and return fig (don't change this part)
    
    fig.savefig('box_plot.png')
    return fig

draw_bar_plot()