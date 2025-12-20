import altair as alt

def line_chart(df, x_col, x_col_title, y_col, y_col_title, height = 400):
        
    chart = (
        alt.Chart(df)
        .mark_line(point=True)
        .encode(
            x=alt.X(f"{x_col}:T", title=x_col_title),
            y=alt.Y(f"{y_col}:Q", title=y_col_title),
            tooltip=[f"{x_col}:T", f"{y_col}:Q"]
        )
        .properties(height=height)
    )

    return chart