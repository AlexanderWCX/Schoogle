#commented

#make api call to get json data; https://data.gov.sg/api/action/datastore_search?resource_id=3bb9e6b0-6865-4a55-87ba-cc380bc4df39&limit=3664&q=SECONDARY

#import libraries
import json
import xlwt

#format json data
x = """[
	{
		"_full_count": "3664",
		"_id": 6178,
		"subject_desc": "MUSIC",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6179,
		"subject_desc": "PHYSICS",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3001,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3002,
		"subject_desc": "BIOLOGY",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3003,
		"subject_desc": "CHEMISTRY",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3004,
		"subject_desc": "CHINESE",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3459,
		"subject_desc": "CHINESE",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3005,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3006,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3007,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3008,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3009,
		"subject_desc": "GEOGRAPHY",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3010,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3011,
		"subject_desc": "HIGHER MALAY",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3012,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3013,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3014,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3015,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3016,
		"subject_desc": "HUMANITIES (SS, LIT IN MALAY)",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3017,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3018,
		"subject_desc": "MATHEMATICS",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3019,
		"subject_desc": "MALAY",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3020,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3021,
		"subject_desc": "PHYSICS",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3022,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3023,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3024,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3025,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3026,
		"subject_desc": "SCIENCE",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3027,
		"subject_desc": "TAMIL",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3028,
		"subject_desc": "VISUAL ARTS",
		"school_name": "ANDERSON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3029,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3030,
		"subject_desc": "ART",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3031,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3032,
		"subject_desc": "BIOLOGY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3033,
		"subject_desc": "BASIC MALAY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3034,
		"subject_desc": "BASIC TAMIL",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3035,
		"subject_desc": "CHEMISTRY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3036,
		"subject_desc": "CHINESE",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3037,
		"subject_desc": "CHINESE B",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3038,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3039,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3040,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3041,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3042,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3043,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3044,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3045,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3046,
		"subject_desc": "HISTORY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3047,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3048,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3049,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3050,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3051,
		"subject_desc": "MATHEMATICS",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3052,
		"subject_desc": "MALAY",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3053,
		"subject_desc": "MALAY B",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3054,
		"subject_desc": "MUSIC",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3055,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3056,
		"subject_desc": "PHYSICS",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3057,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3058,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3059,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3060,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3061,
		"subject_desc": "SCIENCE",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3062,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3063,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3064,
		"subject_desc": "TAMIL",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3065,
		"subject_desc": "TAMIL B",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3066,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3067,
		"subject_desc": "ART",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3068,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3069,
		"subject_desc": "BIOLOGY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3070,
		"subject_desc": "BASIC MALAY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3071,
		"subject_desc": "BASIC TAMIL",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3072,
		"subject_desc": "CHEMISTRY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3073,
		"subject_desc": "CHINESE",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3074,
		"subject_desc": "CHINESE B",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3075,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3076,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3077,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3078,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3079,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3080,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3081,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3082,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3083,
		"subject_desc": "HISTORY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3084,
		"subject_desc": "HIGHER MALAY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3085,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3086,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3087,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3088,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3089,
		"subject_desc": "MATHEMATICS",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3090,
		"subject_desc": "MALAY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3091,
		"subject_desc": "MUSIC",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3092,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3093,
		"subject_desc": "PHYSICS",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3094,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3095,
		"subject_desc": "PROJECT WORK",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3096,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3097,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3098,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3099,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3100,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3101,
		"subject_desc": "TAMIL",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3102,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3103,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3104,
		"subject_desc": "BIOLOGY",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3105,
		"subject_desc": "CHINESE (SPECIAL PROGRAMME)",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3106,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3107,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3108,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3109,
		"subject_desc": "CHEMISTRY",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3110,
		"subject_desc": "CHINESE",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3111,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3112,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3113,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3114,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3115,
		"subject_desc": "GEOGRAPHY",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3116,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3117,
		"subject_desc": "HISTORY",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3118,
		"subject_desc": "HIGHER MALAY",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3119,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3120,
		"subject_desc": "LITERATURE(E)",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3121,
		"subject_desc": "MALAY (SPECIAL PROGRAMME)",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3122,
		"subject_desc": "MATHEMATICS",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3123,
		"subject_desc": "MALAY",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3124,
		"subject_desc": "MUSIC",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3125,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3126,
		"subject_desc": "PHYSICS",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3127,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3128,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3129,
		"subject_desc": "TAMIL",
		"school_name": "CEDAR GIRLS' SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3199,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3200,
		"subject_desc": "ART",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3201,
		"subject_desc": "ART NA LEVEL",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3202,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3203,
		"subject_desc": "BASIC CHINESE",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3204,
		"subject_desc": "BIOLOGY",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3205,
		"subject_desc": "BASIC MALAY",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3206,
		"subject_desc": "BASIC TAMIL",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3207,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3208,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3209,
		"subject_desc": "CHEMISTRY",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3210,
		"subject_desc": "CHINESE",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3211,
		"subject_desc": "CHINESE N(A)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3212,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3213,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3214,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3215,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3216,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3217,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3218,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3219,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3220,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3221,
		"subject_desc": "GEOGRAPHY",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3222,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3223,
		"subject_desc": "HISTORY",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3224,
		"subject_desc": "LITERATURE(E)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3225,
		"subject_desc": "MATHEMATICS",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3226,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3227,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3228,
		"subject_desc": "MALAY",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3229,
		"subject_desc": "MALAY N(A)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3230,
		"subject_desc": "MUSIC",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3231,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3232,
		"subject_desc": "PHYSICS",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3233,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3234,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3235,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3236,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3237,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3238,
		"subject_desc": "TAMIL",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3239,
		"subject_desc": "TAMIL N(A)",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3240,
		"subject_desc": "ART",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3241,
		"subject_desc": "BIOLOGY",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3242,
		"subject_desc": "CHEMISTRY",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3243,
		"subject_desc": "CHINESE",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3244,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3245,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3246,
		"subject_desc": "GEOGRAPHY",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3247,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3248,
		"subject_desc": "HISTORY",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3249,
		"subject_desc": "HIGHER MALAY",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3250,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3251,
		"subject_desc": "LITERATURE(E)",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3252,
		"subject_desc": "MALAY",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3253,
		"subject_desc": "MUSIC",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3254,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3255,
		"subject_desc": "PHYSICS",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3256,
		"subject_desc": "TAMIL",
		"school_name": "RAFFLES GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3279,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3280,
		"subject_desc": "ART",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3281,
		"subject_desc": "BIOLOGY",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3282,
		"subject_desc": "CHEMISTRY",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3283,
		"subject_desc": "CHINESE",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3284,
		"subject_desc": "COMPUTING",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3285,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3286,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3287,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3288,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3289,
		"subject_desc": "HISTORY",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3290,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3291,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3292,
		"subject_desc": "MATHEMATICS",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3293,
		"subject_desc": "MALAY",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3294,
		"subject_desc": "PHYSICS",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3295,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3296,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3297,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3298,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3299,
		"subject_desc": "TAMIL",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3300,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3301,
		"subject_desc": "ART",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3302,
		"subject_desc": "ART NA LEVEL",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3303,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3304,
		"subject_desc": "BASIC CHINESE",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3305,
		"subject_desc": "BIOLOGY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3306,
		"subject_desc": "BASIC MALAY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3307,
		"subject_desc": "BASIC TAMIL",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3308,
		"subject_desc": "CHEMISTRY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3309,
		"subject_desc": "CHINESE",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3310,
		"subject_desc": "CHINESE N(A)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3311,
		"subject_desc": "CHINESE B",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3312,
		"subject_desc": "COMPUTING",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3313,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3314,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3315,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3316,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3317,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3318,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3319,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3320,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3321,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3322,
		"subject_desc": "GEOGRAPHY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3323,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3324,
		"subject_desc": "HIGHER MALAY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3325,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3326,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3327,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3328,
		"subject_desc": "LITERATURE(E)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3329,
		"subject_desc": "MATHEMATICS",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3330,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3331,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3332,
		"subject_desc": "MALAY",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3333,
		"subject_desc": "MALAY N(A)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3334,
		"subject_desc": "MALAY B",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3335,
		"subject_desc": "MUSIC",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3336,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3337,
		"subject_desc": "PHYSICS",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3338,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3339,
		"subject_desc": "SCIENCE",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3340,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3341,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3342,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3343,
		"subject_desc": "TAMIL",
		"school_name": "COMMONWEALTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3511,
		"subject_desc": "TAMIL",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3402,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3403,
		"subject_desc": "ART",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3404,
		"subject_desc": "ART NA LEVEL",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3405,
		"subject_desc": "ART NT LEVEL",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3406,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3407,
		"subject_desc": "BASIC CHINESE",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3408,
		"subject_desc": "BIOLOGY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3409,
		"subject_desc": "BASIC MALAY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3410,
		"subject_desc": "BASIC TAMIL",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3411,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3412,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3413,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3414,
		"subject_desc": "CHEMISTRY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3415,
		"subject_desc": "CHINESE",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3416,
		"subject_desc": "CHINESE N(A)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3417,
		"subject_desc": "CHINESE B",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3418,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3419,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3420,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3421,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3422,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3423,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3424,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3425,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3426,
		"subject_desc": "GEOGRAPHY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3427,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3428,
		"subject_desc": "HISTORY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3429,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3430,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3431,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3432,
		"subject_desc": "LITERATURE(E)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3433,
		"subject_desc": "MATHEMATICS",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3434,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3435,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3436,
		"subject_desc": "MALAY",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3437,
		"subject_desc": "MALAY N(A)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3438,
		"subject_desc": "MALAY B",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3439,
		"subject_desc": "MUSIC",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3440,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3441,
		"subject_desc": "PHYSICS",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3442,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3443,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3444,
		"subject_desc": "SCIENCE",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3445,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3446,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3447,
		"subject_desc": "TAMIL",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3448,
		"subject_desc": "TAMIL N(A)",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3449,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3450,
		"subject_desc": "ART",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3451,
		"subject_desc": "BASIC CHINESE",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3452,
		"subject_desc": "BIOLOGY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3453,
		"subject_desc": "BASIC MALAY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3454,
		"subject_desc": "BASIC TAMIL",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3455,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3456,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3457,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3458,
		"subject_desc": "CHEMISTRY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3460,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3461,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3462,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3463,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3464,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3465,
		"subject_desc": "ELECTRONICS",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3466,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3467,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3468,
		"subject_desc": "GEOGRAPHY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3469,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3470,
		"subject_desc": "MATHEMATICS",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3471,
		"subject_desc": "MALAY",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3472,
		"subject_desc": "MUSIC",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3473,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3474,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3475,
		"subject_desc": "PHYSICS",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3476,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3477,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3478,
		"subject_desc": "SCIENCE",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3479,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3480,
		"subject_desc": "SCIENCE",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3481,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3482,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3483,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3484,
		"subject_desc": "TAMIL",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3485,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3486,
		"subject_desc": "ART",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3487,
		"subject_desc": "BIOLOGY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3488,
		"subject_desc": "CHEMISTRY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3489,
		"subject_desc": "CHINESE",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3490,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3491,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3492,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3493,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3494,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3495,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3496,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3497,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3498,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3499,
		"subject_desc": "LITERATURE(E)",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3500,
		"subject_desc": "MATHEMATICS",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3501,
		"subject_desc": "MALAY",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3502,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3503,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3504,
		"subject_desc": "PHYSICS",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3505,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3506,
		"subject_desc": "RETAIL OPERATIONS",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3507,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3508,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3509,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3510,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3512,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3513,
		"subject_desc": "ART",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3514,
		"subject_desc": "ART NA LEVEL",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3515,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3516,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3517,
		"subject_desc": "BIOLOGY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3518,
		"subject_desc": "BASIC MALAY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3519,
		"subject_desc": "BASIC TAMIL",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3520,
		"subject_desc": "CO-CURRICULAR ACTIVITIES",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3521,
		"subject_desc": "CHEMISTRY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3522,
		"subject_desc": "CHINESE",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3523,
		"subject_desc": "CHINESE N(A)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3524,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3525,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3526,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3527,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3528,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3529,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3530,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3531,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3532,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3533,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3534,
		"subject_desc": "HISTORY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3535,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3536,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3537,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3538,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3539,
		"subject_desc": "MATHEMATICS",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3540,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3541,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3542,
		"subject_desc": "MALAY",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3543,
		"subject_desc": "MALAY N(A)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3544,
		"subject_desc": "MUSIC",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3545,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3546,
		"subject_desc": "PHYSICS",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3547,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3548,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3549,
		"subject_desc": "SCIENCE",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3550,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3551,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3552,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3553,
		"subject_desc": "TAMIL",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3554,
		"subject_desc": "TAMIL N(A)",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3555,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3556,
		"subject_desc": "ART",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3557,
		"subject_desc": "BIOLOGY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3558,
		"subject_desc": "CHEMISTRY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3559,
		"subject_desc": "CHINESE",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3560,
		"subject_desc": "CHINESE B",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3561,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3562,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3563,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3564,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3565,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3566,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3567,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3568,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3569,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3570,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3571,
		"subject_desc": "LITERATURE(E)",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3572,
		"subject_desc": "MATHEMATICS",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3573,
		"subject_desc": "MALAY",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3574,
		"subject_desc": "MUSIC",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3575,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3576,
		"subject_desc": "PHYSICS",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3577,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3578,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3579,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3580,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3581,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3582,
		"subject_desc": "TAMIL",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3583,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3584,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3585,
		"subject_desc": "BIOLOGY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3586,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3587,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3588,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3589,
		"subject_desc": "CHEMISTRY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3590,
		"subject_desc": "CHINESE",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3591,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3592,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3593,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3594,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3595,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3596,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3597,
		"subject_desc": "GEOGRAPHY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3598,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3599,
		"subject_desc": "HISTORY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3600,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3601,
		"subject_desc": "MATHEMATICS",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3602,
		"subject_desc": "MALAY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3603,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3604,
		"subject_desc": "PHYSICS",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3605,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3606,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3607,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3608,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3609,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3610,
		"subject_desc": "ART",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3611,
		"subject_desc": "ART NA LEVEL",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3612,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3613,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3614,
		"subject_desc": "BIOLOGY",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3615,
		"subject_desc": "BASIC MALAY",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3616,
		"subject_desc": "CO-CURRICULAR ACTIVITIES",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3617,
		"subject_desc": "CHEMISTRY",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3618,
		"subject_desc": "CHINESE",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3619,
		"subject_desc": "CHINESE N(A)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3620,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3621,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3622,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3623,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3624,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3625,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3626,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3627,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3628,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3629,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3630,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3631,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3632,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3633,
		"subject_desc": "MATHEMATICS",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3634,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3635,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3636,
		"subject_desc": "MALAY",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3637,
		"subject_desc": "MALAY N(A)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3638,
		"subject_desc": "MUSIC",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3639,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3640,
		"subject_desc": "PHYSICS",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3641,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3642,
		"subject_desc": "SCIENCE",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3643,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3644,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3645,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3646,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3647,
		"subject_desc": "ART",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3648,
		"subject_desc": "BASIC CHINESE",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3649,
		"subject_desc": "BIOLOGY",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3650,
		"subject_desc": "BASIC MALAY",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3651,
		"subject_desc": "BASIC TAMIL",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3652,
		"subject_desc": "CHINESE (SPECIAL PROGRAMME)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3653,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3654,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3655,
		"subject_desc": "CHEMISTRY",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3656,
		"subject_desc": "CHINESE",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3657,
		"subject_desc": "CHINESE N(A)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3658,
		"subject_desc": "COMPUTING",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3659,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3660,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3661,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3662,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3663,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3664,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3665,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3666,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3667,
		"subject_desc": "GEOGRAPHY",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3668,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3669,
		"subject_desc": "HISTORY",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3670,
		"subject_desc": "HIGHER MALAY",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3671,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3672,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3673,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3674,
		"subject_desc": "LITERATURE(E)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3675,
		"subject_desc": "MATHEMATICS",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3676,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3677,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3678,
		"subject_desc": "MALAY",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3679,
		"subject_desc": "MALAY N(A)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3680,
		"subject_desc": "MUSIC",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3681,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3682,
		"subject_desc": "PHYSICS",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3683,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3684,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3685,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3686,
		"subject_desc": "TAMIL",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3687,
		"subject_desc": "TAMIL N(A)",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3688,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3689,
		"subject_desc": "ART",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3690,
		"subject_desc": "BIOLOGY",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3691,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3692,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3693,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3694,
		"subject_desc": "CHEMISTRY",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3695,
		"subject_desc": "CHINESE",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3696,
		"subject_desc": "COMPUTING",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3697,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3698,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3699,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3700,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3701,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3702,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3703,
		"subject_desc": "GEOGRAPHY",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3704,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3705,
		"subject_desc": "HISTORY",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3706,
		"subject_desc": "HIGHER MALAY",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3707,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3708,
		"subject_desc": "LITERATURE(E)",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3709,
		"subject_desc": "MATHEMATICS",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3710,
		"subject_desc": "MALAY",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3711,
		"subject_desc": "MUSIC",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3712,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3713,
		"subject_desc": "OECIE ECONOMICS (GCEO)",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3714,
		"subject_desc": "PHYSICS",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3715,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3716,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3717,
		"subject_desc": "TAMIL",
		"school_name": "TEMASEK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3718,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3719,
		"subject_desc": "ART",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3720,
		"subject_desc": "BIOLOGY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3721,
		"subject_desc": "CHEMISTRY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3722,
		"subject_desc": "CHINESE",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3723,
		"subject_desc": "CHINESE B",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3724,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3725,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3726,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3727,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3728,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3729,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3730,
		"subject_desc": "GEOGRAPHY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3731,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3732,
		"subject_desc": "HIGHER MALAY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3733,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3734,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3735,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3736,
		"subject_desc": "LITERATURE(E)",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3737,
		"subject_desc": "MATHEMATICS",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3738,
		"subject_desc": "MALAY",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3739,
		"subject_desc": "MUSIC",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3740,
		"subject_desc": "PHYSICS",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3741,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3742,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3743,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3744,
		"subject_desc": "SCIENCE",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3745,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3746,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3747,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3748,
		"subject_desc": "ART",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3749,
		"subject_desc": "ART NA LEVEL",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3750,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3751,
		"subject_desc": "BIOLOGY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3752,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3753,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3754,
		"subject_desc": "CHEMISTRY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3755,
		"subject_desc": "CHINESE",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3756,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3757,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3758,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3759,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3760,
		"subject_desc": "ELECTRONICS",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3761,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3762,
		"subject_desc": "GEOGRAPHY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3763,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3764,
		"subject_desc": "HISTORY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3765,
		"subject_desc": "LITERATURE(E)",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3766,
		"subject_desc": "MALAY (SPECIAL PROGRAMME)",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3767,
		"subject_desc": "MATHEMATICS",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3768,
		"subject_desc": "MALAY",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3769,
		"subject_desc": "MUSIC",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3770,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3771,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3772,
		"subject_desc": "PHYSICS",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3773,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3774,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3775,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3776,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3777,
		"subject_desc": "ART",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3778,
		"subject_desc": "BIOLOGY",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3779,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3780,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3781,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3782,
		"subject_desc": "CHEMISTRY",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3783,
		"subject_desc": "CHINESE",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3784,
		"subject_desc": "COMPUTING",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3785,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3786,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3787,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3788,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3789,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3790,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3791,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3792,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3793,
		"subject_desc": "HISTORY",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3794,
		"subject_desc": "HIGHER MALAY",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3795,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3796,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3797,
		"subject_desc": "MATHEMATICS",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3798,
		"subject_desc": "MALAY",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3799,
		"subject_desc": "MUSIC",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3800,
		"subject_desc": "PHYSICS",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3801,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3802,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3803,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3804,
		"subject_desc": "TAMIL",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3805,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3806,
		"subject_desc": "ART",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3807,
		"subject_desc": "ART NA LEVEL",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3808,
		"subject_desc": "ART NT LEVEL",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3809,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3810,
		"subject_desc": "BASIC CHINESE",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3811,
		"subject_desc": "BASIC MALAY",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3812,
		"subject_desc": "BASIC TAMIL",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3813,
		"subject_desc": "CHEMISTRY",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3814,
		"subject_desc": "CHINESE",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3815,
		"subject_desc": "CHINESE N(A)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3816,
		"subject_desc": "CHINESE B",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3817,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3818,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3819,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3820,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3821,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3822,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3823,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3824,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3825,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3826,
		"subject_desc": "HIGHER MALAY",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3827,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3828,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3829,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3830,
		"subject_desc": "HUMANITIES (SS, LIT IN CHINESE)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3831,
		"subject_desc": "HUMANITIES (SS, LIT IN MALAY)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3832,
		"subject_desc": "HUMANITIES (SS, LIT IN TAMIL)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3833,
		"subject_desc": "LITERATURE(E)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3834,
		"subject_desc": "MATHEMATICS",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3835,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3836,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3837,
		"subject_desc": "MALAY",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3838,
		"subject_desc": "MALAY N(A)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3839,
		"subject_desc": "MUSIC",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3840,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3841,
		"subject_desc": "PHYSICS",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3842,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3843,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3844,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3845,
		"subject_desc": "SCIENCE",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3846,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3847,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3848,
		"subject_desc": "TAMIL",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3849,
		"subject_desc": "TAMIL N(A)",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3850,
		"subject_desc": "TAMIL B",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3851,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3852,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3853,
		"subject_desc": "BIOLOGY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3854,
		"subject_desc": "BASIC MALAY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3855,
		"subject_desc": "BASIC TAMIL",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3856,
		"subject_desc": "CHEMISTRY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3857,
		"subject_desc": "CHINESE",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3858,
		"subject_desc": "CHINESE N(A)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3859,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3860,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3861,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3862,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3863,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3864,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3865,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3866,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3867,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3868,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3869,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3870,
		"subject_desc": "HISTORY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3871,
		"subject_desc": "HIGHER MALAY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3872,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3873,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3874,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3875,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3876,
		"subject_desc": "MATHEMATICS",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3877,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3878,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3879,
		"subject_desc": "MALAY",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3880,
		"subject_desc": "MALAY N(A)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3881,
		"subject_desc": "MUSIC",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3882,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3883,
		"subject_desc": "PHYSICS",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3884,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3885,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3886,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3887,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3888,
		"subject_desc": "TAMIL",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3889,
		"subject_desc": "TAMIL N(A)",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3890,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3891,
		"subject_desc": "ART",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3892,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3893,
		"subject_desc": "BIOLOGY",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3894,
		"subject_desc": "BASIC MALAY",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3895,
		"subject_desc": "BASIC TAMIL",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3896,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3897,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3898,
		"subject_desc": "CHEMISTRY",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3899,
		"subject_desc": "CHINESE",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3900,
		"subject_desc": "CHINESE N(A)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3901,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3902,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3903,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3904,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3905,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3906,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3907,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3908,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3909,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3910,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3911,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3912,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3913,
		"subject_desc": "MALAY (SPECIAL PROGRAMME)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3914,
		"subject_desc": "MATHEMATICS",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3915,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3916,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3917,
		"subject_desc": "MALAY",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3918,
		"subject_desc": "MALAY N(A)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3919,
		"subject_desc": "MUSIC",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3920,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3921,
		"subject_desc": "PHYSICS",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3922,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3923,
		"subject_desc": "SCIENCE",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3924,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3925,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3926,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3927,
		"subject_desc": "TAMIL",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3928,
		"subject_desc": "TAMIL N(A)",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3929,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3930,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3931,
		"subject_desc": "ART",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3932,
		"subject_desc": "BIOLOGY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3933,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3934,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3935,
		"subject_desc": "CHEMISTRY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3936,
		"subject_desc": "CHINESE",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3937,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3938,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3939,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3940,
		"subject_desc": "GEOGRAPHY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3941,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3942,
		"subject_desc": "HISTORY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3943,
		"subject_desc": "LITERATURE(E)",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3944,
		"subject_desc": "MATHEMATICS",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3945,
		"subject_desc": "MALAY",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3946,
		"subject_desc": "MUSIC",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3947,
		"subject_desc": "PHYSICS",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3948,
		"subject_desc": "SCIENCE",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3949,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3950,
		"subject_desc": "TAMIL",
		"school_name": "YISHUN TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3951,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3952,
		"subject_desc": "ART",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3953,
		"subject_desc": "BIOLOGY",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3954,
		"subject_desc": "CHEMISTRY",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3955,
		"subject_desc": "CHINESE",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3956,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3957,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3958,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3959,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3960,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3961,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3962,
		"subject_desc": "GEOGRAPHY",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3963,
		"subject_desc": "HISTORY",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3964,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3965,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3966,
		"subject_desc": "HUMANITIES (SS, LIT IN MALAY)",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3967,
		"subject_desc": "LITERATURE(E)",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3968,
		"subject_desc": "MATHEMATICS",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3969,
		"subject_desc": "MALAY",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3970,
		"subject_desc": "MUSIC",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3971,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3972,
		"subject_desc": "PHYSICS",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3973,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3974,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3975,
		"subject_desc": "SCIENCE",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3976,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3998,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 3999,
		"subject_desc": "ART NA LEVEL",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4000,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4001,
		"subject_desc": "BASIC CHINESE",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4002,
		"subject_desc": "BIOLOGY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4003,
		"subject_desc": "BASIC MALAY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4004,
		"subject_desc": "CHEMISTRY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4005,
		"subject_desc": "CHINESE",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4006,
		"subject_desc": "CHINESE N(A)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4007,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4008,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4009,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4010,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4011,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4012,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4013,
		"subject_desc": "ELECTRONICS",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4014,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4015,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4016,
		"subject_desc": "HISTORY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4017,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4018,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4019,
		"subject_desc": "LITERATURE(E)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4020,
		"subject_desc": "MATHEMATICS",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4021,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4022,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4023,
		"subject_desc": "MALAY",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4024,
		"subject_desc": "MALAY N(A)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4025,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4026,
		"subject_desc": "PHYSICS",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4027,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4028,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4029,
		"subject_desc": "SCIENCE",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4030,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4031,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4032,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4033,
		"subject_desc": "ART",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4034,
		"subject_desc": "BASIC CHINESE",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4035,
		"subject_desc": "BIOLOGY",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4036,
		"subject_desc": "BASIC MALAY",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4037,
		"subject_desc": "CHEMISTRY",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4038,
		"subject_desc": "CHINESE",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4039,
		"subject_desc": "COMPUTING",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4040,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4041,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4042,
		"subject_desc": "DRAMA",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4043,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4044,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4045,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4046,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4047,
		"subject_desc": "GEOGRAPHY",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4048,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4049,
		"subject_desc": "HISTORY",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4050,
		"subject_desc": "HIGHER MALAY",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4051,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4052,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4053,
		"subject_desc": "HUMANITIES (SS, LIT IN CHINESE)",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4054,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4055,
		"subject_desc": "LITERATURE(E)",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4056,
		"subject_desc": "MATHEMATICS",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4057,
		"subject_desc": "MALAY",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4058,
		"subject_desc": "PHYSICS",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4059,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4060,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4061,
		"subject_desc": "SCIENCE",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4062,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "XINMIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4063,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4064,
		"subject_desc": "BASIC CHINESE",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4065,
		"subject_desc": "BIOLOGY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4066,
		"subject_desc": "BASIC MALAY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4067,
		"subject_desc": "BASIC TAMIL",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4068,
		"subject_desc": "CO-CURRICULAR ACTIVITIES",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4069,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4070,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4071,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4072,
		"subject_desc": "CHEMISTRY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4073,
		"subject_desc": "CHINESE",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4074,
		"subject_desc": "CHINESE N(A)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4075,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4076,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4077,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4078,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4079,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4080,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4081,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4082,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4083,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4084,
		"subject_desc": "GEOGRAPHY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4085,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4086,
		"subject_desc": "HISTORY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4087,
		"subject_desc": "LITERATURE(E)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4088,
		"subject_desc": "MATHEMATICS",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4089,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4090,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4091,
		"subject_desc": "MALAY",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4092,
		"subject_desc": "MALAY N(A)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4093,
		"subject_desc": "MALAY B",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4094,
		"subject_desc": "MUSIC",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4095,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4096,
		"subject_desc": "PHYSICS",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4097,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4098,
		"subject_desc": "PROJECT WORK",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4099,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4100,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4101,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4102,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4103,
		"subject_desc": "TAMIL",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4104,
		"subject_desc": "TAMIL N(A)",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4105,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4106,
		"subject_desc": "ART",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4107,
		"subject_desc": "ART NA LEVEL",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4108,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4109,
		"subject_desc": "BASIC CHINESE",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4110,
		"subject_desc": "BIOLOGY",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4111,
		"subject_desc": "BASIC MALAY",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4112,
		"subject_desc": "CHEMISTRY",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4113,
		"subject_desc": "CHINESE",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4114,
		"subject_desc": "CHINESE N(A)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4115,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4116,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4117,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4118,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4119,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4120,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4121,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4122,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4123,
		"subject_desc": "GEOGRAPHY",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4124,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4125,
		"subject_desc": "HISTORY",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4126,
		"subject_desc": "LITERATURE(E)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4127,
		"subject_desc": "MATHEMATICS",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4128,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4129,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4130,
		"subject_desc": "MALAY",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4131,
		"subject_desc": "MALAY N(A)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4132,
		"subject_desc": "MUSIC",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4133,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4134,
		"subject_desc": "PHYSICS",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4135,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4136,
		"subject_desc": "SCIENCE",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4137,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4138,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4139,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4140,
		"subject_desc": "ART",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4141,
		"subject_desc": "BASIC CHINESE",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4142,
		"subject_desc": "BIOLOGY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4143,
		"subject_desc": "BASIC MALAY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4144,
		"subject_desc": "BASIC TAMIL",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4145,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4146,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4147,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4148,
		"subject_desc": "CHEMISTRY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4149,
		"subject_desc": "CHINESE",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4150,
		"subject_desc": "CHINESE N(A)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4151,
		"subject_desc": "CHINESE B",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4152,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4153,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4154,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4155,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4156,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4157,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4158,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4159,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4160,
		"subject_desc": "GEOGRAPHY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4161,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4162,
		"subject_desc": "HISTORY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4163,
		"subject_desc": "HIGHER MALAY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4164,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4165,
		"subject_desc": "MATHEMATICS",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4166,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4167,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4168,
		"subject_desc": "MALAY",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4169,
		"subject_desc": "MALAY N(A)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4170,
		"subject_desc": "MUSIC",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4171,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4172,
		"subject_desc": "PHYSICS",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4173,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4174,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4175,
		"subject_desc": "SCIENCE",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4176,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4177,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4178,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4179,
		"subject_desc": "TAMIL",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4180,
		"subject_desc": "TAMIL N(A)",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4181,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4182,
		"subject_desc": "ART",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4183,
		"subject_desc": "BASIC CHINESE",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4184,
		"subject_desc": "BIOLOGY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4185,
		"subject_desc": "BASIC MALAY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4186,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4187,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4188,
		"subject_desc": "CHEMISTRY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4189,
		"subject_desc": "CHINESE",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4190,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4191,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4192,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4193,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4194,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4195,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4196,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4197,
		"subject_desc": "GEOGRAPHY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4198,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4199,
		"subject_desc": "HISTORY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4200,
		"subject_desc": "HIGHER MALAY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4201,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4202,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4203,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4204,
		"subject_desc": "LITERATURE(E)",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4205,
		"subject_desc": "MATHEMATICS",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4206,
		"subject_desc": "MALAY",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4207,
		"subject_desc": "MUSIC",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4208,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4209,
		"subject_desc": "PHYSICS",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4210,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4211,
		"subject_desc": "RETAIL OPERATIONS",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4212,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4213,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4214,
		"subject_desc": "ART",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4215,
		"subject_desc": "BIOLOGY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4216,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4217,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4218,
		"subject_desc": "CHEMISTRY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4219,
		"subject_desc": "CHINESE",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4220,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4221,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4222,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4223,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4224,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4225,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4226,
		"subject_desc": "GEOGRAPHY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4227,
		"subject_desc": "HISTORY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4228,
		"subject_desc": "LITERATURE(E)",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4229,
		"subject_desc": "MATHEMATICS",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4230,
		"subject_desc": "MALAY",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4231,
		"subject_desc": "MUSIC",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4232,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4233,
		"subject_desc": "PHYSICS",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4234,
		"subject_desc": "RETAIL OPERATIONS",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4235,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4236,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4237,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4238,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4239,
		"subject_desc": "TAMIL",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4240,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4241,
		"subject_desc": "ART",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4242,
		"subject_desc": "BIOLOGY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4243,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4244,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4245,
		"subject_desc": "CHEMISTRY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4246,
		"subject_desc": "CHINESE",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4247,
		"subject_desc": "CHINESE B",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4248,
		"subject_desc": "COMPUTING",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4249,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4250,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4251,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4252,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4253,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4254,
		"subject_desc": "GEOGRAPHY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4255,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4256,
		"subject_desc": "HISTORY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4257,
		"subject_desc": "LITERATURE(E)",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4258,
		"subject_desc": "MATHEMATICS",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4259,
		"subject_desc": "MALAY",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4260,
		"subject_desc": "MUSIC",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4261,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4262,
		"subject_desc": "PHYSICS",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4263,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4264,
		"subject_desc": "RETAIL OPERATIONS",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4265,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4266,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4267,
		"subject_desc": "SCIENCE",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4268,
		"subject_desc": "TAMIL",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4269,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4270,
		"subject_desc": "ART",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4271,
		"subject_desc": "BASIC CHINESE",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4272,
		"subject_desc": "BIOLOGY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4273,
		"subject_desc": "BASIC MALAY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4274,
		"subject_desc": "BASIC TAMIL",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4275,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4276,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4277,
		"subject_desc": "CHEMISTRY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4278,
		"subject_desc": "CHINESE",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4279,
		"subject_desc": "CHINESE N(A)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4280,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4281,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4282,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4283,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4284,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4285,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4286,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4287,
		"subject_desc": "ELECTRONICS",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4288,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4289,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4290,
		"subject_desc": "GEOGRAPHY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4291,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4292,
		"subject_desc": "HISTORY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4293,
		"subject_desc": "HIGHER MALAY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4294,
		"subject_desc": "LITERATURE(E)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4295,
		"subject_desc": "MATHEMATICS",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4296,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4297,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4298,
		"subject_desc": "MALAY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4299,
		"subject_desc": "MALAY N(A)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4300,
		"subject_desc": "MUSIC",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4301,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4302,
		"subject_desc": "PHYSICS",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4303,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4304,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4305,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4306,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4307,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4308,
		"subject_desc": "TAMIL",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4309,
		"subject_desc": "TAMIL N(A)",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4310,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4311,
		"subject_desc": "ART",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4312,
		"subject_desc": "ART NA LEVEL",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4313,
		"subject_desc": "ART NT LEVEL",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4314,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4315,
		"subject_desc": "BASIC CHINESE",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4316,
		"subject_desc": "BIOLOGY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4317,
		"subject_desc": "BASIC MALAY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4318,
		"subject_desc": "BASIC TAMIL",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4319,
		"subject_desc": "CHEMISTRY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4320,
		"subject_desc": "CHINESE",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4321,
		"subject_desc": "CHINESE N(A)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4322,
		"subject_desc": "CHINESE B",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4323,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4324,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4325,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4326,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4327,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4328,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4329,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4330,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4331,
		"subject_desc": "GEOGRAPHY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4332,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4333,
		"subject_desc": "HISTORY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4334,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4335,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4336,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4337,
		"subject_desc": "LITERATURE(E)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4338,
		"subject_desc": "MATHEMATICS",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4339,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4340,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4341,
		"subject_desc": "MALAY",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4342,
		"subject_desc": "MALAY N(A)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4343,
		"subject_desc": "MALAY B",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4344,
		"subject_desc": "MUSIC",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4345,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4346,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4347,
		"subject_desc": "PHYSICS",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4348,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4349,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4350,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4351,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4352,
		"subject_desc": "SCIENCE",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4353,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4354,
		"subject_desc": "TAMIL",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4355,
		"subject_desc": "TAMIL N(A)",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4356,
		"subject_desc": "TAMIL B",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4357,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4358,
		"subject_desc": "ART",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4359,
		"subject_desc": "ART NA LEVEL",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4360,
		"subject_desc": "ART NT LEVEL",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4361,
		"subject_desc": "BIOLOGY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4362,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4363,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4364,
		"subject_desc": "CHEMISTRY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4365,
		"subject_desc": "CHINESE",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4366,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4367,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4368,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4369,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4370,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4371,
		"subject_desc": "GEOGRAPHY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4372,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4373,
		"subject_desc": "HISTORY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4374,
		"subject_desc": "HIGHER MALAY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4375,
		"subject_desc": "LITERATURE(E)",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4376,
		"subject_desc": "MATHEMATICS",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4377,
		"subject_desc": "MALAY",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4378,
		"subject_desc": "MUSIC",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4379,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4380,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4381,
		"subject_desc": "PHYSICS",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4382,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4383,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4384,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4385,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4386,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4387,
		"subject_desc": "TAMIL",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4388,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4389,
		"subject_desc": "ART",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4390,
		"subject_desc": "ART NA LEVEL",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4391,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4392,
		"subject_desc": "BASIC CHINESE",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4393,
		"subject_desc": "BIOLOGY",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4394,
		"subject_desc": "BASIC MALAY",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4395,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4396,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4397,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4398,
		"subject_desc": "CHEMISTRY",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4399,
		"subject_desc": "CHINESE",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4400,
		"subject_desc": "CHINESE N(A)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4401,
		"subject_desc": "CHINESE B",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4402,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4403,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4404,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4405,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4406,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4407,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4408,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4409,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4410,
		"subject_desc": "GEOGRAPHY",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4411,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4412,
		"subject_desc": "HISTORY",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4413,
		"subject_desc": "LITERATURE(E)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4414,
		"subject_desc": "MATHEMATICS",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4415,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4416,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4417,
		"subject_desc": "MALAY",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4418,
		"subject_desc": "MALAY N(A)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4419,
		"subject_desc": "MALAY B",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4420,
		"subject_desc": "MUSIC",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4421,
		"subject_desc": "PHYSICS",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4422,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4423,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4424,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4425,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4426,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4427,
		"subject_desc": "SCIENCE",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4428,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4429,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4430,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4431,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4432,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4433,
		"subject_desc": "ART",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4434,
		"subject_desc": "BIOLOGY",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4435,
		"subject_desc": "CHEMISTRY",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4436,
		"subject_desc": "CHINESE",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4437,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4438,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4439,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4440,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4441,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4442,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4443,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4444,
		"subject_desc": "GEOGRAPHY",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4445,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4446,
		"subject_desc": "HISTORY",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4447,
		"subject_desc": "HOME ECONOMICS",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4448,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4449,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4450,
		"subject_desc": "LITERATURE(E)",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4451,
		"subject_desc": "MATHEMATICS",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4452,
		"subject_desc": "MALAY",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4453,
		"subject_desc": "MUSIC",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4454,
		"subject_desc": "PHYSICS",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4455,
		"subject_desc": "PROJECT WORK",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4456,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4457,
		"subject_desc": "SCIENCE",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4458,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4459,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4460,
		"subject_desc": "ART",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4461,
		"subject_desc": "BASIC CHINESE",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4462,
		"subject_desc": "BIOLOGY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4463,
		"subject_desc": "BASIC MALAY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4464,
		"subject_desc": "BASIC TAMIL",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4465,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4466,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4467,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4468,
		"subject_desc": "CHEMISTRY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4469,
		"subject_desc": "CHINESE",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4470,
		"subject_desc": "CHINESE N(A)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4471,
		"subject_desc": "COMPUTING",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4472,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4473,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4474,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4475,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4476,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4477,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4478,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4479,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4480,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4481,
		"subject_desc": "GEOGRAPHY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4482,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4483,
		"subject_desc": "HIGHER ART",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4484,
		"subject_desc": "HISTORY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4485,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4486,
		"subject_desc": "LITERATURE(E)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4487,
		"subject_desc": "MATHEMATICS",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4488,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4489,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4490,
		"subject_desc": "MALAY",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4491,
		"subject_desc": "MALAY N(A)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4492,
		"subject_desc": "MUSIC",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4493,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4494,
		"subject_desc": "PHYSICS",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4495,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4496,
		"subject_desc": "PROJECT WORK",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4497,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4498,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4499,
		"subject_desc": "SCIENCE",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4500,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4501,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4502,
		"subject_desc": "TAMIL",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4503,
		"subject_desc": "TAMIL N(A)",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4504,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4505,
		"subject_desc": "ART",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4506,
		"subject_desc": "BIOLOGY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4507,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4508,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4509,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4510,
		"subject_desc": "CHEMISTRY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4511,
		"subject_desc": "CHINESE",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4512,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4513,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4514,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4515,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4516,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4517,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4518,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4519,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4520,
		"subject_desc": "HISTORY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4521,
		"subject_desc": "MATHEMATICS",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4522,
		"subject_desc": "MALAY",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4523,
		"subject_desc": "MUSIC",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4524,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4525,
		"subject_desc": "PHYSICS",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4526,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4527,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4528,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4529,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4530,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4531,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4532,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4533,
		"subject_desc": "BIOLOGY",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4534,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4535,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4536,
		"subject_desc": "CHEMISTRY",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4537,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4538,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4539,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4540,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4541,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4542,
		"subject_desc": "HISTORY",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4543,
		"subject_desc": "HIGHER MALAY",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4544,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4545,
		"subject_desc": "LITERATURE(E)",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4546,
		"subject_desc": "MATHEMATICS",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4547,
		"subject_desc": "MUSIC",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4548,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4549,
		"subject_desc": "PHYSICS",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4550,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4551,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4552,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4553,
		"subject_desc": "TAMIL",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4554,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4555,
		"subject_desc": "ART",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4556,
		"subject_desc": "ART NA LEVEL",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4557,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4558,
		"subject_desc": "BASIC CHINESE",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4559,
		"subject_desc": "BIOLOGY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4560,
		"subject_desc": "BASIC MALAY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4561,
		"subject_desc": "CHEMISTRY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4562,
		"subject_desc": "CHINESE",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4563,
		"subject_desc": "CHINESE N(A)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4564,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4565,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4566,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4567,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4568,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4569,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4570,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4571,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4572,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4573,
		"subject_desc": "GEOGRAPHY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4574,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4575,
		"subject_desc": "HISTORY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4576,
		"subject_desc": "HIGHER MALAY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4577,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4578,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4579,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4580,
		"subject_desc": "LITERATURE(E)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4581,
		"subject_desc": "MATHEMATICS",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4582,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4583,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4584,
		"subject_desc": "MALAY",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4585,
		"subject_desc": "MALAY N(A)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4586,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4587,
		"subject_desc": "PHYSICS",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4588,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4589,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4590,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4591,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4592,
		"subject_desc": "ART",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4593,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4594,
		"subject_desc": "BASIC CHINESE",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4595,
		"subject_desc": "BASIC MALAY",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4596,
		"subject_desc": "CHEMISTRY",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4597,
		"subject_desc": "CHINESE",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4598,
		"subject_desc": "CHINESE N(A)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4599,
		"subject_desc": "COMPUTING",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4600,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4601,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4602,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4603,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4604,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4605,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4606,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4607,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4608,
		"subject_desc": "GEOGRAPHY",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4609,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4610,
		"subject_desc": "HISTORY",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4611,
		"subject_desc": "HIGHER MALAY",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4612,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4613,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4614,
		"subject_desc": "HUMANITIES (SS, LIT IN MALAY)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4615,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4616,
		"subject_desc": "MATHEMATICS",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4617,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4618,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4619,
		"subject_desc": "MALAY",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4620,
		"subject_desc": "MALAY N(A)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4621,
		"subject_desc": "MUSIC",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4622,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4623,
		"subject_desc": "PHYSICS",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4624,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4625,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4626,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4627,
		"subject_desc": "SCIENCE",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4628,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4629,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4630,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4631,
		"subject_desc": "ART",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4632,
		"subject_desc": "BIOLOGY",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4633,
		"subject_desc": "CHEMISTRY",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4634,
		"subject_desc": "CHINESE",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4635,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4636,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4637,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4638,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4639,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4640,
		"subject_desc": "GEOGRAPHY",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4641,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4642,
		"subject_desc": "HISTORY",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4643,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4644,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4645,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4646,
		"subject_desc": "LITERATURE(E)",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4647,
		"subject_desc": "MATHEMATICS",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4648,
		"subject_desc": "MALAY",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4649,
		"subject_desc": "MUSIC",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4650,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4651,
		"subject_desc": "PHYSICS",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4652,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4653,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4654,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4655,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4656,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4657,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4658,
		"subject_desc": "ART",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4659,
		"subject_desc": "BASIC CHINESE",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4660,
		"subject_desc": "BIOLOGY",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4661,
		"subject_desc": "BASIC MALAY",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4662,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4663,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4664,
		"subject_desc": "CHEMISTRY",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4665,
		"subject_desc": "CHINESE",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4666,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4667,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4668,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4669,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4670,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4671,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4672,
		"subject_desc": "GEOGRAPHY",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4673,
		"subject_desc": "HISTORY",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4674,
		"subject_desc": "LITERATURE(E)",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4675,
		"subject_desc": "MATHEMATICS",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4676,
		"subject_desc": "MALAY",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4677,
		"subject_desc": "MUSIC",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4678,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4679,
		"subject_desc": "PHYSICS",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4680,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4681,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4682,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4683,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4684,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4685,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4686,
		"subject_desc": "ART",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4687,
		"subject_desc": "BIOLOGY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4688,
		"subject_desc": "BIOLOGY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4689,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4690,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4691,
		"subject_desc": "CHEMISTRY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4692,
		"subject_desc": "CHEMISTRY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4693,
		"subject_desc": "CHINESE",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4694,
		"subject_desc": "CHINESE N(A)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4695,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4696,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4697,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4698,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4699,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4700,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4701,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4702,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4703,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4704,
		"subject_desc": "GEOGRAPHY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4705,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4706,
		"subject_desc": "HISTORY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4707,
		"subject_desc": "LITERATURE(E)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4708,
		"subject_desc": "MATHEMATICS",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4709,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4710,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4711,
		"subject_desc": "MALAY",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4712,
		"subject_desc": "MALAY N(A)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4713,
		"subject_desc": "MUSIC",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4714,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4715,
		"subject_desc": "PHYSICAL SCIENCE",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4716,
		"subject_desc": "PHYSICS",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4717,
		"subject_desc": "PHYSICS",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4718,
		"subject_desc": "PROJECT WORK",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4719,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4720,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4721,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4722,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4723,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4724,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4725,
		"subject_desc": "ART",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4726,
		"subject_desc": "BIOLOGY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4727,
		"subject_desc": "CHEMISTRY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4728,
		"subject_desc": "CHINESE",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4729,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4730,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4731,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4732,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4733,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4734,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4735,
		"subject_desc": "GEOGRAPHY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4736,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4737,
		"subject_desc": "HISTORY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4738,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4739,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4740,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4741,
		"subject_desc": "LITERATURE(E)",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4742,
		"subject_desc": "MATHEMATICS",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4743,
		"subject_desc": "MALAY",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4744,
		"subject_desc": "MUSIC",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4745,
		"subject_desc": "PHYSICS",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4746,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4747,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4748,
		"subject_desc": "SCIENCE",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4749,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4750,
		"subject_desc": "ART",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4751,
		"subject_desc": "ART NA LEVEL",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4752,
		"subject_desc": "ART NT LEVEL",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4753,
		"subject_desc": "BASIC CHINESE",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4754,
		"subject_desc": "BIOLOGY",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4755,
		"subject_desc": "CHEMISTRY",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4756,
		"subject_desc": "CHINESE",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4757,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4758,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4759,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4760,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4761,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4762,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4763,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4764,
		"subject_desc": "GEOGRAPHY",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4765,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4766,
		"subject_desc": "HISTORY",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4767,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4768,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4769,
		"subject_desc": "LITERATURE(E)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4770,
		"subject_desc": "MATHEMATICS",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4771,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4772,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4773,
		"subject_desc": "MALAY",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4774,
		"subject_desc": "MALAY N(A)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4775,
		"subject_desc": "MALAY B",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4776,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4777,
		"subject_desc": "PHYSICS",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4778,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4779,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4780,
		"subject_desc": "SCIENCE",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4781,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4782,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4783,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4784,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4785,
		"subject_desc": "TAMIL",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4786,
		"subject_desc": "TAMIL N(A)",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4898,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4899,
		"subject_desc": "ART",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4900,
		"subject_desc": "BIOLOGY",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4901,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4902,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4903,
		"subject_desc": "CHEMISTRY",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4904,
		"subject_desc": "CHINESE",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4905,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4906,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4907,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4908,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4909,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4910,
		"subject_desc": "GEOGRAPHY",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4911,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4912,
		"subject_desc": "HISTORY",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4913,
		"subject_desc": "LITERATURE(E)",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4914,
		"subject_desc": "MATHEMATICS",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4915,
		"subject_desc": "MALAY",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4916,
		"subject_desc": "MUSIC",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4917,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4918,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4919,
		"subject_desc": "PHYSICS",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4920,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4921,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4922,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4923,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4924,
		"subject_desc": "TAMIL",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4925,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4926,
		"subject_desc": "ART",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4927,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4928,
		"subject_desc": "BIOLOGY",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4929,
		"subject_desc": "BASIC MALAY",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4930,
		"subject_desc": "BASIC TAMIL",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4931,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4932,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4933,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4934,
		"subject_desc": "CHEMISTRY",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4935,
		"subject_desc": "CHINESE",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4936,
		"subject_desc": "CHINESE N(A)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4937,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4938,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4939,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4940,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4941,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4942,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4943,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4944,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4945,
		"subject_desc": "HISTORY",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4946,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4947,
		"subject_desc": "MATHEMATICS",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4948,
		"subject_desc": "MALAY",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4949,
		"subject_desc": "MALAY N(A)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4950,
		"subject_desc": "MUSIC",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4951,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4952,
		"subject_desc": "PHYSICS",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4953,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4954,
		"subject_desc": "PROJECT WORK",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4955,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4956,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4957,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4958,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4959,
		"subject_desc": "TAMIL",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4960,
		"subject_desc": "TAMIL N(A)",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4961,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4962,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4963,
		"subject_desc": "BIOLOGY",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4964,
		"subject_desc": "BASIC MALAY",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4965,
		"subject_desc": "BASIC TAMIL",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4966,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4967,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4968,
		"subject_desc": "COMBINED HUMANITIES (SS,LC)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4969,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4970,
		"subject_desc": "CHEMISTRY",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4971,
		"subject_desc": "CHINESE",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4972,
		"subject_desc": "CHINESE N(A)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4973,
		"subject_desc": "CHINESE B",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4974,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4975,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4976,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4977,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4978,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4979,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4980,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4981,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4982,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4983,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4984,
		"subject_desc": "HISTORY",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4985,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4986,
		"subject_desc": "MATHEMATICS",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4987,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4988,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4989,
		"subject_desc": "MALAY",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4990,
		"subject_desc": "MALAY N(A)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4991,
		"subject_desc": "MUSIC",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4992,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4993,
		"subject_desc": "PHYSICS",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4994,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4995,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4996,
		"subject_desc": "SCIENCE",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4997,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4998,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 4999,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5000,
		"subject_desc": "TAMIL",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5001,
		"subject_desc": "TAMIL N(A)",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5046,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5047,
		"subject_desc": "ART",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5048,
		"subject_desc": "BASIC CHINESE",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5049,
		"subject_desc": "BIOLOGY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5050,
		"subject_desc": "BASIC MALAY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5051,
		"subject_desc": "BASIC TAMIL",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5052,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5053,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5054,
		"subject_desc": "CHEMISTRY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5055,
		"subject_desc": "CHINESE",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5056,
		"subject_desc": "CHINESE N(A)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5057,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5058,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5059,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5060,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5061,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5062,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5063,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5064,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5065,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5066,
		"subject_desc": "HIGHER MALAY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5067,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5068,
		"subject_desc": "LITERATURE(E)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5069,
		"subject_desc": "MATHEMATICS",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5070,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5071,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5072,
		"subject_desc": "MALAY",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5073,
		"subject_desc": "MALAY N(A)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5074,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5075,
		"subject_desc": "PHYSICS",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5076,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5077,
		"subject_desc": "SCIENCE",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5078,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5079,
		"subject_desc": "TAMIL",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5080,
		"subject_desc": "TAMIL N(A)",
		"school_name": "DUNMAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5081,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5082,
		"subject_desc": "ART",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5083,
		"subject_desc": "ART NA LEVEL",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5084,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5085,
		"subject_desc": "BASIC CHINESE",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5086,
		"subject_desc": "BIOLOGY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5087,
		"subject_desc": "BIOLOGY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5088,
		"subject_desc": "BASIC MALAY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5089,
		"subject_desc": "BASIC TAMIL",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5090,
		"subject_desc": "CHEMISTRY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5091,
		"subject_desc": "CHEMISTRY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5092,
		"subject_desc": "CHINESE",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5093,
		"subject_desc": "CHINESE N(A)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5094,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5095,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5096,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5097,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5098,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5099,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5100,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5101,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5102,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5103,
		"subject_desc": "GEOGRAPHY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5104,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5105,
		"subject_desc": "HISTORY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5106,
		"subject_desc": "HIGHER MALAY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5107,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5108,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5109,
		"subject_desc": "HUMANITIES (SS, LIT IN CHINESE)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5110,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5111,
		"subject_desc": "LITERATURE IN CHINESE",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5112,
		"subject_desc": "LITERATURE(E)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5113,
		"subject_desc": "MATHEMATICS",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5114,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5115,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5116,
		"subject_desc": "MALAY",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5117,
		"subject_desc": "MALAY N(A)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5118,
		"subject_desc": "MUSIC",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5119,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5120,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5121,
		"subject_desc": "PHYSICS",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5122,
		"subject_desc": "PHYSICS",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5123,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5124,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5125,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5126,
		"subject_desc": "SCIENCE",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5127,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5128,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5129,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5130,
		"subject_desc": "TAMIL",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5131,
		"subject_desc": "TAMIL N(A)",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5132,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5133,
		"subject_desc": "ART",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5134,
		"subject_desc": "BIOLOGY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5135,
		"subject_desc": "CHEMISTRY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5136,
		"subject_desc": "CHINESE",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5137,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5138,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5139,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5140,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5141,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5142,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5143,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5144,
		"subject_desc": "MATHEMATICS",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5145,
		"subject_desc": "MALAY",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5146,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5147,
		"subject_desc": "PHYSICS",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5148,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5149,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5150,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5151,
		"subject_desc": "TAMIL",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5152,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5153,
		"subject_desc": "ART",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5154,
		"subject_desc": "ART NA LEVEL",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5155,
		"subject_desc": "ART NT LEVEL",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5156,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5157,
		"subject_desc": "BASIC CHINESE",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5158,
		"subject_desc": "BIOLOGY",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5159,
		"subject_desc": "BASIC MALAY",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5160,
		"subject_desc": "BASIC TAMIL",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5161,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5162,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5163,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5164,
		"subject_desc": "CHEMISTRY",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5165,
		"subject_desc": "CHINESE",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5166,
		"subject_desc": "CHINESE N(A)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5167,
		"subject_desc": "CHINESE B",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5168,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5169,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5170,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5171,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5172,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5173,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5174,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5175,
		"subject_desc": "LITERATURE(E)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5176,
		"subject_desc": "MATHEMATICS",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5177,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5178,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5179,
		"subject_desc": "MALAY",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5180,
		"subject_desc": "MALAY N(A)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5181,
		"subject_desc": "OECIE BUSINESS STUDIES",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5182,
		"subject_desc": "PHYSICS",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5183,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5184,
		"subject_desc": "RETAIL OPERATIONS",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5185,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5186,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5187,
		"subject_desc": "SCIENCE",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5188,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5189,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5190,
		"subject_desc": "TAMIL",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5191,
		"subject_desc": "TAMIL N(A)",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5192,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5193,
		"subject_desc": "ART NA LEVEL",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5194,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5195,
		"subject_desc": "BIOLOGY",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5196,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5197,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5198,
		"subject_desc": "CHEMISTRY",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5199,
		"subject_desc": "CHINESE",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5200,
		"subject_desc": "CHINESE N(A)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5201,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5202,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5203,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5204,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5205,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5206,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5207,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5208,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5209,
		"subject_desc": "GEOGRAPHY",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5210,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5211,
		"subject_desc": "HISTORY",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5212,
		"subject_desc": "LITERATURE(E)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5213,
		"subject_desc": "MATHEMATICS",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5214,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5215,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5216,
		"subject_desc": "MALAY",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5217,
		"subject_desc": "MALAY N(A)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5218,
		"subject_desc": "MUSIC",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5219,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5220,
		"subject_desc": "PHYSICS",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5221,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5222,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5223,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5224,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5225,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5226,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5227,
		"subject_desc": "TAMIL",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5228,
		"subject_desc": "TAMIL N(A)",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5229,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5230,
		"subject_desc": "ART NA LEVEL",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5231,
		"subject_desc": "ART NT LEVEL",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5232,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5233,
		"subject_desc": "BIOLOGY",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5234,
		"subject_desc": "CHEMISTRY",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5235,
		"subject_desc": "CHINESE",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5236,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5237,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5238,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5334,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5239,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5240,
		"subject_desc": "GEOGRAPHY",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5241,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5242,
		"subject_desc": "HISTORY",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5243,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5244,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5245,
		"subject_desc": "LITERATURE(E)",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5246,
		"subject_desc": "MATHEMATICS",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5247,
		"subject_desc": "MALAY",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5248,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5249,
		"subject_desc": "PHYSICS",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5250,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5251,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5252,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5253,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5254,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5255,
		"subject_desc": "TAMIL",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5256,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5257,
		"subject_desc": "ART",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5258,
		"subject_desc": "BASIC CHINESE",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5259,
		"subject_desc": "BIOLOGY",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5260,
		"subject_desc": "BASIC MALAY",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5261,
		"subject_desc": "BASIC TAMIL",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5262,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5263,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5264,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5265,
		"subject_desc": "CHEMISTRY",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5266,
		"subject_desc": "CHINESE",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5267,
		"subject_desc": "CHINESE B",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5268,
		"subject_desc": "COMPUTING",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5269,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5270,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5271,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5272,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5273,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5274,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5275,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5276,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5277,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5278,
		"subject_desc": "HISTORY",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5279,
		"subject_desc": "HIGHER MALAY",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5280,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5281,
		"subject_desc": "MATHEMATICS",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5282,
		"subject_desc": "MALAY",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5283,
		"subject_desc": "PHYSICS",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5284,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5285,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5286,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5287,
		"subject_desc": "SCIENCE",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5288,
		"subject_desc": "TAMIL",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5289,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5290,
		"subject_desc": "ART",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5291,
		"subject_desc": "ART NA LEVEL",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5292,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5293,
		"subject_desc": "BIOLOGY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5294,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5295,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5296,
		"subject_desc": "CHEMISTRY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5297,
		"subject_desc": "CHINESE",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5298,
		"subject_desc": "CHINESE B",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5299,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5300,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5301,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5302,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5303,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5304,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5305,
		"subject_desc": "GEOGRAPHY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5306,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5307,
		"subject_desc": "HISTORY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5308,
		"subject_desc": "HIGHER MALAY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5309,
		"subject_desc": "LITERATURE(E)",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5310,
		"subject_desc": "MATHEMATICS",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5311,
		"subject_desc": "MALAY",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5312,
		"subject_desc": "MUSIC",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5313,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5314,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5315,
		"subject_desc": "PHYSICS",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5316,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5317,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5318,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5319,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5320,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5321,
		"subject_desc": "TAMIL",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5322,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5323,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5324,
		"subject_desc": "ART",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5325,
		"subject_desc": "ART NA LEVEL",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5326,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5327,
		"subject_desc": "BIOLOGY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5328,
		"subject_desc": "CHEMISTRY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5329,
		"subject_desc": "CHINESE",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5330,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5331,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5332,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5333,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5335,
		"subject_desc": "GEOGRAPHY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5336,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5337,
		"subject_desc": "HISTORY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5338,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5339,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5340,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5341,
		"subject_desc": "LITERATURE(E)",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5342,
		"subject_desc": "MATHEMATICS",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5343,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5344,
		"subject_desc": "MALAY",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5345,
		"subject_desc": "PHYSICS",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5346,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5347,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5348,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5349,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5350,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5351,
		"subject_desc": "ART",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5352,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5353,
		"subject_desc": "BASIC CHINESE",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5354,
		"subject_desc": "BIOLOGY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5355,
		"subject_desc": "BASIC MALAY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5356,
		"subject_desc": "BASIC TAMIL",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5357,
		"subject_desc": "CHEMISTRY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5358,
		"subject_desc": "CHINESE",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5359,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5360,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5361,
		"subject_desc": "DRAMA",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5362,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5363,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5364,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5365,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5366,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5367,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5368,
		"subject_desc": "GEOGRAPHY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5369,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5370,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5371,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5372,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5373,
		"subject_desc": "MATHEMATICS",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5374,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5375,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5376,
		"subject_desc": "MALAY",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5377,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5378,
		"subject_desc": "PHYSICS",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5379,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5380,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5381,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5382,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5383,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5384,
		"subject_desc": "TAMIL",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5385,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5386,
		"subject_desc": "ART",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5387,
		"subject_desc": "CHEMISTRY",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5388,
		"subject_desc": "CHINESE",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5389,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5390,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5391,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5392,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5393,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5394,
		"subject_desc": "GEOGRAPHY",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5395,
		"subject_desc": "HISTORY",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5396,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5397,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5398,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5399,
		"subject_desc": "MATHEMATICS",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5400,
		"subject_desc": "MALAY",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5401,
		"subject_desc": "MUSIC",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5402,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5403,
		"subject_desc": "PHYSICS",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5404,
		"subject_desc": "RETAIL OPERATIONS",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5405,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5406,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5407,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5408,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5409,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5410,
		"subject_desc": "TAMIL",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5411,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5412,
		"subject_desc": "ART",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5413,
		"subject_desc": "ART NA LEVEL",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5414,
		"subject_desc": "BASIC CHINESE",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5415,
		"subject_desc": "BASIC MALAY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5416,
		"subject_desc": "CHEMISTRY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5417,
		"subject_desc": "CHINESE",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5418,
		"subject_desc": "CHINESE N(A)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5419,
		"subject_desc": "CHINESE B",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5420,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5421,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5422,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5423,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5424,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5425,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5426,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5427,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5428,
		"subject_desc": "GEOGRAPHY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5429,
		"subject_desc": "HISTORY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5430,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5431,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5432,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5433,
		"subject_desc": "LITERATURE(E)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5434,
		"subject_desc": "MATHEMATICS",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5435,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5436,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5437,
		"subject_desc": "MALAY",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5438,
		"subject_desc": "MALAY N(A)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5439,
		"subject_desc": "MUSIC",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5440,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5441,
		"subject_desc": "PHYSICS",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5442,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5443,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5444,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5445,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5446,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5447,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5448,
		"subject_desc": "ART",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5449,
		"subject_desc": "BIOLOGY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5450,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5451,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5452,
		"subject_desc": "CHEMISTRY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5453,
		"subject_desc": "CHINESE",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5454,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5455,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5456,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5457,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5458,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5459,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5460,
		"subject_desc": "GEOGRAPHY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5461,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5462,
		"subject_desc": "HISTORY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5463,
		"subject_desc": "HIGHER MALAY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5464,
		"subject_desc": "LITERATURE(E)",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5465,
		"subject_desc": "MATHEMATICS",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5466,
		"subject_desc": "MALAY",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5467,
		"subject_desc": "MUSIC",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5468,
		"subject_desc": "PHYSICS",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5469,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5470,
		"subject_desc": "PROJECT WORK",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5471,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5472,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5473,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5474,
		"subject_desc": "ART",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5475,
		"subject_desc": "BASIC CHINESE",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5476,
		"subject_desc": "BIOLOGY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5477,
		"subject_desc": "BASIC MALAY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5478,
		"subject_desc": "BASIC TAMIL",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5479,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5480,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5481,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5482,
		"subject_desc": "CHEMISTRY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5483,
		"subject_desc": "CHINESE",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5484,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5485,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5486,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5487,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5488,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5489,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5490,
		"subject_desc": "GEOGRAPHY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5491,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5492,
		"subject_desc": "HISTORY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5493,
		"subject_desc": "LITERATURE(E)",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5494,
		"subject_desc": "MATHEMATICS",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5495,
		"subject_desc": "MALAY",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5496,
		"subject_desc": "MUSIC",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5497,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5498,
		"subject_desc": "PHYSICS",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5499,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5500,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5501,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5502,
		"subject_desc": "SCIENCE",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5503,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5504,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5505,
		"subject_desc": "TAMIL",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5506,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5507,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5508,
		"subject_desc": "ART",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5509,
		"subject_desc": "ART NA LEVEL",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5510,
		"subject_desc": "BIOLOGY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5511,
		"subject_desc": "CHEMISTRY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5512,
		"subject_desc": "CHINESE",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5513,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5514,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5515,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5516,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5517,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5518,
		"subject_desc": "GEOGRAPHY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5519,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5520,
		"subject_desc": "HISTORY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5521,
		"subject_desc": "HIGHER MALAY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5522,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5523,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5524,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5525,
		"subject_desc": "LITERATURE(E)",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5526,
		"subject_desc": "LITERATURE IN TAMIL",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5527,
		"subject_desc": "MATHEMATICS",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5528,
		"subject_desc": "MALAY",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5529,
		"subject_desc": "MUSIC",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5530,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5531,
		"subject_desc": "PHYSICS",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5532,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5533,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5534,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5535,
		"subject_desc": "TAMIL",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5536,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5537,
		"subject_desc": "ART",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5538,
		"subject_desc": "ART NA LEVEL",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5539,
		"subject_desc": "ART NT LEVEL",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5540,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5541,
		"subject_desc": "ART FOR AEP",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5542,
		"subject_desc": "BIOLOGY",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5543,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5544,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5545,
		"subject_desc": "CHEMISTRY",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5546,
		"subject_desc": "CHINESE",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5547,
		"subject_desc": "COMPUTING",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5548,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5549,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5550,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5551,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5552,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5553,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5554,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5555,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5556,
		"subject_desc": "GEOGRAPHY",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5557,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5558,
		"subject_desc": "HISTORY",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5559,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5560,
		"subject_desc": "MALAY (SPECIAL PROGRAMME)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5561,
		"subject_desc": "MATHEMATICS",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5562,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5563,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5564,
		"subject_desc": "MALAY",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5565,
		"subject_desc": "MALAY N(A)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5566,
		"subject_desc": "MUSIC",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5567,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5568,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5569,
		"subject_desc": "PHYSICS",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5570,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5571,
		"subject_desc": "SCIENCE",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5572,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5573,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5574,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "ZHONGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5575,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5576,
		"subject_desc": "ART",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5577,
		"subject_desc": "BASIC CHINESE",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5578,
		"subject_desc": "BIOLOGY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5579,
		"subject_desc": "BASIC MALAY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5580,
		"subject_desc": "BASIC TAMIL",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5581,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5582,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5583,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5584,
		"subject_desc": "CHEMISTRY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5585,
		"subject_desc": "CHINESE",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5586,
		"subject_desc": "CHINESE N(A)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5587,
		"subject_desc": "CHINESE B",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5588,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5589,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5590,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5591,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5592,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5593,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5594,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5595,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5596,
		"subject_desc": "GEOGRAPHY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5597,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5598,
		"subject_desc": "HISTORY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5599,
		"subject_desc": "HIGHER MALAY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5600,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5601,
		"subject_desc": "LITERATURE(E)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5602,
		"subject_desc": "MATHEMATICS",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5603,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5604,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5605,
		"subject_desc": "MALAY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5606,
		"subject_desc": "MALAY N(A)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5607,
		"subject_desc": "MALAY B",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5608,
		"subject_desc": "MUSIC",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5609,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5610,
		"subject_desc": "PHYSICS",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5611,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5612,
		"subject_desc": "PROJECT WORK",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5613,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5614,
		"subject_desc": "SCIENCE",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5615,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5616,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5617,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5618,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5619,
		"subject_desc": "TAMIL",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5620,
		"subject_desc": "TAMIL N(A)",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5621,
		"subject_desc": "TAMIL B",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5622,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5623,
		"subject_desc": "ART",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5624,
		"subject_desc": "BIOLOGY",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5625,
		"subject_desc": "CHEMISTRY",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5626,
		"subject_desc": "CHINESE",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5627,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5628,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5629,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5630,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5631,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5632,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5633,
		"subject_desc": "GEOGRAPHY",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5634,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5635,
		"subject_desc": "HISTORY",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5636,
		"subject_desc": "HIGHER MALAY",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5637,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5638,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5639,
		"subject_desc": "LITERATURE(E)",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5640,
		"subject_desc": "MATHEMATICS",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5641,
		"subject_desc": "MALAY",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5642,
		"subject_desc": "MUSIC",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5643,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5644,
		"subject_desc": "PHYSICS",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5645,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5646,
		"subject_desc": "SCIENCE",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5647,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5648,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5649,
		"subject_desc": "TAMIL",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5650,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5651,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5652,
		"subject_desc": "ART",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5653,
		"subject_desc": "BIOLOGY",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5654,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5655,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5656,
		"subject_desc": "CHEMISTRY",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5657,
		"subject_desc": "CHINESE",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5658,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5659,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5660,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5661,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5662,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5663,
		"subject_desc": "LITERATURE(E)",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5664,
		"subject_desc": "MATHEMATICS",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5665,
		"subject_desc": "MALAY",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5666,
		"subject_desc": "PHYSICS",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5667,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5668,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5669,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5670,
		"subject_desc": "TAMIL",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5751,
		"subject_desc": "GEOGRAPHY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5671,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5672,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5673,
		"subject_desc": "ART",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5674,
		"subject_desc": "ART NA LEVEL",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5675,
		"subject_desc": "ART NT LEVEL",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5676,
		"subject_desc": "BASIC CHINESE",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5677,
		"subject_desc": "BIOLOGY",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5678,
		"subject_desc": "BASIC MALAY",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5679,
		"subject_desc": "BASIC TAMIL",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5680,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5681,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5682,
		"subject_desc": "CHEMISTRY",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5683,
		"subject_desc": "CHINESE",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5684,
		"subject_desc": "CHINESE N(A)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5685,
		"subject_desc": "CHINESE B",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5686,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5687,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5688,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5689,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5690,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5691,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5692,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5693,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5694,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5695,
		"subject_desc": "LITERATURE(E)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5696,
		"subject_desc": "MATHEMATICS",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5697,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5698,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5699,
		"subject_desc": "MALAY",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5700,
		"subject_desc": "MALAY N(A)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5701,
		"subject_desc": "MUSIC",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5702,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5703,
		"subject_desc": "PHYSICS",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5704,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5705,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5706,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5707,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5708,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5709,
		"subject_desc": "TAMIL",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5710,
		"subject_desc": "TAMIL N(A)",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5711,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5712,
		"subject_desc": "ART",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5713,
		"subject_desc": "BASIC CHINESE",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5714,
		"subject_desc": "BIOLOGY",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5715,
		"subject_desc": "BASIC MALAY",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5716,
		"subject_desc": "CHEMISTRY",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5717,
		"subject_desc": "CHINESE",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5718,
		"subject_desc": "CHINESE N(A)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5719,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5720,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5721,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5722,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5723,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5724,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5725,
		"subject_desc": "GEOGRAPHY",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5726,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5727,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5728,
		"subject_desc": "LITERATURE(E)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5729,
		"subject_desc": "MATHEMATICS",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5730,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5731,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5732,
		"subject_desc": "MALAY",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5733,
		"subject_desc": "MALAY N(A)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5734,
		"subject_desc": "PHYSICS",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5735,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5736,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5737,
		"subject_desc": "SCIENCE",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5738,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5739,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5740,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5741,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5742,
		"subject_desc": "ART",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5743,
		"subject_desc": "BIOLOGY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5744,
		"subject_desc": "CHEMISTRY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5745,
		"subject_desc": "CHINESE",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5746,
		"subject_desc": "CHINESE B",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5747,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5748,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5749,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5750,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5752,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5753,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5754,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5755,
		"subject_desc": "MATHEMATICS",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5756,
		"subject_desc": "MALAY",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5757,
		"subject_desc": "MUSIC",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5758,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5759,
		"subject_desc": "PHYSICS",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5760,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5761,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5762,
		"subject_desc": "TAMIL",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5763,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5764,
		"subject_desc": "ART",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5765,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5766,
		"subject_desc": "BASIC CHINESE",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5767,
		"subject_desc": "BIOLOGY",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5768,
		"subject_desc": "BASIC MALAY",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5769,
		"subject_desc": "BASIC TAMIL",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5770,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5771,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5772,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5773,
		"subject_desc": "CHEMISTRY",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5774,
		"subject_desc": "CHINESE",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5775,
		"subject_desc": "CHINESE N(A)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5776,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5777,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5778,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5779,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5780,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5781,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5782,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5783,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5784,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5785,
		"subject_desc": "GEOGRAPHY",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5786,
		"subject_desc": "HISTORY",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5787,
		"subject_desc": "LITERATURE(E)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5788,
		"subject_desc": "MATHEMATICS",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5789,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5790,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5791,
		"subject_desc": "MALAY",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5792,
		"subject_desc": "MALAY N(A)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5793,
		"subject_desc": "PHYSICS",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5794,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5795,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5796,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5797,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5798,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5799,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5800,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5801,
		"subject_desc": "TAMIL",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5802,
		"subject_desc": "TAMIL N(A)",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5803,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5804,
		"subject_desc": "ART",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5805,
		"subject_desc": "CHEMISTRY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5806,
		"subject_desc": "CHINESE",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5807,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5808,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5809,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5810,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5811,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5812,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5813,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5814,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5815,
		"subject_desc": "MATHEMATICS",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5816,
		"subject_desc": "MALAY",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5817,
		"subject_desc": "MUSIC",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5818,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5819,
		"subject_desc": "PHYSICS",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5820,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5821,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5822,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5823,
		"subject_desc": "TAMIL",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5824,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5825,
		"subject_desc": "ART",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5826,
		"subject_desc": "CHEMISTRY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5827,
		"subject_desc": "CHINESE",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5828,
		"subject_desc": "CHINESE B",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5829,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5830,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5831,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5832,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5833,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5834,
		"subject_desc": "ELECTRONICS",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5835,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5836,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5837,
		"subject_desc": "GEOGRAPHY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5838,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5839,
		"subject_desc": "HISTORY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5840,
		"subject_desc": "HOME ECONOMICS",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5841,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5842,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5843,
		"subject_desc": "LITERATURE(E)",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5844,
		"subject_desc": "MATHEMATICS",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5845,
		"subject_desc": "MALAY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5846,
		"subject_desc": "MALAY B",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5847,
		"subject_desc": "MUSIC",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5848,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5849,
		"subject_desc": "PHYSICS",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5850,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5851,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5852,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5853,
		"subject_desc": "SCIENCE",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5854,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5855,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5856,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5857,
		"subject_desc": "TAMIL",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5858,
		"subject_desc": "TAMIL B",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5859,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5860,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5861,
		"subject_desc": "BIOLOGY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5862,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5863,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5864,
		"subject_desc": "CHEMISTRY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5865,
		"subject_desc": "CHINESE",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5866,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5867,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5868,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5869,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5870,
		"subject_desc": "GEOGRAPHY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5871,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5872,
		"subject_desc": "HISTORY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5873,
		"subject_desc": "HIGHER MALAY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5874,
		"subject_desc": "LITERATURE(E)",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5875,
		"subject_desc": "MATHEMATICS",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5876,
		"subject_desc": "MALAY",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5877,
		"subject_desc": "PHYSICS",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5878,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "TANJONG KATONG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5879,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5880,
		"subject_desc": "ART",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5881,
		"subject_desc": "ART NA LEVEL",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5882,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5883,
		"subject_desc": "BASIC CHINESE",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5884,
		"subject_desc": "BIOLOGY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5885,
		"subject_desc": "BASIC MALAY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5886,
		"subject_desc": "CHEMISTRY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5887,
		"subject_desc": "CHINESE",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5888,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5889,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5890,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5891,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5892,
		"subject_desc": "ELECTRONICS",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5893,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5894,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5895,
		"subject_desc": "GEOGRAPHY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5896,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5897,
		"subject_desc": "HISTORY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5898,
		"subject_desc": "HIGHER MALAY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5899,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5900,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5901,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5902,
		"subject_desc": "LITERATURE(E)",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5903,
		"subject_desc": "MATHEMATICS",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5904,
		"subject_desc": "MALAY",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5905,
		"subject_desc": "MUSIC",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5906,
		"subject_desc": "PHYSICS",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5907,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5908,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5909,
		"subject_desc": "SCIENCE",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5910,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5911,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5912,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5913,
		"subject_desc": "ART",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5914,
		"subject_desc": "BIOLOGY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5915,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5916,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5917,
		"subject_desc": "CHEMISTRY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5918,
		"subject_desc": "CHINESE",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5919,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5920,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5921,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5922,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5923,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5924,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5925,
		"subject_desc": "HIGHER MALAY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5926,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5927,
		"subject_desc": "MATHEMATICS",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5928,
		"subject_desc": "MALAY",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5929,
		"subject_desc": "PHYSICS",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5930,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5931,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5932,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5933,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5934,
		"subject_desc": "ART",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5935,
		"subject_desc": "BIOLOGY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5936,
		"subject_desc": "CHEMISTRY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5937,
		"subject_desc": "CHINESE",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5938,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5939,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5988,
		"subject_desc": "ART",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5940,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5941,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5942,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5943,
		"subject_desc": "GEOGRAPHY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5944,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5945,
		"subject_desc": "HISTORY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5946,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5947,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5948,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5949,
		"subject_desc": "LITERATURE(E)",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5950,
		"subject_desc": "MATHEMATICS",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5951,
		"subject_desc": "MALAY",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5952,
		"subject_desc": "MUSIC",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5953,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5954,
		"subject_desc": "PHYSICS",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5955,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5956,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5957,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5958,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5959,
		"subject_desc": "TAMIL",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5960,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5961,
		"subject_desc": "ART NA LEVEL",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5962,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5963,
		"subject_desc": "BIOLOGY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5964,
		"subject_desc": "CHEMISTRY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5965,
		"subject_desc": "CHINESE",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5966,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5967,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5968,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5969,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5970,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5971,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5972,
		"subject_desc": "GEOGRAPHY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5973,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5974,
		"subject_desc": "HISTORY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5975,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5976,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5977,
		"subject_desc": "LITERATURE(E)",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5978,
		"subject_desc": "MATHEMATICS",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5979,
		"subject_desc": "MALAY",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5980,
		"subject_desc": "MUSIC",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5981,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5982,
		"subject_desc": "PHYSICS",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5983,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5984,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5985,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5986,
		"subject_desc": "TAMIL",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5987,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5989,
		"subject_desc": "BIOLOGY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5990,
		"subject_desc": "CHEMISTRY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5991,
		"subject_desc": "CHINESE",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5992,
		"subject_desc": "COMPUTING",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5993,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5994,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5995,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5996,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5997,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5998,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 5999,
		"subject_desc": "GEOGRAPHY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6000,
		"subject_desc": "HISTORY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6001,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6002,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6003,
		"subject_desc": "LITERATURE(E)",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6004,
		"subject_desc": "MATHEMATICS",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6005,
		"subject_desc": "MALAY",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6006,
		"subject_desc": "MUSIC",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6007,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6008,
		"subject_desc": "PHYSICS",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6009,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6010,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6011,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6012,
		"subject_desc": "SCIENCE",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6013,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6014,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6015,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6016,
		"subject_desc": "ART",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6017,
		"subject_desc": "BIOLOGY",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6018,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6019,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6020,
		"subject_desc": "CHEMISTRY",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6021,
		"subject_desc": "CHINESE",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6022,
		"subject_desc": "CHINESE B",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6023,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6024,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6025,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6026,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6027,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6028,
		"subject_desc": "GEOGRAPHY",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6029,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6030,
		"subject_desc": "HIGHER MALAY",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6031,
		"subject_desc": "LITERATURE(E)",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6032,
		"subject_desc": "MATHEMATICS",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6033,
		"subject_desc": "MALAY",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6034,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6035,
		"subject_desc": "PHYSICS",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6036,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6037,
		"subject_desc": "TAMIL",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6038,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6039,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6040,
		"subject_desc": "ART",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6041,
		"subject_desc": "BIOLOGY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6042,
		"subject_desc": "BIOLOGY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6043,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6044,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6045,
		"subject_desc": "CHEMISTRY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6046,
		"subject_desc": "CHEMISTRY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6047,
		"subject_desc": "CHINESE",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6048,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6049,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6050,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6051,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6052,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6053,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6054,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6055,
		"subject_desc": "GEOGRAPHY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6056,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6057,
		"subject_desc": "HISTORY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6058,
		"subject_desc": "HIGHER MALAY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6059,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6060,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6061,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6062,
		"subject_desc": "LITERATURE(E)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6063,
		"subject_desc": "MATHEMATICS",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6064,
		"subject_desc": "MALAY",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6065,
		"subject_desc": "MUSIC",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6066,
		"subject_desc": "PHYSICS",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6067,
		"subject_desc": "PHYSICS",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6068,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6069,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6070,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6071,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6072,
		"subject_desc": "SCIENCE",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6073,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6074,
		"subject_desc": "TAMIL",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6075,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6076,
		"subject_desc": "ART NA LEVEL",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6077,
		"subject_desc": "ART NT LEVEL",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6078,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6079,
		"subject_desc": "BASIC CHINESE",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6080,
		"subject_desc": "BIOLOGY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6081,
		"subject_desc": "BASIC MALAY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6082,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6083,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6084,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6085,
		"subject_desc": "CHEMISTRY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6086,
		"subject_desc": "CHINESE",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6087,
		"subject_desc": "CHINESE N(A)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6177,
		"subject_desc": "MALAY",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6088,
		"subject_desc": "CHINESE B",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6089,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6090,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6091,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6092,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6093,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6094,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6095,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6096,
		"subject_desc": "MATHEMATICS",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6097,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6098,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6099,
		"subject_desc": "MALAY",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6100,
		"subject_desc": "MALAY N(A)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6101,
		"subject_desc": "PHYSICS",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6102,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6103,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6104,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6105,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6106,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6107,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6108,
		"subject_desc": "ART",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6109,
		"subject_desc": "ART NA LEVEL",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6110,
		"subject_desc": "ART NT LEVEL",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6111,
		"subject_desc": "BASIC CHINESE",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6112,
		"subject_desc": "BIOLOGY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6113,
		"subject_desc": "BIOLOGY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6114,
		"subject_desc": "BASIC MALAY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6115,
		"subject_desc": "BASIC TAMIL",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6116,
		"subject_desc": "CHEMISTRY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6117,
		"subject_desc": "CHEMISTRY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6118,
		"subject_desc": "CHINESE",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6119,
		"subject_desc": "CHINESE N(A)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6120,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6121,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6122,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6123,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6124,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6125,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6126,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6127,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6128,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6129,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6130,
		"subject_desc": "GEOGRAPHY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6131,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6132,
		"subject_desc": "HISTORY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6133,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6134,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6135,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6136,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6137,
		"subject_desc": "LITERATURE(E)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6138,
		"subject_desc": "MATHEMATICS",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6139,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6140,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6141,
		"subject_desc": "MALAY",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6142,
		"subject_desc": "MALAY N(A)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6143,
		"subject_desc": "MUSIC",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6144,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6145,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6146,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6147,
		"subject_desc": "PHYSICS",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6148,
		"subject_desc": "PHYSICS",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6149,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6150,
		"subject_desc": "SCIENCE",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6151,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6152,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6153,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6154,
		"subject_desc": "TAMIL",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6155,
		"subject_desc": "TAMIL N(A)",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6156,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6157,
		"subject_desc": "ART",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6158,
		"subject_desc": "ART NA LEVEL",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6159,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6160,
		"subject_desc": "BIOLOGY",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6161,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6162,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6163,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6164,
		"subject_desc": "CHEMISTRY",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6165,
		"subject_desc": "CHINESE",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6166,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6167,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6168,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6169,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6170,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6171,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6172,
		"subject_desc": "GEOGRAPHY",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6173,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6174,
		"subject_desc": "HISTORY",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6175,
		"subject_desc": "LITERATURE(E)",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6176,
		"subject_desc": "MATHEMATICS",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6180,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6181,
		"subject_desc": "SCIENCE",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6182,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6183,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6184,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6185,
		"subject_desc": "ART",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6186,
		"subject_desc": "ART NA LEVEL",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6187,
		"subject_desc": "ART NT LEVEL",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6188,
		"subject_desc": "BASIC CHINESE",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6189,
		"subject_desc": "BASIC MALAY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6190,
		"subject_desc": "BASIC TAMIL",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6191,
		"subject_desc": "CHEMISTRY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6192,
		"subject_desc": "CHINESE",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6193,
		"subject_desc": "CHINESE N(A)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6194,
		"subject_desc": "CHINESE B",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6195,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6196,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6197,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6198,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6199,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6200,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6201,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6202,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6203,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6204,
		"subject_desc": "GEOGRAPHY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6205,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6206,
		"subject_desc": "HISTORY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6207,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6208,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6209,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6210,
		"subject_desc": "LITERATURE(E)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6211,
		"subject_desc": "MATHEMATICS",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6212,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6213,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6214,
		"subject_desc": "MALAY",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6215,
		"subject_desc": "MALAY N(A)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6216,
		"subject_desc": "MALAY B",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6217,
		"subject_desc": "MUSIC",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6218,
		"subject_desc": "MUSIC NT LEVEL",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6219,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6220,
		"subject_desc": "PHYSICS",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6221,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6222,
		"subject_desc": "RETAIL OPERATIONS",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6223,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6224,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6225,
		"subject_desc": "SCIENCE",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6226,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6227,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6228,
		"subject_desc": "TAMIL",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6229,
		"subject_desc": "TAMIL N(A)",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6230,
		"subject_desc": "TAMIL B",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6231,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6232,
		"subject_desc": "ART",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6233,
		"subject_desc": "BASIC CHINESE",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6234,
		"subject_desc": "BIOLOGY",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6235,
		"subject_desc": "BASIC MALAY",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6236,
		"subject_desc": "CHEMISTRY",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6237,
		"subject_desc": "CHINESE",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6238,
		"subject_desc": "CHINESE B",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6239,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6240,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6241,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6242,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6243,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6244,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6245,
		"subject_desc": "GEOGRAPHY",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6246,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6247,
		"subject_desc": "HISTORY",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6248,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6249,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6250,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6251,
		"subject_desc": "LITERATURE(E)",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6252,
		"subject_desc": "MATHEMATICS",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6253,
		"subject_desc": "MALAY",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6254,
		"subject_desc": "MUSIC",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6255,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6256,
		"subject_desc": "PHYSICS",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6257,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6258,
		"subject_desc": "SCIENCE",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6259,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6260,
		"subject_desc": "PROJECT WORK",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6261,
		"subject_desc": "ICT",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6262,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6263,
		"subject_desc": "ART NA LEVEL",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6264,
		"subject_desc": "ART NT LEVEL",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6265,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6266,
		"subject_desc": "BASIC CHINESE",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6267,
		"subject_desc": "BIOLOGY",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6268,
		"subject_desc": "BASIC MALAY",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6269,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6270,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6271,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6272,
		"subject_desc": "CHEMISTRY",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6273,
		"subject_desc": "CHINESE",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6274,
		"subject_desc": "CHINESE N(A)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6275,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6276,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6277,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6278,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6279,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6280,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6281,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6282,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6283,
		"subject_desc": "GEOGRAPHY",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6284,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6285,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6286,
		"subject_desc": "MATHEMATICS",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6287,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6288,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6289,
		"subject_desc": "MALAY",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6290,
		"subject_desc": "MALAY N(A)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6291,
		"subject_desc": "MUSIC",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6292,
		"subject_desc": "PHYSICS",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6293,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6294,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6295,
		"subject_desc": "SCIENCE",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6296,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6297,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6298,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6299,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6300,
		"subject_desc": "ART",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6301,
		"subject_desc": "BIOLOGY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6302,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6303,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6304,
		"subject_desc": "CHEMISTRY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6305,
		"subject_desc": "CHINESE",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6306,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6307,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6308,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6309,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6310,
		"subject_desc": "GEOGRAPHY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6311,
		"subject_desc": "HISTORY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6312,
		"subject_desc": "LITERATURE(E)",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6313,
		"subject_desc": "MATHEMATICS",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6314,
		"subject_desc": "MALAY",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6315,
		"subject_desc": "MUSIC",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6316,
		"subject_desc": "PHYSICS",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6317,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6318,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6319,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6320,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6321,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6322,
		"subject_desc": "ART",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6323,
		"subject_desc": "BASIC CHINESE",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6324,
		"subject_desc": "BIOLOGY",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6325,
		"subject_desc": "BASIC MALAY",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6326,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6327,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6328,
		"subject_desc": "CHEMISTRY",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6329,
		"subject_desc": "CHINESE",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6330,
		"subject_desc": "CHINESE N(A)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6331,
		"subject_desc": "CHINESE B",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6332,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6333,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6334,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6335,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6336,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6337,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6338,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6339,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6340,
		"subject_desc": "GEOGRAPHY",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6341,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6342,
		"subject_desc": "HISTORY",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6343,
		"subject_desc": "HOME ECONOMICS",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6344,
		"subject_desc": "LITERATURE(E)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6345,
		"subject_desc": "MATHEMATICS",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6346,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6347,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6348,
		"subject_desc": "MALAY",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6349,
		"subject_desc": "MALAY N(A)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6350,
		"subject_desc": "MALAY B",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6351,
		"subject_desc": "MUSIC",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6352,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6353,
		"subject_desc": "PHYSICS",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6354,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6355,
		"subject_desc": "PROJECT WORK",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6356,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6357,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6358,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6359,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6360,
		"subject_desc": "ART",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6361,
		"subject_desc": "ART NA LEVEL",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6362,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6363,
		"subject_desc": "BASIC CHINESE",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6364,
		"subject_desc": "BIOLOGY",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6365,
		"subject_desc": "BASIC MALAY",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6366,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6367,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6368,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6369,
		"subject_desc": "CHEMISTRY",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6370,
		"subject_desc": "CHINESE",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6371,
		"subject_desc": "CHINESE N(A)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6372,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6373,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6374,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6375,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6376,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6377,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6378,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6379,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6380,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6381,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6382,
		"subject_desc": "GEOGRAPHY",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6383,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6384,
		"subject_desc": "HISTORY",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6385,
		"subject_desc": "LITERATURE(E)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6386,
		"subject_desc": "MATHEMATICS",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6387,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6388,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6389,
		"subject_desc": "MALAY",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6390,
		"subject_desc": "MALAY N(A)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6391,
		"subject_desc": "OECIE ECONOMICS (GCEO)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6392,
		"subject_desc": "PHYSICS",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6393,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6394,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6395,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6396,
		"subject_desc": "SCIENCE",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6397,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6398,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6399,
		"subject_desc": "ART",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6400,
		"subject_desc": "ART NA LEVEL",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6401,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6402,
		"subject_desc": "BASIC CHINESE",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6403,
		"subject_desc": "BIOLOGY",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6404,
		"subject_desc": "BASIC MALAY",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6405,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6406,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6407,
		"subject_desc": "CHEMISTRY",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6408,
		"subject_desc": "CHINESE",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6409,
		"subject_desc": "CHINESE N(A)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6410,
		"subject_desc": "CHINESE B",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6411,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6412,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6413,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6414,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6415,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6416,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6417,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6418,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6419,
		"subject_desc": "MATHEMATICS",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6420,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6421,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6422,
		"subject_desc": "MALAY",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6423,
		"subject_desc": "MALAY N(A)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6424,
		"subject_desc": "PHYSICS",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6425,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6426,
		"subject_desc": "SCIENCE",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6427,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6428,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6429,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6430,
		"subject_desc": "ART",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6431,
		"subject_desc": "BIOLOGY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6432,
		"subject_desc": "CHEMISTRY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6433,
		"subject_desc": "CHINESE",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6434,
		"subject_desc": "CHINESE B",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6435,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6436,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6437,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6438,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6439,
		"subject_desc": "ELECTRONICS",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6440,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6441,
		"subject_desc": "GEOGRAPHY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6442,
		"subject_desc": "HISTORY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6443,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6444,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6445,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6446,
		"subject_desc": "MATHEMATICS",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6447,
		"subject_desc": "MALAY",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6448,
		"subject_desc": "PHYSICS",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6449,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6450,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6451,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6452,
		"subject_desc": "ART",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6453,
		"subject_desc": "BIOLOGY",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6454,
		"subject_desc": "CHEMISTRY",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6455,
		"subject_desc": "CHINESE",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6456,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6457,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6458,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6459,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6460,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6461,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6462,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6463,
		"subject_desc": "GEOGRAPHY",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6464,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6465,
		"subject_desc": "HISTORY",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6466,
		"subject_desc": "HIGHER MALAY",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6467,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6468,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6469,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6470,
		"subject_desc": "LITERATURE(E)",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6471,
		"subject_desc": "MATHEMATICS",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6472,
		"subject_desc": "MALAY",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6473,
		"subject_desc": "MUSIC",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6474,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6475,
		"subject_desc": "PHYSICS",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6476,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6477,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6478,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6479,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 6480,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7243,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7244,
		"subject_desc": "ART NA LEVEL",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7245,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7246,
		"subject_desc": "ART FOR AEP",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7247,
		"subject_desc": "BASIC CHINESE",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7248,
		"subject_desc": "BIOLOGY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7249,
		"subject_desc": "BASIC MALAY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7250,
		"subject_desc": "BASIC TAMIL",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7251,
		"subject_desc": "CHEMISTRY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7252,
		"subject_desc": "CHINESE",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7253,
		"subject_desc": "CHINESE N(A)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7254,
		"subject_desc": "CHINESE B",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7255,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7256,
		"subject_desc": "DRAMA",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7257,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7258,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7259,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7260,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7261,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7262,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7263,
		"subject_desc": "GEOGRAPHY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7264,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7265,
		"subject_desc": "HIGHER ART",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7266,
		"subject_desc": "HISTORY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7267,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7268,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7269,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7270,
		"subject_desc": "LITERATURE(E)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7271,
		"subject_desc": "MATHEMATICS",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7272,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7273,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7274,
		"subject_desc": "MALAY",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7275,
		"subject_desc": "MALAY N(A)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7276,
		"subject_desc": "MALAY B",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7277,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7278,
		"subject_desc": "OECIE DRAMA (GCEO)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7279,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7280,
		"subject_desc": "PHYSICS",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7281,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7282,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7283,
		"subject_desc": "SCIENCE",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7284,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7285,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7286,
		"subject_desc": "TAMIL",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7287,
		"subject_desc": "TAMIL N(A)",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7288,
		"subject_desc": "TAMIL B",
		"school_name": "CHIJ SECONDARY (TOA PAYOH)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7289,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7290,
		"subject_desc": "ART",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7291,
		"subject_desc": "BIOLOGY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7292,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7293,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7294,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7295,
		"subject_desc": "CHEMISTRY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7296,
		"subject_desc": "CHINESE",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7297,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7298,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7299,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7300,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7301,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7302,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7303,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7304,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7305,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7306,
		"subject_desc": "GEOGRAPHY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7307,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7308,
		"subject_desc": "HISTORY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7309,
		"subject_desc": "LITERATURE(E)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7310,
		"subject_desc": "MATHEMATICS",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7311,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7312,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7313,
		"subject_desc": "MALAY",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7314,
		"subject_desc": "PHYSICS",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7315,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7316,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7317,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7352,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7353,
		"subject_desc": "ART",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7354,
		"subject_desc": "BIOLOGY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7355,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7356,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7357,
		"subject_desc": "CHEMISTRY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7358,
		"subject_desc": "CHINESE",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7359,
		"subject_desc": "COMPUTING",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7360,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7361,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7362,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7363,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7364,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7365,
		"subject_desc": "GEOGRAPHY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7366,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7367,
		"subject_desc": "HISTORY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7368,
		"subject_desc": "LITERATURE(E)",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7369,
		"subject_desc": "MATHEMATICS",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7370,
		"subject_desc": "MALAY",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7371,
		"subject_desc": "MUSIC",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7372,
		"subject_desc": "PHYSICS",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7373,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7374,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7375,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7376,
		"subject_desc": "TAMIL",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7406,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7407,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7408,
		"subject_desc": "ART",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7409,
		"subject_desc": "BIOLOGY",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7410,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7411,
		"subject_desc": "CHEMISTRY",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7412,
		"subject_desc": "CHINESE",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7413,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7414,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7415,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7416,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7417,
		"subject_desc": "ELECTRONICS",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7418,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7419,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7420,
		"subject_desc": "HISTORY",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7421,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7422,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7423,
		"subject_desc": "MATHEMATICS",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7424,
		"subject_desc": "MALAY",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7425,
		"subject_desc": "MUSIC",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7426,
		"subject_desc": "PHYSICS",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7427,
		"subject_desc": "MOBILE ROBOTICS",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7428,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7429,
		"subject_desc": "TAMIL",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7430,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7431,
		"subject_desc": "ART",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7432,
		"subject_desc": "BASIC CHINESE",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7433,
		"subject_desc": "BIOLOGY",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7434,
		"subject_desc": "BASIC MALAY",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7435,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7436,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7437,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7438,
		"subject_desc": "CHEMISTRY",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7439,
		"subject_desc": "CHINESE",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7440,
		"subject_desc": "CHINESE N(A)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7441,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7442,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7443,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7444,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7445,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7446,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7447,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7448,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7449,
		"subject_desc": "GEOGRAPHY",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7450,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7451,
		"subject_desc": "MATHEMATICS",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7452,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7453,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7454,
		"subject_desc": "MALAY",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7455,
		"subject_desc": "MALAY N(A)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7456,
		"subject_desc": "MUSIC",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7457,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7458,
		"subject_desc": "PHYSICS",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7459,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7460,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7461,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7462,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7463,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7464,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7465,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7466,
		"subject_desc": "ART",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7467,
		"subject_desc": "BASIC CHINESE",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7468,
		"subject_desc": "BIOLOGY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7469,
		"subject_desc": "BASIC MALAY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7470,
		"subject_desc": "BASIC TAMIL",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7471,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7472,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7473,
		"subject_desc": "CHEMISTRY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7474,
		"subject_desc": "CHINESE",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7475,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7476,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7477,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7478,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7479,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7480,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7481,
		"subject_desc": "MATHEMATICS",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7482,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7483,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7484,
		"subject_desc": "MALAY",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7485,
		"subject_desc": "MUSIC",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7486,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7487,
		"subject_desc": "PHYSICS",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7488,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7489,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7490,
		"subject_desc": "SCIENCE",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7491,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7492,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7493,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7494,
		"subject_desc": "TAMIL",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7551,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7552,
		"subject_desc": "ART",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7553,
		"subject_desc": "BIOLOGY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7554,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7555,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7556,
		"subject_desc": "CHEMISTRY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7557,
		"subject_desc": "CHINESE",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7558,
		"subject_desc": "DRAMA",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7559,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7560,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7561,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7562,
		"subject_desc": "GEOGRAPHY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7563,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7564,
		"subject_desc": "HIGHER MUSIC",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7565,
		"subject_desc": "HISTORY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7566,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7567,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7568,
		"subject_desc": "MATHEMATICS",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7569,
		"subject_desc": "MALAY",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7570,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7571,
		"subject_desc": "PHYSICS",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7572,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7573,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7574,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7575,
		"subject_desc": "TAMIL",
		"school_name": "ST. MARGARET'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7659,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7660,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7661,
		"subject_desc": "ART",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7662,
		"subject_desc": "BASIC CHINESE",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7663,
		"subject_desc": "BIOLOGY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7664,
		"subject_desc": "BASIC MALAY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7665,
		"subject_desc": "BASIC TAMIL",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7666,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7667,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7668,
		"subject_desc": "CHEMISTRY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7669,
		"subject_desc": "CHINESE",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7670,
		"subject_desc": "CHINESE B",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7671,
		"subject_desc": "CIVICS & MORAL EDUCATION",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7672,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7673,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7674,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7675,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7676,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7677,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7678,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7679,
		"subject_desc": "HOME ECONOMICS",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7680,
		"subject_desc": "LITERATURE(E)",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7681,
		"subject_desc": "MATHEMATICS",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7682,
		"subject_desc": "MALAY",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7683,
		"subject_desc": "MALAY B",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7684,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7685,
		"subject_desc": "PHYSICS",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7686,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7687,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7688,
		"subject_desc": "TAMIL",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7689,
		"subject_desc": "TAMIL B",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7690,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7691,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7692,
		"subject_desc": "BIOLOGY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7693,
		"subject_desc": "CHEMISTRY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7694,
		"subject_desc": "CHINESE",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7695,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7696,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7697,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7698,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7699,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7700,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7701,
		"subject_desc": "FOOD STUDIES, N LEVEL",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7702,
		"subject_desc": "GEOGRAPHY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7703,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7704,
		"subject_desc": "HIGHER MUSIC",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7705,
		"subject_desc": "HISTORY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7706,
		"subject_desc": "HIGHER MALAY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7707,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7708,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7709,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7710,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7711,
		"subject_desc": "LITERATURE(E)",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7712,
		"subject_desc": "MATHEMATICS",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7713,
		"subject_desc": "MALAY",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7714,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7715,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7716,
		"subject_desc": "PHYSICS",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7717,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7718,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7719,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7720,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7721,
		"subject_desc": "TAMIL",
		"school_name": "PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7722,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7723,
		"subject_desc": "ART",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7724,
		"subject_desc": "BIOLOGY",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7725,
		"subject_desc": "CHEMISTRY",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7726,
		"subject_desc": "CHINESE",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7727,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7728,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7729,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7730,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7731,
		"subject_desc": "EXERCISE AND SPORTS SCIENCE",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7732,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7733,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7734,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7735,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7736,
		"subject_desc": "MATHEMATICS",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7737,
		"subject_desc": "MALAY",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7738,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7739,
		"subject_desc": "PHYSICS",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7740,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7741,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7742,
		"subject_desc": "SCIENCE (PHY, BIO)",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7743,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7744,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7745,
		"subject_desc": "ART",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7746,
		"subject_desc": "BIOLOGY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7747,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7748,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7749,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7750,
		"subject_desc": "CHEMISTRY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7751,
		"subject_desc": "CHINESE",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7752,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7753,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7754,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7755,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7756,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7757,
		"subject_desc": "LITERATURE(E)",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7758,
		"subject_desc": "MATHEMATICS",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7759,
		"subject_desc": "MALAY",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7760,
		"subject_desc": "MUSIC",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7761,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7762,
		"subject_desc": "PHYSICS",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7763,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7764,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7765,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7766,
		"subject_desc": "TAMIL",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7767,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7768,
		"subject_desc": "PRINCIPLES OF A/C",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7769,
		"subject_desc": "ART",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7770,
		"subject_desc": "BIOLOGY",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7771,
		"subject_desc": "COMBINED HUMANITIES (S,G)",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7772,
		"subject_desc": "COMBINED HUMANITIES (S,H)",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7773,
		"subject_desc": "COMBINED HUMANITIES (S,L)",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7774,
		"subject_desc": "CHEMISTRY",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7775,
		"subject_desc": "CHINESE",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7776,
		"subject_desc": "CHINESE B",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7777,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7778,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7779,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7780,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7781,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7782,
		"subject_desc": "GEOGRAPHY",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7783,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7784,
		"subject_desc": "HISTORY",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7785,
		"subject_desc": "LITERATURE(E)",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7786,
		"subject_desc": "MATHEMATICS",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7787,
		"subject_desc": "MALAY",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7788,
		"subject_desc": "PHYSICS",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7789,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7790,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7791,
		"subject_desc": "SCIENCE",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7792,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7793,
		"subject_desc": "TAMIL",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7794,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7795,
		"subject_desc": "ART",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7796,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7797,
		"subject_desc": "BIOLOGY",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7798,
		"subject_desc": "CHEMISTRY",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7799,
		"subject_desc": "CHINESE",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7800,
		"subject_desc": "CHINESE B",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7801,
		"subject_desc": "COMPUTER STUDIES",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7802,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7803,
		"subject_desc": "GEOGRAPHY",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7804,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7805,
		"subject_desc": "HIGHER ART",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7806,
		"subject_desc": "HIGHER MUSIC",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7807,
		"subject_desc": "HISTORY",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7808,
		"subject_desc": "HIGHER MALAY",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7809,
		"subject_desc": "HOME ECONOMICS",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7810,
		"subject_desc": "HIGHER TAMIL",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7811,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7812,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7813,
		"subject_desc": "HUMANITIES (SS, LIT IN ENGLISH)",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7814,
		"subject_desc": "LITERATURE(E)",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7815,
		"subject_desc": "MATHEMATICS",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7816,
		"subject_desc": "MALAY",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7817,
		"subject_desc": "MUSIC",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7818,
		"subject_desc": "MUSIC 'O' LEVEL",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7819,
		"subject_desc": "MUSIC (MEP)",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7820,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7821,
		"subject_desc": "PHYSICS",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7822,
		"subject_desc": "PROJECT WORK",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 7823,
		"subject_desc": "TAMIL",
		"school_name": "METHODIST GIRLS' SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8176,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8177,
		"subject_desc": "ART",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8178,
		"subject_desc": "BIOLOGY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8179,
		"subject_desc": "CHEMISTRY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8180,
		"subject_desc": "CHINESE",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8181,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8182,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8183,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8184,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8185,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8186,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8187,
		"subject_desc": "GEOGRAPHY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8188,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8189,
		"subject_desc": "HISTORY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8190,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8191,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8192,
		"subject_desc": "LITERATURE(E)",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8193,
		"subject_desc": "MATHEMATICS",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8194,
		"subject_desc": "MALAY",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8195,
		"subject_desc": "MUSIC",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8196,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8197,
		"subject_desc": "PHYSICS",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8198,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8199,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8200,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8225,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8226,
		"subject_desc": "ART",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8227,
		"subject_desc": "ART NA LEVEL",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8228,
		"subject_desc": "ART 'O' LEVEL",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8229,
		"subject_desc": "BASIC CHINESE",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8230,
		"subject_desc": "BIOLOGY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8231,
		"subject_desc": "BASIC MALAY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8232,
		"subject_desc": "CHEMISTRY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8233,
		"subject_desc": "CHINESE",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8234,
		"subject_desc": "CHINESE N(A)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8235,
		"subject_desc": "CHINESE B",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8236,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8237,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8238,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8239,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8240,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8241,
		"subject_desc": "FOOD & NUTRITION",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8242,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8243,
		"subject_desc": "GEOGRAPHY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8244,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8245,
		"subject_desc": "HISTORY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8246,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8247,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8248,
		"subject_desc": "LITERATURE(E)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8249,
		"subject_desc": "MATHEMATICS",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8250,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8251,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8252,
		"subject_desc": "MALAY",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8253,
		"subject_desc": "MALAY N(A)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8254,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8255,
		"subject_desc": "PHYSICS",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8256,
		"subject_desc": "SCIENCE",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8257,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8258,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8259,
		"subject_desc": "SOCIAL STUDIES N(T)",
		"school_name": "FAIRFIELD METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8260,
		"subject_desc": "ADDITIONAL MATHEMATICS",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8261,
		"subject_desc": "ART",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8262,
		"subject_desc": "BASIC CHINESE",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8263,
		"subject_desc": "BIOLOGY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8264,
		"subject_desc": "BASIC MALAY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8265,
		"subject_desc": "CHEMISTRY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8266,
		"subject_desc": "CHINESE",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8267,
		"subject_desc": "COMPUTING",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8268,
		"subject_desc": "COMPUTER APPLICATIONS",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8269,
		"subject_desc": "DESIGN & TECHNOLOGY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8270,
		"subject_desc": "ELEMENTS OF BUSINESS SKILLS",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8271,
		"subject_desc": "ENGLISH LANGUAGE",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8272,
		"subject_desc": "FOOD AND CONSUMER EDUCATION",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8273,
		"subject_desc": "GEOGRAPHY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8274,
		"subject_desc": "HIGHER CHINESE",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8275,
		"subject_desc": "HISTORY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8276,
		"subject_desc": "HIGHER MALAY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8277,
		"subject_desc": "HUMANITIES (SS, GEOGRAPHY)",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8278,
		"subject_desc": "HUMANITIES (SS, HISTORY)",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8279,
		"subject_desc": "LITERATURE(E)",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8280,
		"subject_desc": "MATHEMATICS",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8281,
		"subject_desc": "MALAY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8282,
		"subject_desc": "MUSIC",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8283,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8284,
		"subject_desc": "PHYSICS",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8285,
		"subject_desc": "PRINCIPLES OF ACCOUNTS",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8286,
		"subject_desc": "SCIENCE (CHEM, BIO)",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8287,
		"subject_desc": "SCIENCE (PHY, CHEM)",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8288,
		"subject_desc": "SCIENCE",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8289,
		"subject_desc": "SMART ELECTRICAL TECHNOLOGY",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8290,
		"subject_desc": "SOCIAL STUDIES",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8291,
		"subject_desc": "IPW",
		"school_name": "NGEE ANN SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8350,
		"subject_desc": "BASIC CHINESE",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8351,
		"subject_desc": "BASIC MALAY",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8352,
		"subject_desc": "BASIC TAMIL",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8353,
		"subject_desc": "CHARACTER & CITIZENSHIP (NT)",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8354,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8355,
		"subject_desc": "INFOCOMM TECHNOLOGY (NT)",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8356,
		"subject_desc": "ISC FACILITY SERVICES",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8357,
		"subject_desc": "ISC HOSPITALITY SERVICES",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8358,
		"subject_desc": "ISC MECHANICAL SERVICING",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8359,
		"subject_desc": "ISC RETAIL SERVICES",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8360,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8361,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8362,
		"subject_desc": "SCIENCE",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8363,
		"subject_desc": "TM - FABULOUS MERCHANDISE D.",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8364,
		"subject_desc": "TM - LOOKS GOOD, TASTES GOOD",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8365,
		"subject_desc": "TM - LET IT FLOW3",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8366,
		"subject_desc": "TM  - LIGHT UP THE WORLD",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8367,
		"subject_desc": "TM - PASSION TO SERVE",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8368,
		"subject_desc": "TM - SERVICE WITH A SMILE",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8369,
		"subject_desc": "TM - WHEELS ARE WONDERFUL",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8370,
		"subject_desc": "TM - WE CAN MAKE IT",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8371,
		"subject_desc": "VISUAL ARTS",
		"school_name": "CREST SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8372,
		"subject_desc": "BASIC CHINESE",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8373,
		"subject_desc": "BASIC MALAY",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8374,
		"subject_desc": "BASIC TAMIL",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8375,
		"subject_desc": "CO-CURRICULAR ACTIVITIES",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8376,
		"subject_desc": "CHARACTER & CITIZENSHIP (NT)",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8377,
		"subject_desc": "ENGLISH LANGUAGE (SYLL A)",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8378,
		"subject_desc": "ENGLISH LANGUAGE (SYLL T)",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8379,
		"subject_desc": "INFOCOMM TECHNOLOGY (NT)",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8380,
		"subject_desc": "MATHEMATICS (SYLLABUS A)",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8381,
		"subject_desc": "MATHEMATICS (SYLLABUS T)",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8382,
		"subject_desc": "PERFORMING ARTS",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8383,
		"subject_desc": "PHYSICAL EDUCATION",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8384,
		"subject_desc": "SCIENCE (SYLL T)",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8385,
		"subject_desc": "SCIENCE & TECHNOLOGY",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8386,
		"subject_desc": "ART",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}, {
		"_full_count": "3664",
		"_id": 8387,
		"subject_desc": "VOCATIONAL EDUCATION",
		"school_name": "SPECTRA SECONDARY SCHOOL",
		"rank": 0.0
	}
]"""


#convert from json to dict
x = json.loads(x)

#get data from dict and write to excel database

#open a workbook
wb = xlwt.Workbook()

#open a worksheet
ws = wb.add_sheet('subjectsOffered')

#write column headers
headers = ["_full_count", "_id", "subject_desc", "school_name", "rank"]

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
wb.save('subjectsOffered.xls')
