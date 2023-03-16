import lib.dependancies as dependancies
import input as inp

dataset = dependancies.pd.DataFrame(inp.textClassified)
dependancies.pd.set_option('display.max_colwidth', None)