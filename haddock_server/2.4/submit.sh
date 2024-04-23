#!/bin/bash

login='<your_login>'
password='<your_password>'
pdb1File="./test_files/Ataxin_3_WT_IT.pdb"
pdb1_active="./test_files/Ataxin_3_WT_IT_active.txt"
pdb1_passive="./test_files/ataxin_3_WT-IT_passive.txt"

pdb2File="./test_files/5315.pdb"
pdb2_active="./test_files/5315_active.txt"
pdb2_passive="./test_files/5315passive.txt"

polling_freq=600 #seconds to wait between results polling


#params_file='/tmp/test-haddock-1/Ref_vs_AF_A1L0T0_F1_model_v2_001_job_params.json'

cookies_file=$(mktemp /tmp/haddock-scrap-cookies.XXXXXX)
# Get the first CSRF on the login form, as well as to get the session cookie ($cookies_file)
csrf=$(curl -c $cookies_file -b $cookies_file 'https://wenmr.science.uu.nl/auth/login?next=/haddock2.4/submit/1' 2>/dev/null | grep csrf | sed -e 's/.*value="\(.*\)".*/\1/g' | head -n 1)
sleep 1

# Post the login form
curl -o /dev/null -c $cookies_file -b $cookies_file -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "csrf_token=$csrf&email=$login&password=$password&submit=Login" 'https://wenmr.science.uu.nl/auth/login?next=/haddock2.4/submit/1' 2> /dev/null
sleep 1

# STEP 1
# Get the second CSRF on the STEP 1
csrf2=$(curl -c $cookies_file -b $cookies_file 'https://wenmr.science.uu.nl/haddock2.4/submit/1'  2>/dev/null | grep csrf | sed -e 's/.*value="\(.*\)".*/\1/g' | head -n 1)
sleep 1
echo $csrf2;

# STEP 2
# Submit the pdbs and get the third CSRF on the STEP 2
random_suffix=$(tr -dc 'a-zA-Z0-9' < /dev/urandom | fold -w 12 | head -n 1)
experiment_name="experiment_$random_suffix"
echo "exp name:  $experiment_name"
# curl 'https://wenmr.science.uu.nl/haddock2.4/submit/2' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: multipart/form-data; boundary=---------------------------45803085429117315043204201780' -H 'Origin: https://wenmr.science.uu.nl' -H 'Connection: keep-alive' -H 'Referer: https://wenmr.science.uu.nl/haddock2.4/submit/2' -H 'Cookie: session=f09c96a7-f17e-4b1a-b16d-bac5a2cc9590; _ga=GA1.2.16244081.1713885225; _gid=GA1.2.295981607.1713885225' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' --data-binary $'-----------------------------45803085429117315043204201780\r\nContent-Disposition: form-data; name="csrf_token"\r\n\r\nIjdlMzVhMTcxMGU2Y2M5ZDE1NTY4ODBkZjFkYzI1MTAyMjI3ZWU2OTci.ZifTNQ.oyASlW1468hsHug3jgf5ApuUBcw\r\n-----------------------------45803085429117315043204201780\r\nContent-Disposition: form-data; name="runname"\r\n\r\nataxin_3_WT_IT_5315_IT\r\n-----------------------------45803085429117315043204201780\r\nContent-Disposition: form-data; name="nb_partners"\r\n\r\n2\r\n-----------------------------45803085429117315043204201780\r\nContent-Disposition: form-data; name="p1_pdb_chain"\r\n\r\nAll\r\n-----------------------------45803085429117315043204201780\r\nContent-Disposition: form-data; name="p1_pdb_file"; filename="Ataxin_3_WT_IT.pdb"\r\nContent-Type: application/x-aportisdoc\r\n\r\n-----------------------------45803085429117315043204201780\r\nContent-Disposition: form-data; name="p1_moleculetype"\r\n\r\nProtein\r\n-----------------------------45803085429117315043204201780\r\nContent-Disposition: form-data; name="p2_pdb_chain"\r\n\r\nAll\r\n-----------------------------45803085429117315043204201780\r\nContent-Disposition: form-data; name="p2_pdb_file"; filename="5315.pdb"\r\nContent-Type: application/x-aportisdoc\r\n\r\n-----------------------------45803085429117315043204201780--\r\n'


echo "PDB1 FILE (head)"
head $pdb1File

echo "PDB2 FILE (head)"
head $pdb2File

csrf3=$(curl -c $cookies_file -b $cookies_file -X POST -F "csrf_token=$csrf2" -F "runname=$experiment_name" -F "nb_partners=2" -F "p1_pdb_chain=All" -F "p1_pdb_file=@$pdb1File" -F "p1_moleculetype=Protein" -F "p2_pdb_chain=All" -F "p2_pdb_file=@$pdb2File" 'https://wenmr.science.uu.nl/haddock2.4/submit/2' 2>/dev/null | grep csrf | sed -e 's/.*value="\(.*\)".*/\1/g' | head -n 1)

sleep 1
echo $csrf3;

# STEP 3
# Submit the active and passive sites and get the fouth CSRF on the STEP 3

# curl 'https://wenmr.science.uu.nl/haddock2.4/submit/3' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: multipart/form-data; boundary=---------------------------405987529311069899511932319798' -H 'Origin: https://wenmr.science.uu.nl' -H 'Connection: keep-alive' -H 'Referer: https://wenmr.science.uu.nl/haddock2.4/submit/2' -H 'Cookie: session=f09c96a7-f17e-4b1a-b16d-bac5a2cc9590; _ga=GA1.2.16244081.1713885225; _gid=GA1.2.295981607.1713885225' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' --data-binary $'-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="csrf_token"\r\n\r\nIjdlMzVhMTcxMGU2Y2M5ZDE1NTY4ODBkZjFkYzI1MTAyMjI3ZWU2OTci.ZifUGg.TkmAT0sNBKtIyL04Gyis_4xDGQY\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="p1_r_activereslist_1"\r\n\r\n1,2,3,10,11,12,13,17,28,30,35,36,41,42,44,54,55,61,99,101,102,103,105,108,134,135,138,142,146,150,151,177,178,179,181,182,183,184,185,186,187,188,212,214,215,246,250,268,270,319,322,326,339,346,350,351,355\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="p1_filter_buried"\r\n\r\ny\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="p1_filter_buried_cutoff"\r\n\r\n15.0\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="p1_r_passivereslist_1"\r\n\r\n4,5,7,8,9,21,25,27,34,38,39,43,45,46,47,48,49,50,51,52,53,56,57,58,59,60,62,63,64,65,68,70,71,72,85,86,87,91,92,97,98,100,104,107,109,110,116,118,125,127,128,129,133,139,140,141,144,145,147,149,153,154,156,157,160,166,170,171,175,176,180,189,190,191,192,196,200,201,205,207,208,209,210,211,213,216,217,218,219,220,222,223,225,226,235,238,240,241,242,243,244,245,247,248,249,260,261,265,266,267,269,271,272,273,314,316,317,318,320,321,323,324,325,329,330,331,332,333,334,337,341,342,344,345,347,349,352,353,354,356,357,358,359,360\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="p2_r_activereslist_1"\r\n\r\n1,24,25,26,27,28,30,31,33,34,35,36,213,298,302,303,304,305,307,308,311,312,329,338,339,341,342,343,346,347,349,350,353,354,392,404,405,406,408,411,414,415,418,422,423,480,483,484,487,508,515,516,518,519,520,521,523,524,525,526,527,528,529\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="p2_filter_buried"\r\n\r\ny\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="p2_filter_buried_cutoff"\r\n\r\n15.0\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="p2_r_passivereslist_1"\r\n\r\n57,59,60,62,63,66,80,81,83,85,86,89,93,96,97,98,99,100,101,102,103,104,106,118,123,125,126,127,128,129,130,131,133,135,136,137,138,141,145,146,148,149,150,151,153,154,155,160,162,163,166,167,169,171,175,178,179,180,184,186,187,188,189,190,191,194,196,199,200,202,206,217,218,219,234,235,236,252,261,320,362,363,366,369,372,376,379,380,383,384,488,491,495,498,499,501,504,506,531\r\n-----------------------------405987529311069899511932319798\r\nContent-Disposition: form-data; name="submit"\r\n\r\nNext\r\n-----------------------------405987529311069899511932319798--\r\n'

echo "PDB1 Active sites"
head $pdb1_active
echo ""
echo "PDB1 Passive sites"
head $pdb1_passive
echo ""

echo "PDB2 Active sites"
head $pdb2_active
echo ""
echo "PDB2 Passive sites"
head $pdb2_passive
echo ""


csrf4=$(curl -c $cookies_file -b $cookies_file -X POST -F "csrf_token=$csrf3" -F "p1_r_activereslist_1=$(cat $pdb1_active)" -F "p1_filter_buried=y" -F "p1_filter_buried_cutoff=15" -F "p1_r_passivereslist_1=$(cat $pdb1_passive)" -F "p2_r_activereslist_1=$(cat $pdb2_active)" -F "p2_filter_buried=y" -F "p2_filter_buried_cutoff=15" -F "p2_r_passivereslist_1=$(cat $pdb2_passive)" 'https://wenmr.science.uu.nl/haddock2.4/submit/3' 2>/dev/null | grep csrf | sed -e 's/.*value="\(.*\)".*/\1/g' | head -n 1)

sleep 1
echo $csrf4;

# STEP 4
# Do final submission without changing parameters and get the polling url

# curl 'https://wenmr.science.uu.nl/haddock2.4/submit/4' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: multipart/form-data; boundary=---------------------------133464655013952221674008532074' -H 'Origin: https://wenmr.science.uu.nl' -H 'Connection: keep-alive' -H 'Referer: https://wenmr.science.uu.nl/haddock2.4/submit/3' -H 'Cookie: session=f09c96a7-f17e-4b1a-b16d-bac5a2cc9590; _ga=GA1.2.16244081.1713885225; _gid=GA1.2.295981607.1713885225' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' --data-binary $'-----------------------------133464655013952221674008532074\r\nContent-Disposition: form-data; name="csrf_token"\r\n\r\nIjdlMzVhMTcxMGU2Y2M5ZDE1NTY4ODBkZjFkYzI1MTAyMjI3ZWU2OTci.ZifYgQ.G1SBBDsIjRjdP14V0R3EU51r7h4\r\n-----------------------------133464655013952221674008532074--\r\n'

poll_url=$(curl -i -c $cookies_file -b $cookies_file -X POST -F "csrf_token=$csrf4" -F "p1_r_activereslist_1=$(cat $pdb1_active)" -F "p1_filter_buried=y" -F "p1_filter_buried_cutoff=15" -F "p1_r_passivereslist_1=$(cat $pdb1_passive)" -F "p2_r_activereslist_1= $(cat $pdb2_active)" -F "p2_filter_buried=y" -F "p2_filter_buried_cutoff=15" -F "p2_r_passivereslist_1=$(cat $pdb2_passive)" 'https://wenmr.science.uu.nl/haddock2.4/submit/4' 2>/dev/null | grep -i Location | sed -e 's/location: //g')



poll_url="https://wenmr.science.uu.nl$(echo $poll_url | tr -d $'\r' | tr -d $'\n')"
sleep 1

echo "Waiting for Sucess status..."
while true; do
    echo "Checking if results are available"
    job_status_page=$(curl "$poll_url" 2>/dev/null)
    status=$(echo $job_status_page | tr '<' '\n' | grep Status | sed -e 's/.*Status: \(.*\) .*/\1/g')

    if [ "$status" == "Success" ]; then
        echo "Job finished! "
        exit 0
    else
        echo "Not yet :-)"
    fi
    sleep $polling_freq
done


