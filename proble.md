# problem statement
1.  **First Problem Statement**

"PDF parser for FIR Copy"

-   We have crores of fir copies in pdf format for all over the states in India.
-   for that we need a pdf parser to get data from FIR Copy.

sample input: [sample pdf](https://fg7syt3j.r.ap-south-1.awstrack.me/L0/https:%2F%2Ffirhtml.s3-us-west-2.amazonaws.com%2Fd5ffa24cc24c635c2105d05f31f03ecd/1/01090181b996d067-8220608f-f98c-478f-95dc-bd9638894a7e-000000/FaETZCTHSPd-wHDh6HO2Dsr8fRc=57)

desired output in JSON format:

{

"dist_name":"Valsad",

"police_station":"vapi tauna",

"fir_date":"31/03/2019",

"fir_no":"111/2019",

"state":"Gujarat",

"accused_name_1":"dhannamjaya ramezabhai rathoda g-1, yusupha epartamenta,",

"accused_name_1_org":" ધન્નંજય રમેશભાઈ રાઠોડ G-1, યુસુફ એપાર્ટમેન્ટ,",

"act":"ema mi e",

"act_org":" એમ મી એ ",

"address_org":"",

"age_1_org":"",

"complaint_informan_date_year_of_birth":"",

"complaint_informan_date_year_of_birth_org":" ",

"complaint_informan_father_husband_name":"khabusimha lrpc",

"complaint_informan_father_husband_name_org":" ખાબુસીંહ LRPC",

"complaint_informan_name":"ajaya babursiha lrpc",

"complaint_informan_name_org":" અજય બાબુર્સીહ LRPC ",

"complaint_informan_nationality":"bharatiya",

"complaint_informan_nationality_org":" ભારતીય",

"date":" 31/03/2019",

"details_address_1":"jalarama ,gama. vapitauna, ta. vapi, ji. valasada.",

"details_address_1_org":"જલારામ ,ગામ. વાપીટાઉન, તા. Vapi, જી. વલસાડ. ",

"dist_name_pdf":"valasada",

"dist_name_pdf_org":" વલસાડ ",

"fir_no_org":" |I/111/2019 ",

"occupation":"nokari",

"occupation_org":"નોકરી\n",

"occurrence_of_offence_date_from":" 31/03/2019 ",

"occurrence_of_offence_date_to":" 31/03/2019",

"occurrence_of_offence_time_from":" 03:00 ",

"occurrence_of_offence_time_period":" ",

"occurrence_of_offence_time_to":" 03:00",

"place_of_occurrence_district_org":"",

"place_of_occurrence_name_of_police_station":"",

"place_of_occurrence_name_of_police_station_org":" ",

"police_station_org":" વાપી ટાઉન ",

"sections":"185",

"sections_org":" 185",

"year":" 2019 ",

}

2.  **Second Problem Statement**

"Transliteration"

-   The content of the FIR copy is in the regional language according to the state.
-   We need a transliteration to translate regional language content to English.

Example: -

input:- मख्खन लाल

output:- Makkhan Lal