def dosomething(session: Session) -> None:
    df = session.table("github_connect.github.target")
    df = df.group_by(f.col('id')).agg(sum_(f.col('num')).alias('SUM'))
    df.write.mode("overwrite").save_as_table("agg_target")
    return df
