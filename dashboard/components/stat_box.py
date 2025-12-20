
def html_stat_box(title, count):

    return f"""
        <div style="border:2px solid dodgerblue;border-radius:10px;padding:20px 25px">
            <h4 style='color:white;margin:0;margin-bottom:5px;font-weight:400'>
                {title}
            </h4>
            <h2 style="margin:0;font-size:30px">{count}</h2>
        </div>
    """