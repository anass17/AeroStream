import altair as alt

def pie_chart(df, category, category_title, height = 400):

    df_pie = df.copy()
    df_pie["percentage"] = df_pie["count"] / df_pie["count"].sum() * 100

    chart = (
        alt.Chart(df_pie)
        .mark_arc(innerRadius=50)
        .encode(
            theta=alt.Theta("percentage:Q", stack=True),
            tooltip=[
                f"{category}:N",
                alt.Tooltip("percentage:Q", format=".1f")
            ],
            color=alt.Color(
                f"{category}:N",
                legend=alt.Legend(
                    title=category_title,
                    orient="bottom"
                )
            )
        ).properties(
            height=height
        )
    )

    return chart