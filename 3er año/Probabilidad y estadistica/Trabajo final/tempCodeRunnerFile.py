result = st.pearsonr(dataframe.altura, dataframe.peso) # Averiguar que hace
print("Pearson's: " + 'No se rechaza H0' if result[1] > alpha else 'Se rechaza H0') # type: ignore