def funcPandas(func):
    for col in func.columns:
        print(f'[{col}]==============')
        print(func[col].nuique(), func[col].unique(), sep='\n', end='\n\n')