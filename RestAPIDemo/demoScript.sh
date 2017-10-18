#!/bin/bash
# This simple script shows how you can use the API to create a CAS session, and score observations

echo "Creating a CAS Session ..."
sessionid=$(sh ./createCASSession.sh | jq -r '.session')
echo $sessionid

sleep 2
echo "Scoring the data ..."
python scoreObs.py $sessionid
 
echo "Do you want to close the CAS Session? (y/n)"
read close_ind
if [ "$close_ind" = y ]; then
       sh ./closeCASSession.sh $sessionid
else
      echo "Remember to close the session when you are done! Bye Bye!"
fi

