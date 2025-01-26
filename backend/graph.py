import plotly.express as px
import plotly.graph_objects as go
from present import extractDataFromPropertyTable, convertToDataFrame

def drawGraph1(propertyInfo):

    x_values = propertyInfo['square metres'].tolist()
    y_values = propertyInfo['full price'].tolist()
    urls = propertyInfo['link'].tolist()

    # Create hover text with clickable links
    hover_text = [f'<a href="{url}" target="_blank">.</a>' for url in urls]

    # Create a scatter plot
    fig = go.Figure(
        data=go.Scatter(
            x=x_values,
            y=y_values,
            mode="markers",
            text=hover_text,
            hovertemplate="%{text}<extra></extra>",  # Display the clickable link in hover
        )
    )

    # Update the layout
    fig.update_layout(
        title="Scatter Plot with Clickable Dots",
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
    )

    # Show the plot
    fig.show()


def run(id_search,minPrice,maxPrice,minSquareMetres,maxSquareMetres,minSquarePrice,maxSquarePrice):
    df = convertToDataFrame(id_search)
    df = df.loc[
        (df['full price'] > minPrice) & (df['full price'] < maxPrice) &
        (df['square price'] > minSquarePrice) & (df['square price'] < maxSquarePrice) &
        (df['square metres'] > minSquareMetres) & (df['square metres'] < maxSquareMetres)
    ]
    drawGraph1(df)

#run(68,50,1000000,10,500,50,10000)
import sys
if __name__ == "__main__":
    run(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]) )
