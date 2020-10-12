#commented

#make api call to get json data; https://data.gov.sg/api/action/datastore_search?resource_id=74362320-e29d-458f-aa56-d9971ee310fd&limit=98&q=SECONDARY

#import libraries
import json
import xlwt

#format json data
x = """[{
		"llp_title2": "na",
		"llp_title1": "Nurturing Mindful Leaders through Community Outreach",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "ADMIRALTY SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Design Thinking Through Innovation and Technology",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 1
	}, {
		"llp_title2": "na",
		"llp_title1": "Character Development through Outdoor Learning Experience (OLE)",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Languages & Humanities",
		"school_name": "AHMAD IBRAHIM SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Critical Social Inquiry and Media Literacy",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 2
	}, {
		"llp_title2": "na",
		"llp_title1": "Integrated Arts Programme",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "ANG MO KIO SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Environment Science & Technology",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 3
	}, {
		"llp_title2": "na",
		"llp_title1": "i-LEAD @ Bartley (Leadership Experience and Development)",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "BARTLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Chemical and Life Sciences (Perfumery)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 6
	}, {
		"llp_title2": "na",
		"llp_title1": "Beatty's Leaders for Life Programme",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "BEATTY SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Beattyians Think. Create. Innovate",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 7
	}, {
		"llp_title2": "na",
		"llp_title1": "PAssion Programme",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "BEDOK GREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "ilnquire. ilnnovate. Developing scientific thinking and inquiry skills through real-life applications",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 8
	}, {
		"llp_title2": "na",
		"llp_title1": "SHAPE @ BDS: A School of Healthy And Physically Educated Enthusiasts",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Interdisciplinary",
		"school_name": "BEDOK SOUTH SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Project S.H.I.N.E -- An Integrated Student-Centred and Holistic Programme that Develops Innovation and Nurtures Empathy",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 9
	}, {
		"llp_title2": "na",
		"llp_title1": "Good Values @ BV",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Languages & Humanities",
		"school_name": "BEDOK VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Global Awareness for the 21st Century @ BV",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 10
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing Student Leadership Through Service Learning",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "BENDEMEER SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Making Health Science Alive through Authentic Problem-Based Learning",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 11
	}, {
		"llp_title2": "na",
		"llp_title1": "Music & Performing Arts",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "BOON LAY SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Exploring Possibilities in Materials Science",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 12
	}, {
		"llp_title2": "na",
		"llp_title1": "Bowen ChANgemakers Programme",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Business & Entrepreneurship",
		"school_name": "BOWEN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Nurturing Creativity, Empathy and Enterprise through Social Entrepreneurship",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 13
	}, {
		"llp_title2": "na",
		"llp_title1": "Confidence And REsilience (CARE) though Aesthetics, Community and Youth Leadership",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "BROADRICK SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Broadrick Entrepreneurship in STEM",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 14
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing Community Youth Leadership through VIA - Journey to Become RESPECTful Leaders",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "BUKIT BATOK SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing Proactive Problem-Solvers who care for our World through STEM",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 15
	}, {
		"llp_title2": "na",
		"llp_title1": "Character Development & Leadership through Sports",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "BUKIT MERAH SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Creative Robotics and Engineering",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 16
	}, {
		"llp_title2": "na",
		"llp_title1": "Learning the Arts, Living the Values",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "BUKIT VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Clean Energy and Environmental Technology",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 17
	}, {
		"llp_title2": "na",
		"llp_title1": "Active Holistic Health Advocates (AHHAs) Championing Efforts towards a Healthier Community",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Aesthetics",
		"school_name": "CANBERRA SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Digital Media in Visual Arts",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 18
	}, {
		"llp_title2": "na",
		"llp_title1": "Service and Leadership through School to Nation",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "CHANGKAT CHANGI SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Programme SOAR (Student centered Opportunities for AeRospace Industry)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 19
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing Social Emotional Learning Competencies through Outdoor Adventure Learning",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "CHRIST CHURCH SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing 21st Century Competencies through an Inquiry approach  in Health Science and Technology",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 22
	}, {
		"llp_title2": "na",
		"llp_title1": "Student Leadership",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "CHUA CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Robotics & Automation for a Better Tomorrow",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 23
	}, {
		"llp_title2": "na",
		"llp_title1": "Leadership Development through Uniformed Groups",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "CLEMENTI TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "CODE: COmputing to Discover and Empower",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 25
	}, {
		"llp_title2": "na",
		"llp_title1": "Inspired North Stars Inspire Actions",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "COMPASSVALE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Aeronautics Applied Learning Programme",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 26
	}, {
		"llp_title2": "na",
		"llp_title1": "Character, Citizenship and Leadership Development through Water Sports",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "DAMAI SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Environmental & Health Sciences",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 27
	}, {
		"llp_title2": "na",
		"llp_title1": "Nurturing Confident Communicators and Gracious Citizens through the Arts",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "Languages & Humanities",
		"school_name": "DEYI SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Pen it down, Mike it up!",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 28
	}, {
		"llp_title2": "na",
		"llp_title1": "Every Dunearnite a Community Youth Leader",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "DUNEARN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "FSciTech: Developing Dunearnites as confident and creative young scientists through Food Science and Technology",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 29
	}, {
		"llp_title2": "na",
		"llp_title1": "Every Student a Leader",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "EAST SPRING SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Harnessing Energy to Live, Work and Play",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 30
	}, {
		"llp_title2": "na",
		"llp_title1": "Community and Youth Leadership through Service",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "EAST VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "21st Century Innovators through Health Science",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 31
	}, {
		"llp_title2": "na",
		"llp_title1": "Character Education Through Sports (Anchored on Taekwondo)",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Business & Entrepreneurship",
		"school_name": "EDGEFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Growing the Entrepreneurial Mindset (GEM)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 32
	}, {
		"llp_title2": "na",
		"llp_title1": "Strengthening Resilience and Character through Leadership and Sports Education",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Languages & Humanities",
		"school_name": "EVERGREEN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing Effective Communicators, Caring Leaders and Inventive Thinking through National Education",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 33
	}, {
		"llp_title2": "na",
		"llp_title1": "Rise to Lead",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "FAJAR SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Sustainability through 21st Century Applied Critical and Inventive Thinking Skills (ACIT)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 34
	}, {
		"llp_title2": "na",
		"llp_title1": "Values Through Dance",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "FUCHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Innovations in Science & Technology for Sustain-Ability",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 35
	}, {
		"llp_title2": "na",
		"llp_title1": "Values in Action, Leadership through Service",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "FUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Forensic Science@Fuhua",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 36
	}, {
		"llp_title2": "na",
		"llp_title1": "Nurturing Confident and Compassionate Leaders via Values-in-Action",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "GEYLANG METHODIST SCHOOL (SECONDARY)",
		"rank": 0.0,
		"alp_title": "Environmental Science and Sustainable Living",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 38
	}, {
		"llp_title2": "na",
		"llp_title1": "Character Development through Outdoor and Adventure Education",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "GREENDALE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "SMART Living: Design. Code. Build",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 39
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing Creative and Confident persons, impacting the community through the Arts",
		"llp_domain1": "Music & Performing Arts / Visual Arts & Design",
		"alp_domain": "Languages & Humanities",
		"school_name": "GREENRIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "The Use of Media in Engaging 21st Century Learners in the English Language Classroom -- Camera. Lights. Action. Programme (CLAP)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 40
	}, {
		"llp_title2": "na",
		"llp_title1": "heARTbeat -- Art for Life",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "GUANGYANG SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Environmental Science for Sustainable Living",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 41
	}, {
		"llp_title2": "na",
		"llp_title1": "Nurturing Confident and Passionate Hillgrovians through the Arts",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "HILLGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Broadening our Learning Horizons through Flight and Aerospace",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 43
	}, {
		"llp_title2": "na",
		"llp_title1": "Sports, Active LIving and Values Education (Sports A.L.I.V.E!)",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "HONG KAH SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Real World Learning through Electronics",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 45
	}, {
		"llp_title2": "na",
		"llp_title1": "GRC (Gratitude, Respect & Compassion) in Action, a Hougean way of life",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Languages & Humanities",
		"school_name": "HOUGANG SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "English Communication Skills through Authentic Learning",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 46
	}, {
		"llp_title2": "na",
		"llp_title1": "Community and Youth Leadership in Hua Yi",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "HUA YI SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Health Sciences: Healthcare technologies for the elderly",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 47
	}, {
		"llp_title2": "na",
		"llp_title1": "Cultivating Community Champions through Youth Leadership",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "JUNYUAN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing Application-based Learning through Food Science",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 48
	}, {
		"llp_title2": "na",
		"llp_title1": "Sporty at Heart, Sporting in Mind",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Languages & Humanities",
		"school_name": "JURONG SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Environmental Studies: An Inter-disciplinary Approach To Sustainable Urban Living",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 49
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing Character, Leadership and Citizenship",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Aesthetics",
		"school_name": "JURONG WEST SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Harnessing Technology, Communication and the Visual Arts in Authentic Contexts",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 50
	}, {
		"llp_title2": "na",
		"llp_title1": "Sports for Life - Character Education through Sports Exposure, Sports Empowerment and Sports Excellence",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "JURONGVILLE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "In Heath We Thrive - Connecting the Science and Skills of Health and Wellness",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 51
	}, {
		"llp_title2": "na",
		"llp_title1": "Performing Arts : iACE@Juying (I Appreciate, I Create, I Exhibit at Juying)",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "Languages & Humanities",
		"school_name": "JUYING SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing Confident & Competent Communicators through Oracy Skills Programme",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 52
	}, {
		"llp_title2": "na",
		"llp_title1": "EVOKE!@KR (Educational Values of Olympism at Kent Ridge) through Sports and Outdoor Education",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "KENT RIDGE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing Computational Thinking through Robotics",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 53
	}, {
		"llp_title2": "na",
		"llp_title1": "Nurturing a Leader in Every Kranjian through Community and Youth Leadership",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Interdisciplinary",
		"school_name": "KRANJI SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Nurturing Communities of Reflective and Independent Learners through Thinking Curriculum",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 54
	}, {
		"llp_title2": "na",
		"llp_title1": "Every KCPian a Servant Leader",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Languages & Humanities",
		"school_name": "KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Participate, Access/ Analyse, Create, Evaluate (P.A.C.E) in KCPSS Media Literacy Programme",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 55
	}, {
		"llp_title2": "na",
		"llp_title1": "Sports and Outdoor Education",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "LOYANG VIEW SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Design and Engineering",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 56
	}, {
		"llp_title2": "na",
		"llp_title1": "Learning through the ARTS",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "MANJUSRI SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Building Smart Homes with a Big Heart",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 57
	}, {
		"llp_title2": "na",
		"llp_title1": "Values and Character Building through Outdoor Curriculum (VALOUR)",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "MARSILING SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Eco-sustainability through Inquiry-Based Learning",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 58
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing a zest for life through aesthetics",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "Languages & Humanities",
		"school_name": "MAYFLOWER SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing confidence and curiosity through effective communication",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 59
	}, {
		"llp_title2": "na",
		"llp_title1": "Community and Youth Leadership",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Aesthetics",
		"school_name": "MERIDIAN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Aesthetics",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 60
	}, {
		"llp_title2": "na",
		"llp_title1": "Student Leadership through Outdoor Adventure & Sports",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "MONTFORT SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Made In Montfort  Design, Code, Make",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 61
	}, {
		"llp_title2": "na",
		"llp_title1": "Character Education through Sports Awareness, Commitment and Empowerment (SpACE)",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Aesthetics",
		"school_name": "NAVAL BASE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Applied Learning in Art",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 63
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing Confident & Compassionate Student Leaders to Lead, Serve & Excel",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Aesthetics",
		"school_name": "NEW TOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing critical and inventive thinkers through visual communication",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 64
	}, {
		"llp_title2": "na",
		"llp_title1": "Nurturing Creative Problem Solvers through the Arts & Design",
		"llp_domain1": "Visual Arts & Design",
		"alp_domain": "STEM",
		"school_name": "NORTH VISTA SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Investigative Science in Health & Sports",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 65
	}, {
		"llp_title2": "na",
		"llp_title1": "Northbrooks Outdoor Education: Adventure, Character, Environment (A.C.E.) Programme",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "NORTHBROOKS SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Northbrooks Aerospace Programme (Applied Learning In Aerospace)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 66
	}, {
		"llp_title2": "na",
		"llp_title1": "Game for Life  Developing Social Emotional Competencies through Sports and Physical Activities",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "NORTHLAND SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "ALP Health Sciences - Healthy Lifestyle and Caring for Elderly",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 67
	}, {
		"llp_title2": "na",
		"llp_title1": "OPSS CORE Programme  Orchid Park Secondary School Community OutReach Education Programme",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Aesthetics",
		"school_name": "ORCHID PARK SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "ARTopIA - Arts Appreciation & Values Inculcation through Visual Art",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 68
	}, {
		"llp_title2": "na",
		"llp_title1": "Sports for Life",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Business & Entrepreneurship",
		"school_name": "OUTRAM SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Business and Enterprise",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 69
	}, {
		"llp_title2": "na",
		"llp_title1": "Nurturing Crestian Leaders of Tomorrow through Music and the Performing Arts",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "Languages & Humanities",
		"school_name": "PASIR RIS CREST SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Effective Communicators of the 21st Century",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 70
	}, {
		"llp_title2": "na",
		"llp_title1": "Learning for Life Programme in Music and Performing Arts through SHINE@PRSS",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "Humanities",
		"school_name": "PASIR RIS SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Applied Learning in Humanities and Languages through Project DRIVE!",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 71
	}, {
		"llp_title2": "na",
		"llp_title1": "PRIDE of the Community: Developing Altruists",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "PEI HWA SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Robotics and Programming - Nurturing Leaders, Scholars and Altruists",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 72
	}, {
		"llp_title2": "na",
		"llp_title1": "Becoming Persons for Others  Leadership through and for the Community",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "PEICAI SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "We are what we eat; and what we do  Knowing Better; Living Healthier; Transforming Lives",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 73
	}, {
		"llp_title2": "na",
		"llp_title1": "Community & Youth Leadership",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Languages",
		"school_name": "PEIRCE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Broadcast Journalism",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 74
	}, {
		"llp_title2": "na",
		"llp_title1": "Leadership through CCE",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "PING YI SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Design Education and Aeronautical Engineering",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 75
	}, {
		"llp_title2": "na",
		"llp_title1": "Serving with values and good habits, developing the 21st century gentlemen/ ladies",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "PUNGGOL SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Environment Education",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 77
	}, {
		"llp_title2": "na",
		"llp_title1": "Community & Youth Leadership",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Humanities",
		"school_name": "QUEENSTOWN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Minds for the Future  First Cultivating the Disciplined and Synthesising Mind",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 78
	}, {
		"llp_title2": "na",
		"llp_title1": "Sports for Life & Outdoor Education Programme: Nurturing Responsible Citizens and Life-long Learners",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "QUEENSWAY SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Environmental Science Applied Learning Programme: Developing Confident Learners and Caring Citizens",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 79
	}, {
		"llp_title2": "na",
		"llp_title1": "Empowering every Regenite to be a Responsible and Confident Leader, Committed to Excellence",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "REGENT SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Engineering @ Regent",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 80
	}, {
		"llp_title2": "na",
		"llp_title1": "Arts for Life",
		"llp_domain1": "Music & Performing Arts / Visual Arts & Design",
		"alp_domain": "Languages & Humanities",
		"school_name": "RIVERSIDE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Global Citizenship Education through Critical Social Inquiry",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 81
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing Community Leaders through VIA and Outdoor Education",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Languages & Humanities",
		"school_name": "SEMBAWANG SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Critical & Inventive Thinking (CIT) thru Media Literacy",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 82
	}, {
		"llp_title2": "na",
		"llp_title1": "Building Character Through Physical Education & Sports",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "SENG KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Health Science & Technology",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 83
	}, {
		"llp_title2": "na",
		"llp_title1": "Nurturing Confident and Compassionate Leaders through Uniformed Groups",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Humanities",
		"school_name": "SERANGOON GARDEN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Researching Society using Media Communication",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 84
	}, {
		"llp_title2": "na",
		"llp_title1": "Project Ablaze: Harnessing Student Leadership in the Service of Community",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "SERANGOON SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Real-world Explorations in ICT",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 85
	}, {
		"llp_title2": "na",
		"llp_title1": "Sports and Outdoor Experiences foR Values Education (SERVE)",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "SHUQUN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Shuqun Computing for Applied Learning and Robotics (ScOAR)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 86
	}, {
		"llp_title2": "na",
		"llp_title1": "GEARing Springfielders for Success - Grounding in Values, Engaged to Learn and Lead, Aspiring to Serve, Ready to Soar",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "SPRINGFIELD SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Exploring Health Sciences through SP<sup>2</sup>A",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 87
	}, {
		"llp_title2": "na",
		"llp_title1": "Saints Rugby for Life",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "ST. ANDREW'S SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Saints Engineering Design Programme",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 88
	}, {
		"llp_title2": "na",
		"llp_title1": "Developing Life Skills through Uniformed Groups Experience",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "ST. GABRIEL'S SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Project GaIA - Gabrielites Inspired for Aviation",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 89
	}, {
		"llp_title2": "na",
		"llp_title1": "Develop the Whole Person through Sports and Outdoor Education",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Languages & Humanities",
		"school_name": "ST. HILDA'S SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "iTHink -- the HILDAN Approach to Learning the English Language",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 90
	}, {
		"llp_title2": "na",
		"llp_title1": "Swiss Thoughtful Leadership Programme",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "SWISS COTTAGE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Applied Sciences for Sustainable Development",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 92
	}, {
		"llp_title2": "na",
		"llp_title1": "Creative Expressions: Expressing creatively through visual and performing arts (Arts Education)",
		"llp_domain1": "Music & Performing Arts / Visual Arts & Design",
		"alp_domain": "STEM",
		"school_name": "TAMPINES SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Creative Engineering: Inter-disciplinary Authentic Problem Solving",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 93
	}, {
		"llp_title2": "na",
		"llp_title1": "S3 through the Arts@Tanglin Secondary School (TSS)",
		"llp_domain1": "Music & Performing Arts / Visual Arts & Design",
		"alp_domain": "Languages & Humanities",
		"school_name": "TANGLIN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Tanglin P.L.U.S. (Perspectives and Literacies to Understand Society)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 94
	}, {
		"llp_title2": "na",
		"llp_title1": "Sports and Sportsmanship Programme @ TWSS (Experience, Expose, Excel)",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "TECK WHYE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Re-designing the Future with Materials Science",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 95
	}, {
		"llp_title2": "na",
		"llp_title1": "Lead through Outdoor and Sporting Adventures",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "UNITY SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Inspire through Scientific Innovation and Enterprise",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 96
	}, {
		"llp_title2": "na",
		"llp_title1": "FOCUS (Finding, Optimising, Communicating, Understanding Sports)",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "Languages & Humanities",
		"school_name": "WEST SPRING SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Effective Communication and Critical Thinking through Media Literacy",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 97
	}, {
		"llp_title2": "na",
		"llp_title1": "Arts for Life (AfL)",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "Business & Entrepreneurship",
		"school_name": "WESTWOOD SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Innovation & Social Entrepreneurship",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 98
	}, {
		"llp_title2": "na",
		"llp_title1": "Active Citizenship for Social Change",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Languages",
		"school_name": "WHITLEY SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Speech Communication Arts",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 99
	}, {
		"llp_title2": "na",
		"llp_title1": "Learners and Leaders for Life",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "WOODGROVE SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Materials Science for Sustainable Living",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 100
	}, {
		"llp_title2": "na",
		"llp_title1": "Student Leadership Development through Involvement in the Community Programme",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "WOODLANDS RING SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "The Robotics Education & Enterprise (TREE)",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 101
	}, {
		"llp_title2": "na",
		"llp_title1": "Active Glocal Citizens Programme",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "STEM",
		"school_name": "WOODLANDS SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Real Food, Real Science",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 102
	}, {
		"llp_title2": "na",
		"llp_title1": "Growing Character Leadership through Arts, Media and Design",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "STEM",
		"school_name": "YIO CHU KANG SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Developing inquiring minds and creative learners through Arduino",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 103
	}, {
		"llp_title2": "na",
		"llp_title1": "Leadership for Life",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Aesthetics",
		"school_name": "YISHUN SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Sonic Arts  Applied Learning in Music, Media and Technology",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 104
	}, {
		"llp_title2": "na",
		"llp_title1": "Dragonboat -- gRowing Values: Mastering Core Dragon Boating Skills and Embracing the Values it Embodies",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "YUAN CHING SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Marine Architecture and Engineering",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 105
	}, {
		"llp_title2": "na",
		"llp_title1": "MELODY- Music Empowered Learners, Our Dynamic Yuhuans",
		"llp_domain1": "Music & Performing Arts",
		"alp_domain": "Business & Entrepreneurship",
		"school_name": "YUHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Integrated Events and Project Management",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 106
	}, {
		"llp_title2": "na",
		"llp_title1": "H2eArts in Tune Programme: History & Heritage through Arts & Music Programme",
		"llp_domain1": "Music & Performing Arts / Visual Arts & Design",
		"alp_domain": "STEM",
		"school_name": "YUSOF ISHAK SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Programme for Authentic Science, Technology and Environmental Learning",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 107
	}, {
		"llp_title2": "na",
		"llp_title1": "Totally Wholesome Engaged and Empowered TeenS (TWEETS)",
		"llp_domain1": "Community & Youth Leadership",
		"alp_domain": "Business & Entrepreneurship",
		"school_name": "YUYING SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Fostering  Inventive and  Critical Thinking through Design Thinking for Enterprising Learners",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 108
	}, {
		"llp_title2": "na",
		"llp_title1": "Outdoor Education for Character & Leadership Development",
		"llp_domain1": "Sports & Outdoor Education",
		"alp_domain": "STEM",
		"school_name": "ZHENGHUA SECONDARY SCHOOL",
		"rank": 0.0,
		"alp_title": "Game Design and Simulation and Robotics",
		"_full_count": "98",
		"llp_domain2": "na",
		"_id": 109
	}
]"""


#convert from json to dict
x = json.loads(x)

#get data from dict and write to excel database

#open a workbook
wb = xlwt.Workbook()

#open a worksheet
ws = wb.add_sheet('schoolDistinctiveProgs')

#write column headers
headers = ["llp_title2", "llp_title1", "llp_domain1", "alp_domain", "school_name", "rank", "alp_title", "_full_count", "llp_domain2", "_id"]

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
wb.save('schoolDistinctiveProgs.xls')