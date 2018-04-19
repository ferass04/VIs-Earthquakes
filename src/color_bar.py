from plotly.graph_objs import *
from earthquake_visualization import *


def get_colorscale():
    scale = 1
    data = Data([
        Scatter(
            x=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            y=[1, 2, 3, 4, 5, 6, 7, 8, 9],

            marker=Marker(
                size=[circle_size[0] * scale, circle_size[1] * scale, circle_size[2] * scale, circle_size[3] * scale,
                      circle_size[4] * scale, circle_size[5] * scale, circle_size[6] * scale, circle_size[7] * scale,
                      circle_size[8] * scale],
                cmax=9,
                cmin=1,
                color=[colors_RGB[0], colors_RGB[1], colors_RGB[2], colors_RGB[3], colors_RGB[4], colors_RGB[5],
                       colors_RGB[6], colors_RGB[7], colors_RGB[8]],
                colorbar=ColorBar(
                    title='Colorbar',
                ),
                colorscale=[[0, colors_RGB[0]], [(1/8) * 1, colors_RGB[1]], [(1/8) * 2, colors_RGB[2]],
                            [(1 / 8) * 3, colors_RGB[3]], [(1 / 8) * 4, colors_RGB[4]], [(1 / 8) * 5, colors_RGB[5]],
                            [(1 / 8) * 6, colors_RGB[6]], [(1 / 8) * 7, colors_RGB[7]], [(1 / 8) * 8, colors_RGB[8]]],
            ),
            mode='markers',
            text=['Magnitude 1', 'Magnitude 2', 'Magnitude 3', 'Magnitude 4', 'Magnitude 5', 'Magnitude 6',
                  'Magnitude 7', 'Magnitude 8', 'Magnitude 9']
        )
    ])

    layout = Layout(
        title='Color Bar and Circle Scale by Magnitude',
        paper_bgcolor='rgba(0,0,0,1)',
        plot_bgcolor='rgba(0,0,0,1)'
    )

    fig = Figure(data=data, layout=layout)
    plot(fig, filename='../html/color_scale.html')

