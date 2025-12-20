import altair as alt

def line_chart(df, col, col_title, height = 400):
        
    df_counts = df.groupby(col).size().reset_index(name="count")

    chart = (
        alt.Chart(df_counts)
        .mark_line(point=True)
        .encode(
            x=alt.X(f"{col}:T", title={col_title}),
            y=alt.Y("count:Q", title="Number of tweets"),
            tooltip=[f"{col}:T", "count:Q"]
        )
        .properties(height=height)
    )

    return chart