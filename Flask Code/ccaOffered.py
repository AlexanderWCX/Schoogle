#commented

#make api call to get json data; https://data.gov.sg/api/action/datastore_search?resource_id=dd7a056a-49fa-4854-bd9a-c4e1a88f1181&limit=1455&q=SECONDARY

#import libraries
import json
import xlwt

#format json data
x = """[{
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 936
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 937
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SEPAK TAKRAW",
		"_id": 938
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 939
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 940
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 941
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 942
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 943
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 944
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 945
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BAND-CONCERT",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 946
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENSEMBLE-GUZHENG",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 947
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE-MODERN",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 948
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MERIT (MEDIA RESOURCE & IT) CLUB",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 949
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ENTREPRENEUR CLUB",
		"_id": 950
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SERVICE LEARNING CLUB",
		"_id": 951
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 952
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CANOEING/ROWING/DRAGON BOAT",
		"_id": 953
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CROSS COUNTRY",
		"_id": 954
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "HOCKEY",
		"_id": 955
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 956
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 957
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TRACK & FIELD",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 958
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 959
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "SINGAPORE RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 960
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 961
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - ANGKLUNG/KULINTANG",
		"_id": 962
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 963
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 964
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE AND MODERN DANCE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 965
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 966
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "CHESS CLUB",
		"_id": 967
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "COMPUTER CLUB",
		"_id": 968
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LDDS - ENGLISH",
		"_id": 969
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DIGITAL ART & PHOTOGRAPHY CLUB",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 970
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CRESCENT GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INNOVATION AND ENTERPRISE CLUB",
		"cca_generic_name": "ENTREPRENEUR CLUB",
		"_id": 971
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (BOYS ONLY)",
		"cca_generic_name": "BASKETBALL",
		"_id": 972
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "CANOE SPRINT TEAM",
		"cca_generic_name": "CANOEING/ROWING/DRAGON BOAT",
		"_id": 973
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CROSS COUNTRY",
		"_id": 974
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL (BOYS ONLY)",
		"cca_generic_name": "FOOTBALL",
		"_id": 975
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TABLE TENNIS (GIRLS ONLY)",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 976
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 977
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 978
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NPCC (BOYS ONLY)",
		"cca_generic_name": "NPCC",
		"_id": 979
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 980
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "DRAGON SCOUTS",
		"cca_generic_name": "SCOUTS",
		"_id": 981
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (LAND) (BOYS ONLY)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 982
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 983
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 984
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE ENSEMBLE",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 985
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 986
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ENTREPRENEUR CLUB",
		"_id": 987
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GAN ENG SENG SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 988
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 989
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (BOYS)",
		"cca_generic_name": "BASKETBALL",
		"_id": 990
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "DRAGON BOAT",
		"cca_generic_name": "CANOEING/ROWING/DRAGON BOAT",
		"_id": 991
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CROSS COUNTRY",
		"_id": 992
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 993
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOCCER (BOYS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 994
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 995
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 996
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 997
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 998
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 999
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1000
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 1001
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1002
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INDIAN",
		"_id": 1003
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1004
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1005
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "URBAN NATURE",
		"cca_generic_name": "MUSICIANS' CLUB",
		"_id": 1006
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1007
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "NEW MEDIA",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1008
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ECO CLUB",
		"cca_generic_name": "COMMUNITY SERVICE CLUB",
		"_id": 1009
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "BITS AND ATOMS",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1010
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CULINARY CLUB",
		"cca_generic_name": "HOME ECONOMICS",
		"_id": 1011
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1012
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1013
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1014
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "GOLF",
		"_id": 1015
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRAMPOLINE",
		"_id": 1016
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1017
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1018
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1019
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1020
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1021
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1022
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1023
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1024
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1025
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 1026
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AVA & BROADCASTING CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1027
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1028
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1029
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TCHOUKBALL",
		"_id": 1030
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1031
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1032
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1033
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1034
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "HARMONICA BAND",
		"cca_generic_name": "ENSEMBLE - HARMONICA",
		"_id": 1035
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "STAGEWRIGHT",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1036
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1037
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "LIBRARY",
		"cca_generic_name": "LIBRARY COUNCIL",
		"_id": 1038
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LDDS - CHINESE",
		"_id": 1039
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM AND MEDIA CLUB",
		"cca_generic_name": "IT CLUB",
		"_id": 1040
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "TINKERING CLUB",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1041
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1042
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1043
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1044
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SEPAK TAKRAW",
		"_id": 1045
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1046
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1047
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1048
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1049
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1050
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1051
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCDCC",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1052
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1053
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1054
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1055
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1056
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INDIAN",
		"_id": 1057
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1058
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "D'LITE (ENGLISH DRAMA)",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1059
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AVA CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1060
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "APERTURE",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1061
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ROBOTICS CLUB",
		"cca_generic_name": "RADIO CONTROL AND ROBOTICS CLUB",
		"_id": 1062
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1063
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CROSS COUNTRY",
		"_id": 1064
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SEPAK TAKRAW",
		"_id": 1065
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1066
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TAEKWONDO",
		"_id": 1067
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TCHOUKBALL",
		"_id": 1068
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1069
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1070
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "SINGAPORE RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1071
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1072
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1073
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1074
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1075
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1076
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - TAMIL",
		"_id": 1077
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1078
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1079
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1080
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SEPAK TAKRAW",
		"_id": 1081
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1082
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1083
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1084
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1085
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1086
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 1087
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE - MODERN & CULTURAL",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1088
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1089
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INDIAN",
		"_id": 1090
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1091
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1092
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INTERACT CLUB",
		"_id": 1093
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "FESTIVE DRUMS AND LION DANCE TROUPE",
		"cca_generic_name": "LION DANCE TROUPE",
		"_id": 1094
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE YOUTH FLYING CLUB",
		"_id": 1095
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 1096
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MECHATRONICS CLUB",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1097
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 1098
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1099
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1100
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1101
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1102
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1103
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1104
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1105
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1106
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1107
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1108
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 1109
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1110
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1111
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MODERN DANCE",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1112
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MALAY DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1113
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1114
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BAND SYMPHONIC",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1115
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1116
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AV MEDIA CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1117
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "STUDENT LEADERS' BOARD",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 1118
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1119
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1120
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1121
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1122
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TAEKWONDO",
		"_id": 1123
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TEN-PIN BOWLING",
		"_id": 1124
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1125
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1126
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1127
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE ENSEMBLES",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1128
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1129
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1130
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1131
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1132
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1133
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "COMPUTER CLUB",
		"_id": 1134
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "LITERARY & ORATORICAL CLUB",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 1135
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ENTERPRISE CLUB",
		"cca_generic_name": "ENTREPRENEUR CLUB",
		"_id": 1136
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1137
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1138
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "NETBALL",
		"cca_generic_name": "NETBALL",
		"_id": 1139
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL",
		"cca_generic_name": "FOOTBALL",
		"_id": 1140
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1141
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1142
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1143
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST JOHN BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1144
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (LAND) (BOYS)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1145
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SHOW CHOIR",
		"cca_generic_name": "CHOIR",
		"_id": 1146
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE DYNAMICS",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1147
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MODERN CHINESE DANCE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1148
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MALAY DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1149
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1150
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1151
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1152
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIATECH CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1153
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "PHOTO AND VIDEO CLUB",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 1154
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MAKER FAIRE CLUB",
		"cca_generic_name": "YOUNG INVENTORS' CLUB",
		"_id": 1155
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1156
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1157
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1158
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1159
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1160
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1161
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TAEKWONDO",
		"_id": 1162
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1163
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1164
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1165
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1166
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1167
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1168
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 1169
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1170
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INDIAN",
		"_id": 1171
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1172
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1173
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BOWEN ARTISTS",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1174
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LIBRARY",
		"_id": 1175
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AIMS CLUB",
		"cca_generic_name": "MEDIA RESOURCE AND IT CLUB",
		"_id": 1176
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SHOOTING",
		"cca_generic_name": "AIR RIFLE / SHOOTING",
		"_id": 1177
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1178
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1179
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1180
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TEN-PIN BOWLING",
		"_id": 1181
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1182
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1183
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1184
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1185
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1186
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1187
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1188
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "WIND ORCHESTRA",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1189
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "CHESS CLUB",
		"_id": 1190
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "PHOTOGRAPHY CLUB",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 1191
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ARTS SOCIETY",
		"_id": 1192
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 1193
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOM CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1194
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1195
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL",
		"cca_generic_name": "BASKETBALL",
		"_id": 1196
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "ATHLETICS",
		"cca_generic_name": "CROSS COUNTRY",
		"_id": 1197
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "NETBALL (GIRLS)",
		"cca_generic_name": "NETBALL",
		"_id": 1198
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL (BOYS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 1199
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOFTBALL (GIRLS)",
		"cca_generic_name": "SOFTBALL",
		"_id": 1200
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1201
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "VOLLEYBALL (BOYS)",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1202
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1203
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1204
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1205
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1206
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1207
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE ORCHESTRA",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1208
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1209
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SYMPHONIC BAND",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1210
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUZHENG ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1211
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "HARP ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - LAP HARP",
		"_id": 1212
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE SOCIETY",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1213
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DRAMA SOCIETY",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 1214
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH DRAMA & DEBATING CLUB",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1215
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART AND DESIGN CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1216
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CALLIGRAPHY CLUB",
		"cca_generic_name": "CHINESE CALLIGRAPHY AND BRUSH PAINTING",
		"_id": 1217
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "IT CLUB",
		"_id": 1218
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INNOVATION CLUB",
		"cca_generic_name": "INNOVATION SOCIETY",
		"_id": 1219
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN HUA HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SERVICE LEARNING CLUB",
		"_id": 1220
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1221
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1222
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1223
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 1224
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1225
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1226
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1227
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "AIR SCOUTS",
		"cca_generic_name": "SCOUTS",
		"_id": 1228
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 1229
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1230
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MODERN DANCE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1231
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MALAY DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1232
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA CLUB",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1233
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1234
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1235
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE YOUTH FLYING CLUB",
		"_id": 1236
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1237
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "MEDIA CLUB",
		"_id": 1238
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "RUGBY",
		"_id": 1239
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1240
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1241
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TCHOUKBALL",
		"_id": 1242
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1243
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1244
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1245
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1246
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1247
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1248
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1249
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1250
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1251
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA LITERACY CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1252
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1253
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1254
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1255
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1256
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SEPAK TAKRAW",
		"_id": 1257
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1258
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SWIMMING",
		"_id": 1259
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1260
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 1261
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1262
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1263
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST. JOHN BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1264
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1265
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (SEA)",
		"_id": 1266
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1267
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1268
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BAND",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 1269
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MOVEMENT & DANCE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1270
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1271
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1272
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB (Animation)",
		"cca_generic_name": "IT CLUB",
		"_id": 1273
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "COMMUNITY SERVICE CLUB",
		"cca_generic_name": "CABIN",
		"_id": 1274
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1275
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB (AVA)",
		"cca_generic_name": "AUDIO VIDEO AND INFORMATION TECHNOLOGY CLUB",
		"_id": 1276
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "CANOEING",
		"cca_generic_name": "CANOEING/ROWING/DRAGON BOAT",
		"_id": 1277
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1278
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "RUGBY",
		"_id": 1279
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 1280
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1281
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1282
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1283
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1284
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1285
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1286
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1287
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1288
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE - ETHNIC",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1289
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1290
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1291
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1292
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1293
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "HOCKEY",
		"_id": 1294
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1295
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1296
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 1297
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1298
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1299
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 1300
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1301
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUZHENG",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1302
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1303
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MULTI CULTURAL ARTISTE CLUB",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1304
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INDIAN",
		"_id": 1305
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1306
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - PIPE",
		"_id": 1307
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "GREEN CLUB",
		"_id": 1308
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB (AVA, PHOTOGRAPHY & VIDEOGRAPHY)",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1309
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1310
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "JUDO",
		"_id": 1311
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1312
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "RUGBY",
		"_id": 1313
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1314
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1315
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1316
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1317
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1318
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1319
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1320
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1321
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1322
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1323
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1324
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1325
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ALPHA ROBOTICS",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1326
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1327
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1328
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1329
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1330
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SEPAK TAKRAW",
		"_id": 1331
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1332
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SAILING",
		"_id": 1333
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TCHOUKBALL",
		"_id": 1334
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1335
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1336
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1337
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1338
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1339
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1340
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CULTURAL ENSEMBLE - MALAY",
		"cca_generic_name": "ENSEMBLE - ANGKLUNG/KULINTANG",
		"_id": 1341
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1342
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1343
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRUMATIX BATUCADA",
		"cca_generic_name": "ENSEMBLE - PERCUSSION",
		"_id": 1344
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1345
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1346
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1347
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1348
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1349
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON",
		"cca_generic_name": "BADMINTON",
		"_id": 1350
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL",
		"cca_generic_name": "BASKETBALL",
		"_id": 1351
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1352
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL",
		"cca_generic_name": "FOOTBALL",
		"_id": 1353
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "BOYS' BRIGADE",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1354
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1355
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NPCC",
		"cca_generic_name": "NPCC",
		"_id": 1356
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST JOHN BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1357
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1358
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (LAND)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1359
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1360
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1361
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "LIBRARY/EDITORIAL CLUB",
		"cca_generic_name": "LIBRARY COUNCIL",
		"_id": 1362
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ARTS SOCIETY (CHOIR & DANCE)",
		"cca_generic_name": "ARTS SOCIETY",
		"_id": 1363
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "IT CLUB",
		"_id": 1364
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "Badminton",
		"cca_generic_name": "BADMINTON",
		"_id": 1365
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "Basketball",
		"cca_generic_name": "BASKETBALL",
		"_id": 1366
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "Football",
		"cca_generic_name": "FOOTBALL",
		"_id": 1367
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "Table Tennis (Girls)",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1368
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FRISBEE",
		"_id": 1369
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "Boy's Brigade",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1370
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "Girls' Brigade",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1371
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NPCC",
		"cca_generic_name": "NPCC",
		"_id": 1372
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST JOHN AMBULANCE BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1373
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (Land)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1374
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "School Choir",
		"cca_generic_name": "CHOIR",
		"_id": 1375
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Symphonic Band",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1376
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Modern Dance Club",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1377
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "K-PRODUCTIONS SOCIETY",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1378
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "K-PRODUCTION TECHNICAL",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1379
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "DEBATE",
		"cca_generic_name": "DEBATING AND ORATORICAL SOCIETY",
		"_id": 1380
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA INNOVATION",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 1381
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ENVIRONMENT SERVICE LEARNING (ECOS)",
		"cca_generic_name": "EARTH WATCH",
		"_id": 1382
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ARTS AND INNOVATION CLUB",
		"_id": 1383
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1384
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1385
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "HOCKEY",
		"_id": 1386
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1387
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1388
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 1389
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FRISBEE",
		"_id": 1390
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1391
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NATIONAL POLICE CADET CORPS",
		"cca_generic_name": "NPCC",
		"_id": 1392
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1393
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NATIONAL CADET CORPS",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1394
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1395
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1396
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1397
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1398
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ENGLISH LITERARY DRAMA & DEBATE SOCIETY",
		"cca_generic_name": "LDDS - ENGLISH",
		"_id": 1399
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "STUDENT LEADERSHIP",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 1400
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "AUDIO VIDEO AND INFORMATION TECHNOLOGY CLUB",
		"_id": 1401
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SCIENCE CLUB",
		"_id": 1402
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ARTS AND INNOVATION CLUB",
		"_id": 1403
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1404
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1405
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "CANOEING",
		"cca_generic_name": "CANOEING/ROWING/DRAGON BOAT",
		"_id": 1406
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1407
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 1408
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1409
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1410
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1411
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1412
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1413
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1414
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MALAY DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1415
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1416
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1417
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART & CRAFT",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1418
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "OUTDOOR ADVENTURE CLUB",
		"cca_generic_name": "OUTDOOR ACTIVITIES CLUB",
		"_id": 1419
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE YOUTH FLYING CLUB",
		"_id": 1420
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ENVIRONMENT CLUB",
		"cca_generic_name": "ENVIRONMENTAL CLUB",
		"_id": 1421
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1422
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1423
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1424
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1425
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "ATHLETICS",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1426
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "GOLF",
		"_id": 1427
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1428
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1429
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1430
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1431
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1432
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - STRING",
		"_id": 1433
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1434
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1435
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1436
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA CLUB",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1437
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ODAC",
		"cca_generic_name": "OUTDOOR ACTIVITIES CLUB",
		"_id": 1438
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1439
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON",
		"cca_generic_name": "BADMINTON",
		"_id": 1440
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "AIR PISTOL/ SHOOTING",
		"cca_generic_name": "AIR RIFLE / SHOOTING",
		"_id": 1441
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1442
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1443
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 1444
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TAEKWONDO",
		"_id": 1445
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1446
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1447
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1448
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1449
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC (SEA)",
		"_id": 1450
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1451
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1452
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - HARMONICA",
		"_id": 1453
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1454
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "FESTIVE DRUMS",
		"cca_generic_name": "ENSEMBLE - PERCUSSION",
		"_id": 1455
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1456
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH LITERARY DRAMA AND DEBATE SOCIETY",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1457
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1458
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1459
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE YOUTH FLYING CLUB",
		"_id": 1460
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1461
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "NEW MEDIA CLUB",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 1462
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "THINKERS SOCIETY",
		"cca_generic_name": "INNOVATION SOCIETY",
		"_id": 1463
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ENTREPRENEUR CLUB",
		"_id": 1464
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1465
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1466
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1467
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1468
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 1469
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1470
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1471
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCDCC",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1472
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MERIDIAN NUSANTARA ORCHESTRA",
		"cca_generic_name": "ENSEMBLE - ANGKLUNG/KULINTANG",
		"_id": 1473
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1474
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE CLUB",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1475
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA & DEBATING SOCIETY",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1476
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SYMPHONIC BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1477
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1478
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA CLUB",
		"cca_generic_name": "MEDIA RESOURCE AND IT CLUB",
		"_id": 1479
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "AIR RIFLE/SHOOTING",
		"cca_generic_name": "AIR RIFLE / SHOOTING",
		"_id": 1480
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1482
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1484
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "NETBALL (SENIOR HIGH)",
		"cca_generic_name": "NETBALL",
		"_id": 1486
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOCCER (SENIOR HIGH)",
		"cca_generic_name": "FOOTBALL",
		"_id": 1488
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOFTBALL (GIRLS)",
		"cca_generic_name": "SOFTBALL",
		"_id": 1490
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SAILING (SENIOR HIGH)",
		"cca_generic_name": "SAILING",
		"_id": 1492
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1494
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1496
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TENNIS (SENIOR HIGH)",
		"cca_generic_name": "TENNIS",
		"_id": 1498
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TAEKWONDO (JUNIOR HIGH)",
		"cca_generic_name": "TAEKWONDO",
		"_id": 1500
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1502
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1504
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BOWLING (JUNIOR HIGH)",
		"cca_generic_name": "TEN-PIN BOWLING",
		"_id": 1506
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "GOLF (JUNIOR HIGH)",
		"cca_generic_name": "GOLF",
		"_id": 1508
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1510
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1512
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST. JOHN BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1514
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1516
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE ORCHESTRA",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1518
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1520
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUITAR ENSEMBLE (SENIOR HIGH)",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 1522
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "STRING ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - STRING",
		"_id": 1524
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SYMPHONIC BAND",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1526
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUZHENG ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1528
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "INTERNATIONAL DANCE",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1530
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DANCE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1532
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DRAMA",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 1534
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1536
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BEIJING OPERA",
		"cca_generic_name": "DRAMA - OPERA/OPERATTA",
		"_id": 1538
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1540
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ROBOTICS CLUB",
		"cca_generic_name": "COMPUTER CLUB",
		"_id": 1542
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ORATORICAL SOCIETY",
		"cca_generic_name": "DEBATING AND ORATORICAL SOCIETY",
		"_id": 1544
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "JAPANESE CULTURAL CLUB (SENIOR HIGH)",
		"cca_generic_name": "JAPANESE CLUB",
		"_id": 1546
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "LIBRARY SOCIETY",
		"cca_generic_name": "LIBRARY COUNCIL",
		"_id": 1548
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "LION DANCE (By Scouts)",
		"cca_generic_name": "LION DANCE TROUPE",
		"_id": 1550
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MATHEMATICS & SCIENCE PROGRAMME (MATHEMATICS)",
		"cca_generic_name": "MATHEMATICS SOCIETY",
		"_id": 1552
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "PHOTOGRAHIC SOCIETY(SENIOR HIGH)",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 1554
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 1556
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "SCIENCE SOCIETY (SENIOR HIGH)",
		"cca_generic_name": "SCIENCE SOCIETY",
		"_id": 1558
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1590
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "SINGAPORE YOUTH FLYING CLUB (SENIOR HIGH)",
		"cca_generic_name": "SINGAPORE YOUTH FLYING CLUB",
		"_id": 1560
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE CALLIGRAPHY",
		"cca_generic_name": "CHINESE CALLIGRAPHY SOCIETY",
		"_id": 1562
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "PUBLICATIONS (Senior High)",
		"cca_generic_name": "COLLEGE PUBLICATIONS",
		"_id": 1564
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "COMMUNITY SERVICE CLUB (SENIOR HIGH)",
		"cca_generic_name": "COMMUNITY SERVICE CLUB",
		"_id": 1566
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "PA CREW (SENIOR HIGH)",
		"cca_generic_name": "PA CREW",
		"_id": 1568
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1570
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1572
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL",
		"cca_generic_name": "BASKETBALL",
		"_id": 1574
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1576
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 1578
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1580
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1582
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "VOLLEYBALL",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1584
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FLOORBALL",
		"cca_generic_name": "FLOORBALL",
		"_id": 1586
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1588
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1592
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1594
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1596
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE ORCHESTRA",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1598
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1600
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUITAR ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 1602
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1604
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "HISTORY AND CURRENT AFFAIRS SOCIETY",
		"cca_generic_name": "HISTORY/CURRENT AFFAIRS SOCIETY",
		"_id": 1606
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "PHOTOGRAPHY CLUB",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 1608
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "STUDENT LEADERSHIP DEVELOPMENT ACADEMY",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 1610
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "SCIENCE LEADERS ACADEMY",
		"cca_generic_name": "SCIENCE SOCIETY",
		"_id": 1612
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE YOUTH FLYING CLUB",
		"_id": 1614
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "LIBRARY AND EDITORIAL CLUB",
		"cca_generic_name": "EDITORIAL BOARD",
		"_id": 1616
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "THE ECO-SUSTAINABILITY LEADERSHIP ACADEMY",
		"cca_generic_name": "ENVIRONMENTAL CLUB",
		"_id": 1618
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1620
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVER VALLEY HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "SERVICE AND CITIZENSHIP SOCIETY",
		"cca_generic_name": "SERVICE LEARNING CLUB",
		"_id": 1622
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1624
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CANOEING/ROWING/DRAGON BOAT",
		"_id": 1625
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FENCING",
		"_id": 1626
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "HOCKEY",
		"_id": 1627
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1628
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1629
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1630
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1631
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1632
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1633
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1634
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1635
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1636
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 1637
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1638
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 1639
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1640
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "BP Com Link",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1641
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "MALAY CULTURAL SOCIETY",
		"_id": 1642
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1706
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SCIENCE SOCIETY",
		"_id": 1643
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1644
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BUKIT PANJANG GOVT. HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SERVICE LEARNING CLUB",
		"_id": 1645
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON (BOYS)",
		"cca_generic_name": "BADMINTON",
		"_id": 1646
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1647
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1648
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL (GIRLS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 1649
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TABLE TENNIS (BOYS)",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1650
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1651
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1652
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1653
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1654
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (AIR) (BOYS)",
		"cca_generic_name": "NCC(AIR)",
		"_id": 1655
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (LAND) (BOYS)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1656
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1657
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 1658
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - STRING",
		"_id": 1659
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1660
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "STAGEARTS DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1661
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1662
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "COMPUTER CLUB",
		"_id": 1663
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 1664
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1665
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1666
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SEPAK TAKRAW",
		"cca_generic_name": "SEPAK TAKRAW",
		"_id": 1667
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOCCER",
		"cca_generic_name": "FOOTBALL",
		"_id": 1668
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1669
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1670
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1671
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1672
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1673
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1674
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 1737
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1675
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1676
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SYMPHONIC BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1677
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1678
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "SERVICE LEARNING CLUB",
		"cca_generic_name": "LIBRARY",
		"_id": 1679
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1680
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON (BOYS)",
		"cca_generic_name": "BADMINTON",
		"_id": 1681
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (BOYS & GIRLS)",
		"cca_generic_name": "BASKETBALL",
		"_id": 1682
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1683
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1684
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1685
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1686
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1687
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1688
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (LAND) - BOYS & GIRLS",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1689
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - ANGKLUNG/KULINTANG",
		"_id": 1690
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1691
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1692
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1693
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1694
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1695
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SERVICE LEARNING CLUB",
		"_id": 1696
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "MEDIA RESOURCE AND IT CLUB",
		"_id": 1697
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "na",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 1698
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1699
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1700
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1701
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1702
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1703
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1704
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 1705
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NATIONAL POLICE CADET CORPS (NPCC)",
		"cca_generic_name": "NPCC",
		"_id": 1707
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1708
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NATIONAL CADET CORPS (NCC)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1709
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SHOW CHOIR",
		"cca_generic_name": "CHOIR",
		"_id": 1710
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUZHENG ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1711
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "HIP-HOP DANCE CLUB",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1712
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE SOCIETY",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1713
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1714
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "AESTHETICS & DESIGN CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1715
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ENGLISH LITERARY DRAMA DEBATE SOCIETY (ELDDS)",
		"cca_generic_name": "LDDS - ENGLISH",
		"_id": 1716
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE YOUTH FLYING CLUB",
		"_id": 1717
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CHINESE CULTURAL SOCIETY",
		"cca_generic_name": "LDDS - CHINESE",
		"_id": 1718
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1719
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "NUTRITION & FOOD SCIENCE CLUB",
		"cca_generic_name": "HOME ECONOMICS",
		"_id": 1720
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INNOVATION AND ENTREPRENEUR CLUB",
		"cca_generic_name": "INNOVATION AND ENTERPRISE CLUB",
		"_id": 1721
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON (BOYS)",
		"cca_generic_name": "BADMINTON",
		"_id": 1722
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (GIRLS)",
		"cca_generic_name": "BASKETBALL",
		"_id": 1723
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL (GIRLS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 1724
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1725
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1726
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "VOLLEYBALL (BOYS)",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1727
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "ODAC",
		"cca_generic_name": "ADVENTURE CLUB",
		"_id": 1728
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1729
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1730
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1731
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1732
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BAND",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 1733
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MOVEMENT AND DANCE CLUB",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1734
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1735
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1736
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "IT CLUB",
		"_id": 1738
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "YOUNG JOURNALISTS CLUB",
		"_id": 1739
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1740
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 1741
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1742
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1743
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1744
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1745
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (SEA)",
		"_id": 1746
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1747
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1748
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1749
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1750
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "AERO-MODELLING",
		"_id": 1751
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1752
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "IT CLUB",
		"_id": 1753
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1754
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1755
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1756
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1757
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1758
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1759
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1760
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1761
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1762
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE ORCHESTRA",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1763
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1764
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MALAY DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1765
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1766
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA CLUB",
		"cca_generic_name": "MUSIC, DRAMA & DANCE CLUB",
		"_id": 1767
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 1768
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "TINKERS' CLUB",
		"cca_generic_name": "RADIO CONTROL AND ROBOTICS CLUB",
		"_id": 1769
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "na",
		"cca_generic_name": "PREFECTORIAL BOARD",
		"_id": 1770
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1771
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1772
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1773
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "CROSS COUNTRY",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1774
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1775
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1776
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1777
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1778
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1779
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1780
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1781
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1904
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE",
		"cca_generic_name": "MUSIC, DRAMA & DANCE CLUB",
		"_id": 1782
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AUDIO VISUAL CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1783
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "COMPUTER CLUB",
		"_id": 1784
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "OUTDOOR ACTIVITIES CLUB",
		"_id": 1785
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 1786
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1787
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1788
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1789
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1790
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOFTBALL (GIRLS ONLY)",
		"cca_generic_name": "SOFTBALL",
		"_id": 1791
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1792
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1793
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1794
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST JOHN BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1795
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (SEA)",
		"_id": 1796
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1797
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1798
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1799
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE - CHINESE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1800
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INDIAN",
		"_id": 1801
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1802
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1803
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "VISUAL ARTS",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1804
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1805
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1806
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON (GIRLS)",
		"cca_generic_name": "BADMINTON",
		"_id": 1807
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (MIXED)",
		"cca_generic_name": "BASKETBALL",
		"_id": 1808
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL (BOYS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 1809
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FLOORBALL (MIXED)",
		"cca_generic_name": "FLOORBALL",
		"_id": 1810
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TENPIN BOWLING (BOYS)",
		"cca_generic_name": "TEN-PIN BOWLING",
		"_id": 1811
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1812
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1813
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1814
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST. JOHN BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1815
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1816
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 1817
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE ORCHESTRA",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 1818
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHOIR",
		"cca_generic_name": "CHOIR",
		"_id": 1819
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SWISS WINDS (Command Band of the National Cadet Corps)",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1820
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DANCE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1821
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MALAY DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1822
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1823
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "STUDENT COUNCIL",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 1824
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "SCIENCE & TECHNOLOGY",
		"cca_generic_name": "SCIENCE SOCIETY",
		"_id": 1825
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "SWISS NATURALISTS",
		"cca_generic_name": "ENVIRONMENTAL CLUB",
		"_id": 1826
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "PUBLICATIONS AND MEDIA CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1827
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "na",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 1828
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1829
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1830
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1831
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 1832
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1833
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1834
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1835
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1836
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1837
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1838
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE CONTEMPORARY DANCE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1839
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ETHNIC FUSION DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1840
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1841
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1842
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA & COMMUNICATIONS",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1843
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CREATIVE READERS CLUB",
		"cca_generic_name": "LIBRARY",
		"_id": 1844
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "LANGUAGE ART(2ND CCA)",
		"cca_generic_name": "LANGUAGE ART",
		"_id": 1845
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON(BOYS)",
		"cca_generic_name": "BADMINTON",
		"_id": 1846
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL(BOYS)",
		"cca_generic_name": "BASKETBALL",
		"_id": 1847
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "NETBALL",
		"cca_generic_name": "NETBALL",
		"_id": 1848
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL(BOYS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 1849
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TABLE TENNIS(BOYS)",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1850
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FLOORBALL(GIRLS)",
		"cca_generic_name": "FLOORBALL",
		"_id": 1851
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1852
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1853
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1854
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1855
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1856
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC(BOYS)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1857
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1858
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1859
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE - INTL",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 1860
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1861
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA CLUB",
		"cca_generic_name": "IT CLUB",
		"_id": 1862
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ROBOTICS CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1863
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "THE STUDENTS' COUNCIL",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 1864
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "na",
		"cca_generic_name": "PREFECTORIAL BOARD",
		"_id": 1865
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON",
		"cca_generic_name": "BADMINTON",
		"_id": 1866
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1867
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FENCING",
		"_id": 1868
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1869
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1870
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1871
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1872
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1873
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1874
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1875
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1876
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 1877
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUZHENG ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1878
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "PERCUSSION ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - PERCUSSION",
		"_id": 1879
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Contemporary Dance",
		"cca_generic_name": "DANCE - BALLET",
		"_id": 1880
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DANCE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1881
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "Infocomm Club",
		"cca_generic_name": "IT CLUB",
		"_id": 1882
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "AIR RIFLE / SHOOTING",
		"_id": 1883
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (BOYS)",
		"cca_generic_name": "BASKETBALL",
		"_id": 1884
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1885
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL (BOYS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 1886
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1887
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FLOORBALL (GIRLS)",
		"cca_generic_name": "FLOORBALL",
		"_id": 1888
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1889
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1890
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1891
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1892
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (SEA)",
		"_id": 1893
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1894
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BAND-DISPLAY/CONCERT",
		"cca_generic_name": "BAND - DISPLAY/MARCHING",
		"_id": 1895
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1896
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1897
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1898
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AVMC (AV MEDIA & COMPUTER)",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1899
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "CHESS CLUB",
		"_id": 1900
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON (BOYS ONLY)",
		"cca_generic_name": "BADMINTON",
		"_id": 1901
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (BOYS ONLY)",
		"cca_generic_name": "BASKETBALL",
		"_id": 1902
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "HOCKEY (BOYS ONLY)",
		"cca_generic_name": "HOCKEY",
		"_id": 1903
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOFTBALL (BOYS ONLY)",
		"cca_generic_name": "SOFTBALL",
		"_id": 1905
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "VOLLEYBALL (GIRLS ONLY)",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1906
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1907
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (LAND) (BOYS ONLY)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1908
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1909
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1910
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1911
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUZHENG ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1912
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE - CONTEMPORARY",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1913
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DANCE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1914
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MALAY DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1915
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH DRAMA CLUB",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1916
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AVA/PHOTOGRAPHY CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1917
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 1918
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA RESOURCE LIBRARY",
		"cca_generic_name": "LIBRARY",
		"_id": 1919
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (BOYS)",
		"cca_generic_name": "BASKETBALL",
		"_id": 1920
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "HOCKEY (BOYS)",
		"cca_generic_name": "HOCKEY",
		"_id": 1921
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "NETBALL (GIRLS)",
		"cca_generic_name": "NETBALL",
		"_id": 1922
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL (BOYS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 1923
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "WUSHU (MIXED)",
		"cca_generic_name": "WUSHU",
		"_id": 1924
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FLOORBALL (BOYS & GIRLS)",
		"cca_generic_name": "FLOORBALL",
		"_id": 1925
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1926
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1927
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1928
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (SEA)",
		"_id": 1929
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 1930
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Joaquim Chorale",
		"cca_generic_name": "CHOIR",
		"_id": 1931
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUITAR ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 1932
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Wind Orchestra",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 1933
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE CLUB",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1934
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA CLUB",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1935
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1936
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIATECH CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1937
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON TEAM",
		"cca_generic_name": "BADMINTON",
		"_id": 1938
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "NETBALL TEAM",
		"cca_generic_name": "NETBALL",
		"_id": 1939
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOCCER TEAM",
		"cca_generic_name": "FOOTBALL",
		"_id": 1940
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "VOLLEYBALL TEAM",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1941
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FLOORBALL TEAM",
		"cca_generic_name": "FLOORBALL",
		"_id": 1942
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "BOYS' BRIGADE",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1943
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "GIRLS' BRIGADE",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1944
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NATIONAL POLICE CADET CORPS",
		"cca_generic_name": "NPCC",
		"_id": 1945
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NATIONAL CADET CORPS (SEA)",
		"cca_generic_name": "NCC (SEA)",
		"_id": 1946
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DANCE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 1947
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MALAY DANCE",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 1948
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND - SEMBWINDS",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 1949
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART AND DESIGN CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1950
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AUDIO VISUAL AIDS CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1951
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIACOMM CLUB",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 1952
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1953
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1954
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "HOCKEY",
		"_id": 1955
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 1956
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 1957
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 1958
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1959
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 1960
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1961
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1962
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1963
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 1964
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1965
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1966
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 1967
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA SERVICES CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 1968
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "PROJECT CABIN",
		"cca_generic_name": "CABIN",
		"_id": 1969
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ARCHERY",
		"_id": 1970
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 1971
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1972
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "RUGBY",
		"_id": 1973
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1974
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 1975
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1976
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1977
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1978
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1979
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 1980
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 1981
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1982
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 1983
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 1984
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE - MODERN",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 1985
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 1986
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "LIBRARY CLUB",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 1987
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 1988
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 1989
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SEPAK TAKRAW",
		"_id": 1990
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TRACK & FIELD",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 1991
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 1992
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 1993
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 1994
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 1995
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 1996
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 1997
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 1998
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 1999
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 2000
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - INDIAN",
		"_id": 2001
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 2002
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2003
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 2004
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SPEECH AND DRAMA SOCIETY",
		"_id": 2005
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LIBRARY",
		"_id": 2006
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ENVIRONMENTAL CLUB",
		"_id": 2007
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "na",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 2008
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2009
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2010
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 2011
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 2012
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2013
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2014
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 2015
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Guzheng Ensemble",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 2016
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Modern Dance",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2017
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Drama Club",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2018
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Concert Band",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2019
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "Northbrooks Youth Flying Club",
		"cca_generic_name": "AERO-MODELLING",
		"_id": 2020
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENVIRONMENTAL ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 2021
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "Audio Visual Aids Club",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2022
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "OUTDOOR ACTIVITIES CLUB",
		"_id": 2023
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "PHOTOGRAPHY CLUB",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 2024
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "Infocomm Club",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 2025
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SCRABBLE CLUB",
		"_id": 2026
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2027
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "HOCKEY",
		"_id": 2028
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2029
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 2030
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2031
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2032
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (SEA)",
		"_id": 2033
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2034
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "INTERNATIONAL DANCE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2035
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 2036
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA SOCIETY",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2037
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2038
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 2039
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LIBRARY COUNCIL",
		"_id": 2040
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AVA / INFOCOMM CLUB",
		"cca_generic_name": "AUDIO VIDEO AND INFORMATION TECHNOLOGY CLUB",
		"_id": 2041
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON (BOYS)",
		"cca_generic_name": "BADMINTON",
		"_id": 2042
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2043
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2044
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2045
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2046
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TAEKWONDO",
		"_id": 2047
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 2048
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2049
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2050
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SHOW CHOIR",
		"cca_generic_name": "CHOIR",
		"_id": 2051
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MOVEMENT & DANCE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2052
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ELDS",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2053
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2054
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AVPA",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2055
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "GREEN BOOK CLUB",
		"cca_generic_name": "GREEN CLUB",
		"_id": 2056
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 2057
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ENTREPRENEUR CLUB",
		"_id": 2058
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 2059
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON (B&G)",
		"cca_generic_name": "BADMINTON",
		"_id": 2060
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (B&G)",
		"cca_generic_name": "BASKETBALL",
		"_id": 2061
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2062
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOFTBALL (B&G)",
		"cca_generic_name": "SOFTBALL",
		"_id": 2063
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FLOORBALL (B&G)",
		"cca_generic_name": "FLOORBALL",
		"_id": 2064
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 2065
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2066
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2067
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "SINGAPORE RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2068
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 2069
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2070
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MODERN DANCE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2071
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2072
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2073
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AERONAUTICS",
		"cca_generic_name": "AERO-MODELLING",
		"_id": 2074
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "PA/AVA/ROBOTICS",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2075
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LIBRARY",
		"_id": 2076
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ENVIRONMENT",
		"cca_generic_name": "ENVIRONMENTAL CLUB",
		"_id": 2077
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "VIDEOGRAPHY",
		"cca_generic_name": "MEDIA RESOURCE AND IT CLUB",
		"_id": 2078
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2435
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2436
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2437
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SQUASH",
		"_id": 2438
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "ATHLETICS",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 2439
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TENNIS",
		"_id": 2440
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TEN-PIN BOWLING",
		"_id": 2441
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "GYMNASTICS (RHYTHMIC)",
		"cca_generic_name": "RHYTHMIC GYMNASTICS",
		"_id": 2442
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2443
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2444
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2445
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUITAR ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 2446
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE ENSEMBLE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2447
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE LDDS",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 2448
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "IJ THEATER",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2449
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BAND (CONCERT)",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2450
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "DEBATING AND ORATORY SOCIETY",
		"cca_generic_name": "DEBATING AND ORATORICAL SOCIETY",
		"_id": 2451
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LEGION OF MARY",
		"_id": 2452
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "OUTDOOR ACTIVITIES CLUB",
		"_id": 2453
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "IJ MEDIA CLUB",
		"cca_generic_name": "EDITORIAL BOARD",
		"_id": 2454
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ARC (ROBOTICS)",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 2455
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ARTS ALIVE!",
		"cca_generic_name": "ARTS AND INNOVATION CLUB",
		"_id": 2456
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "CHIJ YOUTH MISSION",
		"_id": 2457
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "na",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 2458
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "na",
		"cca_generic_name": "HOUSE APPOINTMENT",
		"_id": 2459
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2460
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2461
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2462
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2463
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 2464
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "ATHLETICS",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 2465
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 2466
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 2467
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TEN-PIN BOWLING",
		"_id": 2468
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 2469
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 2470
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2471
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2472
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2473
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 2474
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 2475
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2476
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "BOARD GAMES CLUB",
		"cca_generic_name": "CHESS CLUB",
		"_id": 2477
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "DIGITAL MEDIA CLUB",
		"cca_generic_name": "COMPUTER CLUB",
		"_id": 2478
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 2479
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 2480
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "PHOTO AND VIDEO SOCIETY",
		"cca_generic_name": "YOUNG JOURNALISTS CLUB",
		"_id": 2481
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON",
		"cca_generic_name": "BADMINTON",
		"_id": 2482
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "CANOEING",
		"cca_generic_name": "CANOEING/ROWING/DRAGON BOAT",
		"_id": 2483
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2484
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 2485
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 2486
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TEN-PIN BOWLING",
		"_id": 2487
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2488
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCDCC",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 2489
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2490
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2491
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2492
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DRAMA",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 2493
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMATIC ARTS SOCIETY",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2494
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2495
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "DEBATE CLUB",
		"cca_generic_name": "DEBATING AND ORATORICAL SOCIETY",
		"_id": 2496
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CABIN CLUB",
		"cca_generic_name": "CABIN",
		"_id": 2497
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ENTREPRENEUR CLUB",
		"_id": 2498
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA COMMUNICATIONS CLUB (PREVIOUSLY INFOCOMM CLUB)",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 2499
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ KATONG CONVENT",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "IJYM",
		"cca_generic_name": "CHIJ YOUTH MISSION",
		"_id": 2500
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2501
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2502
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "RUGBY",
		"_id": 2503
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2504
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 2505
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TAEKWONDO",
		"_id": 2506
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 2507
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2508
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 2509
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 2510
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 2511
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2512
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 2513
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE CLUB",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2514
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "IDMA CLUB (AV)",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2515
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "DRAMA CLUB",
		"cca_generic_name": "LDDS - ENGLISH",
		"_id": 2516
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "STUDENTS' COUNCIL",
		"_id": 2517
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "YOUNG CHRISTIAN SOCIETY",
		"_id": 2518
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "IDMA CLUB (INFO COMM)",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 2519
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2520
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "JUDO",
		"_id": 2521
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "KARATE",
		"_id": 2522
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2523
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 2524
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 2525
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "GOLF",
		"_id": 2526
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NPCC",
		"cca_generic_name": "NPCC",
		"_id": 2527
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2528
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "SCOUTS",
		"cca_generic_name": "SCOUTS",
		"_id": 2529
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (AIR)",
		"cca_generic_name": "NCC(AIR)",
		"_id": 2530
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (LAND)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 2531
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "VOCAL ENSEMBLE",
		"cca_generic_name": "CHOIR",
		"_id": 2532
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUITAR ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 2533
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA AND DEBATE SOCIETY",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2534
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONCERT BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2535
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2536
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2537
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2538
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FENCING",
		"_id": 2539
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2540
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TENNIS",
		"_id": 2541
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 2542
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TEN-PIN BOWLING",
		"_id": 2543
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 2544
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2545
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2546
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2547
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2548
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - STRING",
		"_id": 2549
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 2550
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2551
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 2552
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INDIAN",
		"_id": 2553
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MALAY",
		"_id": 2554
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2555
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "DEBATE CLUB",
		"cca_generic_name": "LDDS - ENGLISH",
		"_id": 2556
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Creative Art Club",
		"cca_generic_name": "ARTS SOCIETY",
		"_id": 2557
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "Smarts Media",
		"cca_generic_name": "MEDIA RESOURCE CLUB",
		"_id": 2558
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AGAPE CLUB",
		"cca_generic_name": "CHRISTIAN SOCIETY",
		"_id": 2559
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LIBRARY",
		"_id": 2560
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "JOURNALISM CLUB",
		"cca_generic_name": "JOURNALISM BROADCAST",
		"_id": 2561
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "OTHERS",
		"cca_customized_name": "na",
		"cca_generic_name": "PREFECTORIAL BOARD",
		"_id": 2562
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2563
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2564
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CRICKET",
		"_id": 2565
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2566
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SQUASH",
		"_id": 2567
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 2568
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TENNIS",
		"_id": 2569
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "GOLF",
		"_id": 2570
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2571
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 2572
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC(AIR)",
		"_id": 2573
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 2574
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUITAR ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 2575
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "MILITARY BAND",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 2576
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2577
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LEGION OF MARY",
		"_id": 2578
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA RESOURCE LIBRARY",
		"cca_generic_name": "LIBRARY COUNCIL",
		"_id": 2579
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "SOCIETY OF ST. VINCENT DE PAUL",
		"cca_generic_name": "CHRISTIAN SOCIETY",
		"_id": 2580
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "ST. PATRICK'S SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 2581
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2582
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2583
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2584
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2585
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 2586
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 2587
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 2588
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2589
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 2590
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 2591
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2592
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2593
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SCHOOL BAND",
		"cca_generic_name": "BAND - MILITARY",
		"_id": 2594
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2595
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2596
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2597
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "OUTDOOR ACTIVITIES CLUB",
		"_id": 2598
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 2599
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CHRISTIAN FELLOWSHIP",
		"cca_generic_name": "CHRISTIAN SOCIETY",
		"_id": 2600
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2601
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2602
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SWIMMING",
		"_id": 2603
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 2604
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 2605
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 2606
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "RHYTHMIC GYMNASTICS",
		"_id": 2607
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 2608
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2609
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST. JOHN BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 2610
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2611
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUITAR",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 2612
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUZHENG",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 2613
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "HANDBELL ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - HANDBELL/HANDCHIME",
		"_id": 2614
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "HARP ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - LAP HARP",
		"_id": 2615
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2616
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "D'ARTS SOCIETY (CL DRAMA)",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 2617
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "EL DRAMA CLUB",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2618
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "BAND",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2619
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "DEBATE CLUB",
		"cca_generic_name": "LDDS - ENGLISH",
		"_id": 2620
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "PHOTOGRAPHY CLUB",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 2621
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA AND INFORMATION TECHNOLOGY CLUB",
		"cca_generic_name": "MEDIA RESOURCE AND IT CLUB",
		"_id": 2622
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "AIR RIFLE / SHOOTING",
		"_id": 2623
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2624
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2625
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2626
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2627
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SWIMMING",
		"_id": 2628
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 2629
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 2630
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 2631
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 2632
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2633
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NATIONAL POLICE CADET CORPS",
		"cca_generic_name": "NPCC",
		"_id": 2634
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NATIONAL CIVIL DEFENCE CADET CORPS",
		"_id": 2635
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2636
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 2637
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE - CONTEMPORARY",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2638
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 2639
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2640
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2641
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 2642
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "PHOTOGRAPHIC SOCIETY",
		"_id": 2643
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 2644
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INFOCOM CLUB",
		"_id": 2645
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL",
		"cca_generic_name": "BASKETBALL",
		"_id": 2647
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SOFTBALL",
		"cca_generic_name": "SOFTBALL",
		"_id": 2649
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TRACK & FIELD (WITH CROSS COUNTRY)",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 2651
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "TABLE TENNIS",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 2653
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "WUSHU",
		"cca_generic_name": "WUSHU",
		"_id": 2655
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "VOLLEYBALL",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 2657
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FLOORBALL",
		"cca_generic_name": "FLOORBALL",
		"_id": 2659
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NPCC",
		"cca_generic_name": "NPCC",
		"_id": 2660
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "St John Brigade",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 2662
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "Scouts",
		"cca_generic_name": "SCOUTS",
		"_id": 2664
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC(AIR)",
		"cca_generic_name": "NCC(AIR)",
		"_id": 2665
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC(LAND)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 2666
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Orchestra - Chinese",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2668
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Edward Becheras Choir",
		"cca_generic_name": "CHOIR",
		"_id": 2670
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Symphony Band",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 2672
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Dance - Modern",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2674
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Drama - Chinese",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 2676
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "Drama - English",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2678
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CATHOLIC HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ION (INFOCOMM & ROBOTICS)",
		"cca_generic_name": "IT CLUB",
		"_id": 2680
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (BOYS)",
		"cca_generic_name": "BASKETBALL",
		"_id": 2681
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "OUTDOOR ACTIVITIES CLUB",
		"cca_generic_name": "CANOEING/ROWING/DRAGON BOAT",
		"_id": 2682
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FENCING",
		"_id": 2683
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 2684
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 2685
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2686
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "ST JOHN BRIGADE",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 2687
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "PEREGRINE SCOUTS GROUP",
		"cca_generic_name": "SCOUTS",
		"_id": 2688
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (AIR)",
		"cca_generic_name": "NCC(AIR)",
		"_id": 2689
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2690
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2691
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 2692
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUZHENG ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 2693
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "FESTIVAL DRUMS",
		"cca_generic_name": "ENSEMBLE - PERCUSSION",
		"_id": 2694
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 2695
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 2696
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DRAMA CLUB",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 2697
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "AVA CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2698
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 2699
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHUNG CHENG HIGH SCHOOL (YISHUN)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ENTREPRENEUR CLUB",
		"_id": 2700
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2701
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL",
		"cca_generic_name": "BASKETBALL",
		"_id": 2702
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 2703
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 2704
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2705
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2706
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 2707
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 2708
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE ORCHESTRA",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2709
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2710
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "STRING ORCHESTRA",
		"cca_generic_name": "ENSEMBLE - STRING",
		"_id": 2711
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "WIND ORCHESTRA",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 2712
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CONTEMPORARY DANCE",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 2713
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DANCE",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 2714
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DRAMA",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 2715
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH DRAMA",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2716
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "VISUAL ARTS CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 2717
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MULTIMEDIA CLUB",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2718
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ELDDS (Debate)",
		"cca_generic_name": "DEBATING AND ORATORICAL SOCIETY",
		"_id": 2719
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE CALLIGRAPHY",
		"cca_generic_name": "CHINESE CALLIGRAPHY AND BRUSH PAINTING",
		"_id": 2720
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "GREEN CLUB",
		"_id": 2721
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "IT CLUB",
		"_id": 2722
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 2723
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CHINESE CHESS CLUB",
		"cca_generic_name": "CHESS CLUB - CHINESE",
		"_id": 2724
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MIND GAMES CLUB",
		"cca_generic_name": "WEIQI CLUB",
		"_id": 2725
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NAN CHIAU HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "LIBRARY",
		"_id": 2726
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "INFOCOMM CLUB",
		"cca_generic_name": "BYTE CLUB",
		"_id": 2727
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "AIR RIFLE & AIR PISTOL / SHOOTING",
		"cca_generic_name": "AIR RIFLE / SHOOTING",
		"_id": 2728
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BADMINTON",
		"cca_generic_name": "BADMINTON",
		"_id": 2729
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2730
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "JUDO",
		"_id": 2731
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2732
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SOFTBALL",
		"_id": 2733
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "SAILING",
		"_id": 2734
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 2735
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 2736
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TENNIS",
		"_id": 2737
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 2738
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 2739
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "ARTISTIC GYM/TRAMPOLINE",
		"cca_generic_name": "ARTISTIC GYMNASTICS",
		"_id": 2740
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2741
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2742
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 2743
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2744
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2745
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - STRING",
		"_id": 2746
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUZHENG",
		"_id": 2747
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - MODERN",
		"_id": 2748
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 2749
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "THEATRE CLUB",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2750
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2751
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2752
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "CHINESE SOCIETY",
		"_id": 2753
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "NANYANG DEBATE CLUB",
		"cca_generic_name": "DEBATING AND ORATORICAL SOCIETY",
		"_id": 2754
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "ENGLISH SOCIETY",
		"cca_generic_name": "LDDS - ENGLISH",
		"_id": 2755
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "LION DANCE TROUPE / DRUM ENSEMBLE",
		"cca_generic_name": "LION DANCE TROUPE",
		"_id": 2756
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "NANYANG OUTDOORS CLUB",
		"cca_generic_name": "OUTDOOR ACTIVITIES CLUB",
		"_id": 2757
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "NANYANG GIRLS' HIGH SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MIND SPORTS CLUB",
		"cca_generic_name": "CHESS CLUB - INTERNATIONAL",
		"_id": 2758
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2760
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "HOCKEY",
		"_id": 2762
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2764
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TRACK & FIELD",
		"_id": 2766
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 2768
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ARTISTIC GYMNASTICS",
		"_id": 2770
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "RHYTHMIC GYMNASTICS",
		"_id": 2772
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2773
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2774
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "ST. JOHN BRIGADE",
		"_id": 2776
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE ORCHESTRA",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2778
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2780
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "STRING ORCHESTRA",
		"cca_generic_name": "ENSEMBLE - STRING",
		"_id": 2782
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SYMPHONIC BAND",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 2784
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "DANCE SOCIETY",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 2786
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "CHINESE DRAMA SOCIETY",
		"cca_generic_name": "DRAMA - CHINESE",
		"_id": 2788
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "LDS",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2790
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ART CLUB",
		"cca_generic_name": "ART AND CRAFT CLUB",
		"_id": 2792
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "DEBATE SOCIETY",
		"cca_generic_name": "DEBATING AND ORATORICAL SOCIETY",
		"_id": 2793
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CHINESE CULTURAL SOCIETY",
		"cca_generic_name": "CHINESE CULTURAL SOCIETY",
		"_id": 2795
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "PUBLICATIONS",
		"_id": 2797
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "LIBRARY SOCIETY",
		"cca_generic_name": "LIBRARY",
		"_id": 2799
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "CHIJ ST. NICHOLAS GIRLS' SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MIND GAMES CLUB",
		"cca_generic_name": "MIND SPORTS CLUB",
		"_id": 2801
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2802
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2803
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2804
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TABLE TENNIS",
		"_id": 2805
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "WUSHU",
		"_id": 2806
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRL GUIDES",
		"_id": 2807
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NPCC",
		"_id": 2808
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 2809
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (LAND)",
		"_id": 2810
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ORCHESTRA - CHINESE",
		"_id": 2811
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2812
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - CHINESE",
		"_id": 2813
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - CONCERT",
		"_id": 2814
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "INTERACT CLUB",
		"_id": 2815
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHINESE CALLIGRAPHY SOCIETY",
		"_id": 2816
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CABIN CLUB",
		"cca_generic_name": "CABIN",
		"_id": 2817
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "MEDIA CLUB",
		"_id": 2818
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "JOURNALISM",
		"cca_generic_name": "JOURNALISM BROADCAST",
		"_id": 2819
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2820
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "BASKETBALL (BOYS)",
		"cca_generic_name": "BASKETBALL",
		"_id": 2821
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "NETBALL",
		"_id": 2822
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "FOOTBALL (BOYS)",
		"cca_generic_name": "FOOTBALL",
		"_id": 2823
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "SQUASH (BOYS)",
		"cca_generic_name": "SQUASH",
		"_id": 2824
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "VOLLEYBALL",
		"_id": 2825
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "BOYS' BRIGADE",
		"_id": 2826
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "GIRLS' BRIGADE",
		"_id": 2827
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "RED CROSS YOUTH",
		"cca_generic_name": "SINGAPORE RED CROSS SOCIETY",
		"_id": 2828
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "NCC (LAND) (BOYS)",
		"cca_generic_name": "NCC (LAND)",
		"_id": 2829
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "NCC (SEA)",
		"_id": 2830
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "CHOIR",
		"_id": 2831
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 2832
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BAND - SYMPHONIC",
		"_id": 2833
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DANCE - INTERNATIONAL",
		"_id": 2834
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2835
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "PA CREW",
		"cca_generic_name": "AUDIO & VIDEO/ PA CLUB",
		"_id": 2836
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 2837
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "CHRISTIAN FELLOWSHIP",
		"cca_generic_name": "CHRISTIAN SOCIETY",
		"_id": 2838
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "MEDIA@FAIRFIELD",
		"cca_generic_name": "MEDIA RESOURCE AND IT CLUB",
		"_id": 2839
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BADMINTON",
		"_id": 2840
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "BASKETBALL",
		"_id": 2841
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "ATHLETICS",
		"cca_generic_name": "CROSS COUNTRY",
		"_id": 2842
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FENCING",
		"_id": 2843
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FOOTBALL",
		"_id": 2844
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "TAEKWONDO",
		"_id": 2845
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "PHYSICAL SPORTS",
		"cca_customized_name": "na",
		"cca_generic_name": "FLOORBALL",
		"_id": 2846
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "UNIFORMED GROUPS",
		"cca_customized_name": "na",
		"cca_generic_name": "SCOUTS",
		"_id": 2847
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "GUITAR ENSEMBLE",
		"cca_generic_name": "ENSEMBLE - GUITAR",
		"_id": 2848
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "ENGLISH DRAMA CLUB",
		"cca_generic_name": "DRAMA - ENGLISH",
		"_id": 2849
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "SHOW CHOIR",
		"cca_generic_name": "MUSIC, DRAMA & DANCE CLUB",
		"_id": 2850
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ASTRONOMY CLUB",
		"_id": 2851
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "SINGAPORE YOUTH FLYING CLUB",
		"_id": 2852
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "CLUBS AND SOCIETIES",
		"cca_customized_name": "na",
		"cca_generic_name": "ROBOTICS CLUB",
		"_id": 2853
	}, {
		"_full_count": "1455",
		"school_section": "SECONDARY",
		"school_name": "SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE",
		"rank": 0.0,
		"cca_grouping_desc": "VISUAL AND PERFORMING ARTS",
		"cca_customized_name": "na",
		"cca_generic_name": "MEDIA CLUB",
		"_id": 2854
	}
]"""


#convert from json to dict
x = json.loads(x)

#get data from dict and write to excel database

#open a workbook
wb = xlwt.Workbook()

#open a worksheet
ws = wb.add_sheet('ccaOffered')

#write column headers
headers = ["_full_count", "school_section", "school_name", "rank", "cca_grouping_desc", "cca_customized_name", "cca_generic_name", "_id"]

for i in range(len(headers)):
	ws.write(0, i, headers[i])

#write data
row = 1
#for each row/json item
for item in x:
	#for each column/data
	for i in range(len(headers)):
		header = headers[i]
		ws.write(row, i, item[header])
	row += 1

#save excel workbook
wb.save('ccaOffered.xls')