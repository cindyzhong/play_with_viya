import swat
import sys
import pandas as pd

# Connect to an existing CAS Session passed as argument
mysession = sys.argv[1] 
cashost='localhost'
casport=5570
casauth='~/.authinfo'

s = swat.CAS(cashost, casport, authinfo=casauth,session=mysession)
s.loadactionset('decisionTree')
# load my observation to CAS
tbl = pd.read_csv('./newObsToScore.csv')
score_tbl = s.upload_frame(tbl, casout=dict(name='score', replace=True))
# score my observation
s.decisionTree.dtreeScore(table = {'name' : 'score'},modeltable = {'name':'DT_MODEL'},casOut = {'name' : 'scored_obs'})
# save score observation to local
out = s.CASTable("scored_obs").to_frame()
out.to_csv('./newObsScored.csv')

