from cleaning.irrelevant import delete_last_two_columns
from cleaning.outliers import outliersfunction
from cleaning.mistaken import mistakendata
from cleaning.nulos import eliminar_nulos
from cleaning.repeated import repeated_values
from cleaning.duplicates import deal_with_duplicates


def cleaning(df_to_clean, ir, out, md, vn, rep, dup):
    if False == (ir or out or md or vn or rep or dup):
        print("\n\n\nYou didn't select any cleaning method.\n\n\n")
    if ir:
        df_to_clean = delete_last_two_columns(df_to_clean)
    if out:
        df_to_clean = outliersfunction(df_to_clean)
    if md:
        df_to_clean = mistakendata(df_to_clean)
    if vn:
        df_to_clean = eliminar_nulos(df_to_clean)
    if rep:
        df_to_clean = repeated_values(df_to_clean)
    if dup:
        df_to_clean = deal_with_duplicates(df_to_clean)
    if False == (ir and out and md and vn and rep and dup):
        print("\n\n\nRemember that there are still things to clean!\n\n\n")

    df = df_to_clean.copy()

    return df
