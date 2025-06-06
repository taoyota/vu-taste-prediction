df = descriptor_df.applymap(lambda x: np.nan if isinstance(x, Missing) else x)

missing_tpsa_indices = descriptor_df[descriptor_df["TPSA"].apply(lambda x: isinstance(x, Missing))].index
problem_smiles = [taste_df["canonical SMILES"][i] for i in missing_tpsa_indices[:5]]  # First 5 examples
print("Example problematic SMILES:", problem_smiles)

mol = Chem.MolFromSmiles("Oc1cc2c(cc1O)C1c3ccc(c(c3OCC1(O)C2)O)O")
d = calc(mol)