import altair as alt

##### Function to create horizental bar chart

def horizental_bar_chart(df, x_col, y_col, x_col_title, y_col_title, height = 400):
        
    bars = (
        alt.Chart(df)
        .mark_bar(size=30)
        .encode(
            y=alt.Y(
                f"{x_col}:N",
                sort="-x",
                title=x_col_title
            ),
            x=alt.X(
                f"{y_col}:Q",
                title=y_col_title
            ),
            tooltip=[f"{x_col}:N", f"{y_col}:Q"]
        )
    )

    text = (
        alt.Chart(df)
        .mark_text(
            align="left",      
            baseline="middle",
            dx=5,              
            color="white"      
        )
        .encode(
            y=alt.Y(f"{x_col}:N", sort="-x"),
            x=alt.X(f"{y_col}:Q"),
            text=alt.Text(f"{y_col}:Q")
        )
    )

    chart = (bars + text).properties(height=height)

    return chart


##### Function to create horizental bar chart with split parts

def split_horizental_bar_chart(df, x_col, middle_col, y_col, x_col_title, middle_col_name, y_col_title, height = 400):

    df_plot = df.pivot(
        index=x_col,
        columns=middle_col,
        values=y_col
    ).reset_index()

    df_melted = df_plot.melt(
        id_vars=x_col,
        var_name=middle_col_name,
        value_name=y_col
    )

    bars = (
        alt.Chart(df_melted)
        .mark_bar(size=30)
        .encode(
            y=alt.Y(f"{x_col}:N", title=x_col_title),
            x=alt.X(f"{y_col}:Q", title=y_col_title),
            color=alt.Color(
                f"{middle_col_name}:N",
                title=middle_col_name,
                legend=alt.Legend(orient="bottom", direction="horizontal")
            ),
            tooltip=[f"{x_col}:N", f"{middle_col_name}:N", f"{y_col}:Q"]
        )
    )

    text = (
        alt.Chart(df_melted)
        .mark_text(
            align="right",
            baseline="middle",
            dx=-5, 
            color="white",
            size=12
        )
        .encode(
            y=alt.Y(f"{x_col}:N", title=x_col_title),
            x=alt.X(f"{y_col}:Q", stack="zero"),
            detail=f"{middle_col_name}:N", 
            text=alt.Text(f"{y_col}:Q")
        )
    )

    chart = (bars + text).properties(height=height)

    return chart
